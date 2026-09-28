"""
The relevance gate.

This runs *before* the model does. It looks at how close the best retrieved
chunk actually is, and if nothing came back close enough it refuses the
question outright.

Why this exists as its own step, rather than just asking the model nicely to
admit when it doesn't know: if you only ask nicely, it will sometimes ignore
you and write something confident and wrong. Those answers are much harder to
catch than obvious errors. Deciding in your own code when there's nothing worth
answering from is more reliable than hoping.

You keep the polite instruction too — it's in generate.py — but as a second
layer. The gate catches the clear misses; the prompt catches the near ones.
"""

import re
from dataclasses import dataclass

import config
from store import Result

REFUSAL = "I don't have enough information about that."

# Deliberately duplicated from scorer.py rather than imported. scorer.py is the
# test harness; this is the thing being tested. A gate that shares its word
# splitting with the scorer that grades it can't be caught disagreeing with it.
_STOPWORDS = {
    "a", "about", "after", "all", "am", "an", "and", "any", "are", "as", "at",
    "be", "been", "before", "but", "by", "can", "did", "do", "does", "for",
    "from", "had", "has", "have", "how", "i", "if", "in", "into", "is", "it",
    "its", "just", "me", "my", "no", "not", "of", "on", "or", "our", "out",
    "over", "should", "so", "than", "that", "the", "their", "them", "then",
    "there", "these", "they", "this", "to", "up", "was", "we", "what", "when",
    "where", "which", "who", "why", "will", "with", "would", "you", "your",
}
_STEM = 5


def _stems(text: str) -> set[str]:
    words = re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).split()
    return {w[:_STEM] for w in words if w not in _STOPWORDS and len(w) > 1}


def lexical_support(question: str, results: list[Result]) -> float:
    """
    Fraction of the question's content words that appear in the nearest chunk.

    The second opinion on whether a question is answerable from this corpus,
    and deliberately a different kind of signal from distance: distance asks
    whether the question *resembles* the chunk, this asks whether they are
    about the same nouns.

    Measured against the nearest chunk alone. Against all of top-k it stops
    working — a question only has to find its vocabulary scattered across five
    unrelated chunks, and "How do I appeal a parking ticket?" scores 0.667 that
    way, higher than four of the five questions the system can really answer.
    """
    wanted = _stems(question)
    if not wanted or not results:
        return 0.0
    nearest = min(results, key=lambda r: r.distance)
    return len(wanted & _stems(nearest.text)) / len(wanted)


@dataclass
class GateDecision:
    passed: bool
    best_distance: float
    threshold: float
    lexical: float | None = None
    lexical_min: float = 0.0

    @property
    def explanation(self) -> str:
        if self.passed:
            return (
                f"best distance {self.best_distance:.3f} "
                f"is under the {self.threshold} cutoff"
            )
        if self.lexical is not None and self.lexical < self.lexical_min:
            return (
                f"best distance {self.best_distance:.3f} is under the "
                f"{self.threshold} cutoff, but only {self.lexical:.2f} of the "
                f"question's words appear in that chunk "
                f"(needs {self.lexical_min}) — refusing"
            )
        return (
            f"best distance {self.best_distance:.3f} "
            f"is over the {self.threshold} cutoff — refusing"
        )


def check(
    results: list[Result],
    threshold: float | None = None,
    question: str | None = None,
    lexical_min: float | None = None,
) -> GateDecision:
    """
    Decide whether the retrieved chunks are close enough to answer from.

    Remember: LOWER distance is better. A question passes when its best chunk
    is *under* the threshold.

    When `lexical_min` is above zero and a `question` is supplied, the question
    must clear a second, independent bar as well — see `lexical_support`. The
    two are combined with AND, so this can only ever refuse more than distance
    alone, never less. `lexical_min` defaults to `config.LEXICAL_MIN`, which
    ships at 0 and disables the check.
    """
    threshold = config.THRESHOLD if threshold is None else threshold
    lexical_min = config.LEXICAL_MIN if lexical_min is None else lexical_min

    if not results:
        return GateDecision(passed=False, best_distance=1.0, threshold=threshold)

    best = min(r.distance for r in results)
    passed = best < threshold

    lexical = None
    if lexical_min > 0 and question is not None:
        lexical = lexical_support(question, results)
        passed = passed and lexical >= lexical_min

    return GateDecision(
        passed=passed,
        best_distance=best,
        threshold=threshold,
        lexical=lexical,
        lexical_min=lexical_min,
    )
