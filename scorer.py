"""
The scorer: what counts as a correct answer.

`run_eval.py` finds `judge` automatically and uses it to fill the Run columns.
Everything else here exists because the run log in README.md is one row per
CRITERION, and `judge` only returns one boolean per question. So each criterion
that depends on a run gets its own function, `judge` combines the ones about
the answer, and every call appends a record to results/scorer_ledger.jsonl so
the per-criterion counts can be added up afterwards from real data rather than
from memory.

Criteria (from criteria.md):

  1. Retrieved chunks contain the answer  -> retrieval_hit()    per run
  2. Every answer names a source          -> names_a_source()   per run
  3. Gate stops out-of-corpus questions   -> run_eval.py::check_out_of_scope
  4. Chunk completeness at boundaries     -> chunk_integrity()  deterministic
  5. Grounded facts + accurate citation   -> grounded_answer()  per run

HOW MATCHING WORKS, and why it isn't exact string matching.

`expects` in questions.py is a phrase the corpus actually uses, but neither the
chunk nor the model reproduces it verbatim: the corpus says "six months after
you graduate" where `expects` says "Six months after graduation", and the model
paraphrases on top of that. Exact substring matching would score those as
failures, which would be a measurement bug, not a finding.

So: strip both sides to content words (no stopwords, no punctuation, no case),
compare on a five-character prefix so graduate/graduation/graduating collapse
together, and call it a match when at least COVERAGE of the expected content
words are present. The prefix rule is deliberately loose in one direction — it
can match a word that merely starts the same — which is the trade accepted to
avoid failing on ordinary inflection.

`python scorer.py` runs the deterministic criteria (3 and 4) and prints them.
"""

import json
import re
import string

import config

# Fraction of the expected content words that must be present. 0.6 leaves room
# for the model dropping a word or two while paraphrasing, without letting a
# single shared word carry a match.
COVERAGE = 0.6

# Length of the prefix two words must share to count as the same word.
# graduate/graduation/graduating -> "gradu"; month/months -> "month".
STEM = 5

STOPWORDS = {
    "a", "about", "after", "all", "am", "an", "and", "any", "are", "as", "at",
    "be", "been", "before", "but", "by", "can", "did", "do", "does", "for",
    "from", "had", "has", "have", "how", "i", "if", "in", "into", "is", "it",
    "its", "just", "me", "my", "no", "not", "of", "on", "or", "our", "out",
    "over", "should", "so", "than", "that", "the", "their", "them", "then",
    "there", "these", "they", "this", "to", "up", "was", "we", "what", "when",
    "where", "which", "who", "why", "will", "with", "would", "you", "your",
}

LEDGER = config.RESULTS_DIR / "scorer_ledger.jsonl"


# ─── Word matching ───────────────────────────────────────────────────────────

def content_words(text: str) -> list[str]:
    """Lowercase alphanumeric words, stopwords and one-character tokens dropped."""
    words = re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).split()
    return [w for w in words if w not in STOPWORDS and len(w) > 1]


def _stems(text: str) -> set[str]:
    return {w[:STEM] for w in content_words(text)}


def covers(text: str, expects: str) -> bool:
    """True when `text` carries at least COVERAGE of the words in `expects`."""
    wanted = _stems(expects)
    if not wanted:
        return False
    found = _stems(text)
    return len(wanted & found) / len(wanted) >= COVERAGE


# ─── Criterion 1 — retrieved chunks contain the answer ───────────────────────

def retrieval_hit(expects: str, results) -> bool:
    """
    Did retrieval put the answer in front of the model at all?

    Measured against each chunk on its own, not the chunks concatenated: the
    criterion says one retrieved chunk contains the answer, and a phrase that
    is only assembled by gluing five unrelated chunks together isn't that.
    """
    return any(covers(r.text, expects) for r in results)


# ─── Criterion 2 — every answer names a source ───────────────────────────────

def cited_sources(answer: str, results) -> list[str]:
    """Which of the retrieved source filenames the answer actually names."""
    text = (answer or "").lower()
    cited = []
    for source in {r.source for r in results}:
        stem = source.rsplit(".", 1)[0].lower()
        if source.lower() in text or stem in text:
            cited.append(source)
    return sorted(cited)


def names_a_source(answer: str, results) -> bool:
    return bool(cited_sources(answer, results))


# ─── Criterion 5 — grounded facts and an accurate citation ───────────────────

CITATION_SCAFFOLD = {"source", "sources", "txt", "according", "also", "found",
                     "document", "documents", "file", "mentioned", "states"}


