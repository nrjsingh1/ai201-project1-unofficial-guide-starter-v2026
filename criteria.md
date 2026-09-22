# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in week 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next week costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
One of my test questions covers a specific detail mentioned in only a single document with non-standard phrasing, making it significantly harder to retrieve than the rest. Expecting 4 out of 5 allows for this single edge case while ensuring the overall retrieval pipeline works reliably.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
This is set to 100% (5 of 5) because source citation is strictly enforced in the system's prompt instructions (`GROUNDING_INSTRUCTION`)[cite: 1]. If the prompt logic and grounding pipeline are working correctly, the model should never output an answer without citing its origin file[cite: 1].

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries[cite: 1].

**Why this target:**
The distance scores for out-of-scope questions typically sit cleanly above the 0.6 threshold, but occasional keyword overlaps with general vocabulary in the corpus can yield a false match[cite: 1]. Setting the target at 4 of 5 accounts for minor embedding noise while ensuring out-of-bounds queries are reliably filtered out[cite: 1].

---

## 4. Chunk completeness and boundary integrity

At least 4 of 5 sampled chunks read as a complete, self-contained thought without cutting mid-sentence at either the start or end of the chunk text.

**Why this target:**
Choosing a paragraph- or sentence-aware chunking strategy with appropriate overlap prevents sentences from being severed mid-thought. A 4 of 5 target ensures the chunker preserves context integrity across structural boundaries, while allowing for occasional awkward splits in unusually long or dense single-sentence paragraphs.

---

## 5. Answer factual grounding and citation accuracy

For at least 4 of 5 test questions, the system's generated answer contains only facts explicitly present in the retrieved chunks and correctly matches the cited source file name.

**Why this target:**
Having source citations present is not enough; the cited sources must match the actual document from which the chunk was extracted, and the LLM must not hallucinate facts outside the provided text. Target 4 of 5 ensures high factual precision while allowing tolerance for minor summary phrasing variations.

---