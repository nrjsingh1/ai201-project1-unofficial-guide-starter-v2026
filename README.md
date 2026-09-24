# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none, because the grader can't
> read it.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Week 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:**
**Overlap:**

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->
### Sample Chunks

#### Chunk 1
- **Source:** `admin_add_drop_deadline.txt#0`
- **Produced by:** `chunker.py::split_documents`

> **On the add/drop deadline**
> 
> You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on yourtranscript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

---

#### Chunk 2
- **Source:** `course_biol_160_exams.txt#0`
- **Produced by:** `chunker.py::split_documents`

> **BIOL 160 Cell Biology — assessment**
> 
> Four unit tests and a cumulative final. Not curved.
> 
> The unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.

---

#### Chunk 3
- **Source:** `course_math_220_exams.txt#0`
- **Produced by:** `chunker.py::split_documents`

> **MATH 220 Linear Algebra — assessment**
> 
> Two midterms and a cumulative final. Curved to a b- median.
> 
> The problem sets are the course; the lectures make sense afterwards rather than during.

---

#### Chunk 4
- **Source:** `dining_the_ridgeway_cafe.txt#0`
- **Produced by:** `chunker.py::split_documents`

> **The Ridgeway Café**
> 
> Second-year here. Wait times: 10 to 15 minutes at 12:30, none after 2:00. The thing worth going for is the only place on campus with real espresso. The thing to know is that seating is tight; about 40 seats for a building of 900.
> 
> Hours are 7:00am to 4:00pm weekdays only. Costs declining balance only, no meal swipes.

---

#### Chunk 5
- **Source:** `housing_innisfree_hall_laundry.txt#0`
- **Produced by:** `chunker.py::split_documents`

> **Laundry in Innisfree Hall**
> 
> Machines take $1.75 wash, $1.75 dry, app-based. There are eight washers and six dryers for the building, which is the wrong ratio and means the dryers back up on Sunday evenings.
> 
> Best time to do laundry here is Tuesday or Wednesday morning. Sunday after 6pm you will wait.


## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
"I am using student account cloud drive for my personal files and I am graduating next month, how long my files are safe?"

**Answer:**
======================================================================
System instruction sent with the prompt
======================================================================
You answer questions using only the documents provided to you.

Rules:
- Use only the information in the documents below. Do not use anything you know from elsewhere.
- If the documents don't cover the question, say you don't have enough information. Do not guess.
- Name the document your answer came from, using the filename given in each excerpt.
- Be brief. Two or three sentences is usually enough.

======================================================================
The assembled prompt, exactly as sent
======================================================================
Documents:

[from admin_wifi_and_accounts.txt]
On the wifi and accounts

Your student account gives you campus wifi, printing, and a cloud drive with unlimited storage that most people never discover. The account stays active for six months after you graduate, and the cloud drive is purged at that point without a second warning.

[from course_cs_210_workload.txt]
Workload for CS 210 Data Structures

People keep asking so: 8 to 10 hours a week outside class. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.

[from course_cs_340_workload.txt]
Workload for CS 340 Databases

People keep asking so: 6 hours a week early, 15 in the last three weeks when the project lands. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.

[from course_cs_340.txt]
CS 340 Databases

I'm a junior and I've done this twice now. Format is lecture twice a week plus a project that runs the whole term. Assessment: one midterm and a final, both open-book. Lightly curved, usually two or three points.

Expect 6 hours a week early, 15 in the last three weeks when the project lands.

The one piece of advice: start the term project in week three, not week eight; everyone learns this the hard way.

[from course_stat_150_workload.txt]
Workload for STAT 150 Applied Statistics

People keep asking so: 5 to 6 hours a week outside class. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.

---

Question: I am using student account cloud drive for my personal files and I am graduating next month, how long my files are safe?

Answer using only the documents above, and name the file you used.
======================================================================

Your student account and its cloud drive stay active for six months after you graduate, and the cloud drive is purged at that point (admin_wifi_and_accounts.txt).

Sources retrieved: admin_wifi_and_accounts.txt, course_cs_210_workload.txt, course_cs_340.txt, course_cs_340_workload.txt, course_stat_150_workload.txt

0 model calls this session, 1 served from cache

```
```

**My relevance cutoff: 0.6**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->



| Question | In Corpus? | Best Distance |
| :--- | :---: | :---: |
| "I cant buy parking permit, its all sold out , where can i park legally?" | Yes | 0.432 |
| "I am using student account cloud drive for my personal files and I am graduating next month, how long my files are safe?" | Yes | 0.340 |
| "I want to get checked by doctor urgently can wait for appointments , what should I do ?" | Yes | 0.536 |
| "When is the best time to apply for on campus jobs?" | Yes | 0.582 |
| "I dont want to wait , which is the best time to do laundry ?" | Yes | 0.446 |

| Question | In Corpus? | Best Distance | Gated / Refused? |
| :--- | :---: | :---: | :---: |
| "What is the capital of Mongolia?" | No | 0.825 | Yes |
| "How do I change the oil in a diesel engine?" | No | 0.934 | Yes |
| "Who won the 1994 World Cup?" | No | 0.886 | Yes |
| "What is the recommended dosage of ibuprofen for a headache?" | No | 0.844 | Yes |
| "How do I write a for loop in Rust?" | No | 0.896 | Yes |




## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**

**2.**

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Week 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     week 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     week — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