def unsupported_words(answer: str, results) -> list[str]:
    """
    Words in the answer that appear in no retrieved chunk.

    Criterion 5 has two halves. `grounded_answer` below covers the second —
    the citation points at a file that really carries the fact. This covers the
    first: "contains ONLY facts explicitly present in the retrieved chunks."
    Nothing in `judge` was checking that, so it was being asserted rather than
    measured.

    This is a screen, not a verdict. It flags words, and a word is not a fact:
    citation scaffolding ("Source:", "according to") and paraphrase that echoes
    the question ("avoid", "apply") both surface here and neither is a
    fabrication. What it is good for is making sure nothing gets asserted
    without a human looking at it — anything it flags has to be read.
    """
    supported = set()
    for r in results:
        supported |= _stems(r.text)
    for r in results:
        supported |= _stems(r.source.replace("_", " ").replace(".txt", ""))
    return sorted(
        w for w in content_words(answer)
        if w[:STEM] not in supported and w not in CITATION_SCAFFOLD
    )


def grounded_answer(expects: str, answer: str, results) -> bool:
    """
    Stricter than criterion 2. The answer has to carry the expected fact, AND
    the file it cites has to be a file that genuinely contains that fact —
    not just any of the five chunks that happened to come back.
    """
    if not covers(answer, expects):
        return False
    bearing = {r.source for r in results if covers(r.text, expects)}
    return bool(bearing & set(cited_sources(answer, results)))


# ─── Criterion 4 — chunk boundary integrity ──────────────────────────────────

OPENERS = tuple(string.ascii_uppercase) + tuple("0123456789-•#\"'(")


def chunk_integrity(text: str) -> bool:
    """
    Does this chunk read as a complete thought rather than a severed sentence?

    Starts on something that can begin a sentence — a capital, a digit, a
    bullet, an opening quote — and ends on terminal punctuation.
    """
    body = (text or "").strip()
    if not body:
        return False
    return body.startswith(OPENERS) and body.endswith((".", "!", "?", ":"))


# ─── What run_eval.py calls ──────────────────────────────────────────────────

def judge(question, expects, answer, results) -> bool:
    """
    The per-question verdict run_eval.py records in its Run columns.

    A question passes when the answer says the right thing and names a source
    that actually says it — criteria 2 and 5 together. Criterion 1 is recorded
    alongside it in the ledger rather than folded in here, because retrieval
    finding the answer and the model using it are separate failures and the run
    log has separate rows for them.
    """
    record = {
        "question": question,
        "expects": expects,
        "c1_retrieval_hit": retrieval_hit(expects, results),
        "c2_names_source": names_a_source(answer, results),
        "c5_grounded": grounded_answer(expects, answer, results),
        "c5_unsupported": unsupported_words(answer, results),
        "cited": cited_sources(answer, results),
        "best_distance": min((r.distance for r in results), default=1.0),
    }
    config.RESULTS_DIR.mkdir(exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record) + "\n")

    return record["c2_names_source"] and record["c5_grounded"]


# ─── The deterministic criteria, run on their own ────────────────────────────

def main():
    """Criteria 3 and 4: no model calls, no variation between runs."""
    import gate
    import questions as qs
    from chunker import split_documents
    from ingest import load_documents
    from store import search

    print(f"Criterion 3 — the gate on out-of-corpus questions (cutoff {config.THRESHOLD})")
    refused = 0
    for question in qs.OUT_OF_SCOPE:
        results = search(question, top_k=config.TOP_K, corpus=config.CORPUS)
        decision = gate.check(results)
        refused += not decision.passed
        print(f"  {'refused    ' if not decision.passed else 'LET THROUGH'} "
              f"{decision.best_distance:.3f}  {question}")
    print(f"  -> {refused} of {len(qs.OUT_OF_SCOPE)}\n")

    print("Criterion 4 — chunk boundary integrity (5 chunks, evenly spaced)")
    chunks = split_documents(load_documents(config.CORPUS))
    # Evenly spaced rather than the first five, so the sample spans the whole
    # corpus instead of five chunks off the same couple of documents.
    step = max(1, len(chunks) // 5)
    sample = chunks[::step][:5]
    print(f"  {len(chunks)} chunks total, sampling every {step}th")
    intact = 0
    for chunk in sample:
        ok = chunk_integrity(chunk.text)
        intact += ok
        body = chunk.text.strip()
        print(f"  {'intact' if ok else 'CUT   '}  {chunk.source}#{chunk.index}")
        print(f"          starts: {body[:60]!r}")
        print(f"          ends:   {body[-60:]!r}")
    print(f"  -> {intact} of {len(sample)}")


if __name__ == "__main__":
    main()
