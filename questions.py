"""
Your test questions.

Milestone 2 asks you to write five questions your system should be able to
answer from your corpus, specific enough to have a right answer.

  ✗ "What are good dining halls?"          — no right answer
  ✓ "What do students say about wait times at Commons during lunch?"

Fill in `QUESTIONS` below. `expects` is a word or short phrase you'd expect a
correct answer to contain — you'll use it in week 2 when you build a scorer,
and having written it now means you decided what "correct" meant before you saw
any results.

`OUT_OF_SCOPE` holds five questions your documents clearly don't cover. You
need these in Milestone 4 to find where your relevance cutoff belongs, and
again in week 2, where `run_eval.py` runs them through the gate and writes what
happened into your run log — that's the evidence for criterion 3.

Swap them for your own if you like. Keep five of them either way: criterion 3
names a target of "4 of 5", and four of three is not a thing.
"""

QUESTIONS = [
    # {"question": "...", "expects": "..."},
    {"question": "I cant buy parking permit, its all sold out , where can i park legally?", "expects": "Verrill Street "},
    {"question": "I am using student account cloud drive for my personal files and I am graduating next month, how long my files are safe?", "expects": "Six months after graduation"},
    {"question": "I want to get checked by doctor urgently can wait for appointments , what should I do ?", "expects": "go at 8am and wait rather than booking"},
    {"question": "When is the best time to apply for on campus jobs?", "expects": "first week of each semester and go fast"},
    {"question": "I dont want to wait , which is the best time to do laundry ?", "expects": "Best time to do laundry here is Tuesday or Wednesday morning. Sunday after 6pm you will wait."},
]

# Questions from a different world entirely. Your gate should refuse all five.
#
# There are five of these because criterion 3 in criteria.md names a target of
# "at least 4 of 5" — you need five things to try before you can report 4 of 5.
# `run_eval.py` runs these through retrieval and the gate on every eval and
# records what happened, so criterion 3 has evidence in the run log alongside
# the others. They cost no model calls: a refusal never reaches the model.
OUT_OF_SCOPE = [
    "What is the capital of Mongolia?",
    "How do I change the oil in a diesel engine?",
    "Who won the 1994 World Cup?",
    "What is the recommended dosage of ibuprofen for a headache?",
    "How do I write a for loop in Rust?",
]


# Campus questions the corpus genuinely does not cover — added in Unit 2
# Milestone 3 as diagnostic evidence, not as a fix.
#
# OUT_OF_SCOPE above is drawn from a different world entirely (Mongolia, Rust,
# the 1994 World Cup), and the gate refuses all five without breaking a sweat.
# That made criterion 3 look stronger than it is. These are the questions a
# real student would plausibly ask this system: on-topic for a campus, absent
# from these documents. They are the harder half of the test, and the gate
# scores 6 of 8 on them.
#
# Nothing reads this list automatically. It is here so the Milestone 3
# diagnosis can be re-run rather than taken on trust.
NEAR_MISS = [
    "What are the opening hours for the campus gym?",
    "How do I appeal a parking ticket?",
    "Where do I pick up a package that was mailed to me?",
    "Is there somewhere to store my bike over the winter?",
    "How do I register with disability services for exam accommodations?",
    "When is the spring career fair?",
    "How do I set up a tuition payment plan?",
    "Can I call campus security for a walk home at night?",
]


# The same five facts as QUESTIONS, asked in words the corpus does not use —
# added in Unit 2 Milestone 4.
#
# These are what killed the lexical gate. Every question in QUESTIONS above was
# written while reading the documents, so each one arrives carrying the
# corpus's own vocabulary, and any test built only on them will score a
# word-overlap check as excellent. A real student has not read the documents.
# Rewording the same five questions drops the gate from 3 of 5 admitted to 0
# of 5 once the lexical check is switched on.
REWORDED = [
    "The permits are gone for the year. Is there anywhere I can leave my car without getting fined?",
    "After I finish my degree, how long before the university deletes what I uploaded?",
    "I need to see someone about a medical problem today, not in a week. Options?",
    "What point in the year should I be looking for paid work run by the university?",
    "Which day and hour should I pick if I want a free machine straight away?",
]


def answered() -> list[dict]:
    """The questions you've actually filled in."""
    return [q for q in QUESTIONS if q.get("question", "").strip()]
