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
I asdked gemini to explain me about the tasks for milestones that I could not understand.

**2.**
I used AI to format the texts that I have to put in the readme or criteria files.

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

Evidence: [`results/run_2026-09-27_1939_before.md`](results/run_2026-09-27_1939_before.md),
produced by `run_eval.py::main` — 5 questions × 3 runs, caching off, 15 real
model calls. Corpus `campus_life`, top-k 5, cutoff 0.6.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk completeness and boundary integrity | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Answer factual grounding and citation accuracy | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Criteria 3 and 4 show the same number in all three columns because neither
depends on the model. Criterion 3 is retrieval plus a comparison against a
fixed number; criterion 4 is a property of the chunker. One pass is the whole
measurement. Criteria 1, 2 and 5 were measured on all three runs separately and
happened not to move — the distances were identical run to run, and the model
paraphrased differently each time without ever dropping the fact or the
citation.

### How each cell was measured

| Criterion | File and function |
|---|---|
| 1 | `scorer.py::retrieval_hit`, called from `scorer.py::judge` via `run_eval.py::main` |
| 2 | `scorer.py::names_a_source` (uses `scorer.py::cited_sources`) |
| 3 | `run_eval.py::check_out_of_scope`, gate logic in `gate.py::check` |
| 4 | `scorer.py::chunk_integrity`, sampled in `scorer.py::main` |
| 5 | `scorer.py::grounded_answer` |

`expects` phrases are compared against chunk and answer text by content-word
overlap on a five-character stem (`scorer.py::covers`), not exact substring
match. The corpus writes "six months after you graduate" where `expects` says
"Six months after graduation"; exact matching would score that a failure, which
would be a bug in the measurement rather than a finding.

---

## Real output

Actual text the system produced, from run 1 of
`results/run_2026-09-27_1939_before.md`.

### Criterion 1 — retrieved chunk contains the answer

Retrieval, `store.py::search`, over chunks from `chunker.py::split_documents`.
The chunk carrying the answer, and its distance, for each of the five:

```
0.432  admin_parking_permits.txt#0
       "...There is no waitlist — people who miss the window park on Verrill
       Street and walk in, which is legal but unmarked and confuses everyone."

0.340  admin_wifi_and_accounts.txt#0
       "...The account stays active for six months after you graduate, and the
       cloud drive is purged at that point without a second warning."

0.536  health_center.txt#0
       "Walk-in hours are 8am to 11am; everything after that is by appointment
       and appointments run about a week out. If something is urgent, go at 8am
       and wait rather than booking."

0.582  money_jobs.txt#0
       "Library and dining jobs post in the first week of each semester and go
       fast..."

0.446  housing_tamsin_court_laundry.txt#0
       "Best time to do laundry here is Tuesday or Wednesday morning. Sunday
       after 6pm you will wait."
```

5 of 5. Every expected fact was in a retrieved chunk, and in each case in the
chunk `scorer.py::retrieval_hit` identified — no question was carried by a
chunk that merely shared vocabulary.

### Criterion 2 — every answer names a source

Generated by `generate.py::answer_from_chunks` under `GROUNDING_INSTRUCTION`.
All five run-1 answers, unedited:

```
If you miss the permit window, you can park legally on Verrill Street and walk
in (though it is unmarked).

Source: admin_parking_permits.txt
```

```
Your student account and its cloud drive stay active for six months after you
graduate, and the cloud drive is purged at that point without a second warning
(admin_wifi_and_accounts.txt).
```

```
If something is urgent, you should go to the health centre at 8am and wait
rather than booking an appointment.

Source: health_center.txt
```

```
The best time to apply for on-campus library and dining jobs is in the first
week of each semester, as they are posted then and go fast (money_jobs.txt).
```

```
The best time to do laundry to avoid waiting is Tuesday or Wednesday morning.

Source: housing_tamsin_court_laundry.txt (also found in
housing_old_brewhouse_laundry.txt, housing_aldridge_hall_laundry.txt,
housing_fenwick_court_laundry.txt, and housing_morrow_house_laundry.txt)
```

5 of 5. Worth noting the format is not fixed — two answers use a trailing
`Source:` line and two use a parenthetical. `scorer.py::cited_sources` matches
the filename anywhere in the answer rather than a fixed citation format.

### Criterion 3 — the gate stops out-of-corpus questions

`run_eval.py::check_out_of_scope`, cutoff 0.6:

```
  refused  (best distance 0.825)  What is the capital of Mongolia?
  refused  (best distance 0.934)  How do I change the oil in a diesel engine?
  refused  (best distance 0.886)  Who won the 1994 World Cup?
  refused  (best distance 0.844)  What is the recommended dosage of ibuprofen for a headache?
  refused  (best distance 0.896)  How do I write a for loop in Rust?
  -> gate refused 5 of 5
```

5 of 5, and not narrowly. The closest out-of-scope question sits at 0.825
against a 0.6 cutoff, while the furthest in-scope question sits at 0.582. The
two groups are separated by a gap of 0.243 with no overlap, so the cutoff has
room on both sides rather than splitting a crowded middle.

### Criterion 4 — chunk completeness and boundary integrity

`scorer.py::chunk_integrity`, sampled by `scorer.py::main` — 5 chunks spaced
evenly across all 94:

```
  94 chunks total, sampling every 18th
  intact  admin_add_drop_deadline.txt#0
          starts: 'On the add/drop deadline\n\nYou can add a course through the e'
          ends:   'te says this plainly, and students find out from each other.'
  intact  course_biol_160_exams.txt#0
          starts: 'BIOL 160 Cell Biology — assessment\n\nFour unit tests and a cu'
          ends:   'ree weeks; falling behind once is very hard to recover from.'
  intact  course_math_220_exams.txt#0
          starts: 'MATH 220 Linear Algebra — assessment\n\nTwo midterms and a cum'
          ends:   'urse; the lectures make sense afterwards rather than during.'
  intact  dining_the_ridgeway_cafe.txt#0
          starts: 'The Ridgeway Café\n\nSecond-year here. Wait times: 10 to 15 mi'
          ends:   'weekdays only. Costs declining balance only, no meal swipes.'
  intact  housing_innisfree_hall_laundry.txt#0
          starts: 'Laundry in Innisfree Hall\n\nMachines take $1.75 wash, $1.75 d'
          ends:   'uesday or Wednesday morning. Sunday after 6pm you will wait.'
  -> 5 of 5
```

5 of 5. Every sampled chunk opens on a heading or a sentence start and closes
on terminal punctuation.

### Criterion 5 — factual grounding and citation accuracy

`scorer.py::grounded_answer`. Stricter than criterion 2: the answer must carry
the expected fact *and* cite a file that actually contains it, not just any of
the five chunks that came back. The cited file each run, checked against the
files that genuinely bear the fact:

```
  q1 r1  cited=['admin_parking_permits.txt']       grounded=True
  q2 r1  cited=['admin_wifi_and_accounts.txt']     grounded=True
  q3 r1  cited=['health_center.txt']               grounded=True
  q4 r1  cited=['money_jobs.txt']                  grounded=True
  q5 r1  cited=[5 housing_*_laundry.txt files]     grounded=True
```

5 of 5. This is the criterion where the retrieved set was noisiest — question 3
pulled back four dining and library chunks alongside `health_center.txt`, and
question 2 pulled back four course-workload chunks — and in both cases the
answer cited only the file that held the fact, with no material from the
unrelated four leaking in.

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     week — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | **MET** | 5/5 on all three runs against a target of 4 of 5. Not a threshold artifact: it stays 5/5 even when the matcher is tightened to demand *every* expected content word (COVERAGE 1.0). |
| 2 | Every answer names a source | **MET** | 15 of 15 answers named a file, against a target of 5 of 5 — the strictest target I set, and the only one with no slack. Scope note below. |
| 3 | Gate stops out-of-corpus questions | **MET** | All five out-of-scope questions refused, closest at 0.825 against a 0.6 cutoff. Criterion reworded — see below; verdict identical either way. |
| 4 | Chunk completeness and boundary integrity | **MET** | 5/5 sampled, and 94/94 when run over the whole corpus. Criterion reworded — see below; verdict identical either way. |
| 5 | Answer factual grounding and citation accuracy | **MET** | 5/5, but this is the close one. Question 5 passes at coverage exactly 0.60 against a 0.60 bar, and the criterion's other half wasn't measured until I went back for it. Detail below. |

### Where it was close, and where I argued against myself

**Criterion 5 is the only genuinely close call, and it passes on the target
rather than on the margin.** Question 5's answer — *"The best time to do
laundry to avoid waiting is Tuesday or Wednesday morning."* — covers 6 of the
10 content words in its `expects` phrase. That is 0.60 against a 0.60 bar: one
word the other way and it fails. Tightening `scorer.py::COVERAGE` to 0.7 drops
criterion 5 to 4 of 5 on every run.

I took the opposite verdict seriously here and it doesn't hold. 4 of 5 is still
MET, because 4 of 5 is the target I wrote in Unit 1 and the target doesn't move
now that I've seen the result. So criterion 5 is MET at *every* coverage
setting from 0.5 to 1.0 — the verdict never depended on the threshold I picked.
What the sensitivity does expose is that `expects` for question 5 is two
sentences where the question only asks for one. The answer is correct; the
yardstick was over-specified. That's a question-design problem, and under the
rule that a number you missed stays where it is, it's not grounds for editing
`expects` — I'd be editing the test to flatter the result.

**Criterion 5's verdict initially rested on something I hadn't measured.** The
criterion has two halves: the answer contains *only* facts from the retrieved
chunks, and the citation matches the file the fact came from.
`scorer.py::grounded_answer` only ever checked the second. The first was being
asserted. I added `scorer.py::unsupported_words` to screen every answer for
content words appearing in no retrieved chunk, and read everything it flagged:

```
  q1 r1: ['though']          q3 r3: ['00']
  q2 r1: ['stay']            q4 r1: ['apply', 'best', 'posted']
  q5 r1: ['avoid', 'waiting']
```

All paraphrase or reformatting, no invented facts. `00` is the one worth
naming: run 3 of question 3 wrote *"go to the health centre at 8:00 am"* where
`health_center.txt` says *"8am"*. Same fact, tidier formatting — not a
fabrication, but it is the model editing the corpus's wording, which is the
direction hallucinations start from. Had I not gone looking, criterion 5 would
have been scored MET on half its own definition.

**Criterion 2 needs its scope stated.** "Every answer the system produces"
counts 15 of 15 — but only if a gate refusal isn't an answer. Across all ten
questions including `OUT_OF_SCOPE`, output naming a source is 15 of 30. I score
refusals as out of scope for this criterion because `gate.REFUSAL` is a fixed
string in `gate.py`, returned before any model call — the system never
*produced* it in the sense the criterion means. That reading is defensible but
it is a reading, and someone coming to the criterion cold could land the other
way. Worth stating rather than leaving implicit.

**Criterion 1 is the one verdict I couldn't argue against.** Every expected
fact appeared in a retrieved chunk, in the specific chunk the scorer named,
under every matcher setting I tried. The honest caveat isn't about the
measurement, it's about the difficulty: all five `expects` phrases turned out
to be near-verbatim from a single document, so retrieval was never asked to do
anything hard. Criterion 1 is MET and the test behind it is easy — those are
both true and the second one is the more useful fact.

### Revisions

Two criteria are reworded in [`criteria.md`](criteria.md), originals left in
place above each revision. **Neither changes a verdict** — both were 5/5 before
and after. Both are measurement defects, not missed numbers:

- **Criterion 3** said "4 of 5 **tries**". Retrieval is deterministic, so five
  tries of one question can only come out 5 of 5 or 0 of 5, never 4. I have
  five *questions*, not five tries, and the original justified its slack as
  absorbing "embedding noise" that has no run-to-run variation to produce.
- **Criterion 4** asked for chunks that "read as a complete, self-contained
  thought" *and* don't cut mid-sentence. `scorer.py::chunk_integrity` only
  covers the second. Given *"It backs up on Sunday evenings for that reason."*
  it returns intact — nothing is severed, yet it plainly isn't self-contained.
  The dropped half was a judgment I couldn't count on making the same way
  twice.

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

**I missed nothing. Five criteria, five MET, three runs each.**

That is the result that should be read with the most suspicion, so the rest of
this section is spent arguing that my targets were soft rather than that my
system is good. One of them turns out to be soft enough that the criterion is
measuring the wrong question entirely.

### The targets were set low — here is the margin on each

| # | Target | Measured | Headroom |
|---|---|---|---|
| 1 | 4 of 5 | 5/5, and still 5/5 when the matcher demands *every* expected word | Large. Never tested a hard retrieval. |
| 2 | 5 of 5 | 15/15 | Moderate, but `GROUNDING_INSTRUCTION` explicitly orders a citation — this tests the prompt, not the pipeline. |
| 3 | 4 of 5 | 5/5 | **Illusory — see below.** |
| 4 | 4 of 5 sampled | 94/94 across the entire corpus | Total. The criterion cannot fail on this corpus. |
| 5 | 4 of 5 | 5/5, but question 5 lands on 0.60 against a 0.60 bar | Thin. The only criterion with a cell that nearly went the other way. |

Criteria 1 and 4 are the clearest cases of a safe target. Criterion 4 samples
five chunks out of 94 and asks that four pass a check that all 94 pass —
there is no sample of five that could have failed it. Criterion 1 is safe for a
different reason: every `expects` phrase I wrote in Unit 1 turned out to be
near-verbatim from one document, so retrieval only ever had to match text
against itself.

### Criterion 3 is not just soft — it is measuring the wrong thing

**Stage: embedding. Mechanism: distance measures question *shape*, not topic.**

My five `OUT_OF_SCOPE` questions come from a different world entirely, and they
sit at distances 0.825–0.934 against a 0.6 cutoff. Nothing about that is close.
So I wrote eight questions that a real student would actually ask this system —
on-topic for a campus, absent from these documents — and put them through the
same gate (`questions.py::NEAR_MISS`, measured with `store.py::search` and
`gate.py::check`):

```
  0.461  LET THROUGH  What are the opening hours for the campus gym?
  0.575  LET THROUGH  When is the spring career fair?
  0.612  refused      Can I call campus security for a walk home at night?
  0.646  refused      How do I set up a tuition payment plan?
  0.647  refused      Is there somewhere to store my bike over the winter?
  0.657  refused      How do I appeal a parking ticket?
  0.686  refused      How do I register with disability services for exam accommodations?
  0.747  refused      Where do I pick up a package that was mailed to me?
  -> refused 6 of 8
```

6 of 8 is 75%. Against the 80% my criterion asks for, **that is a MISS** — and
it is the same gate, the same cutoff and the same code that scored 5 of 5 an
hour earlier. The only thing that changed is that the questions got realistic.

The three distance bands say why:

```
  in-scope     0.340 .. 0.582     <- must pass
  near-miss    0.461 .. 0.747     <- must be refused, OVERLAPS in-scope by 0.121
  original oos 0.825 .. 0.934     <- the easy set I actually tested against
```

The mechanism, question by question. The gym question's nearest chunk is
`transit_shuttle.txt`, whose text is *"Runs a loop every 20 minutes from 7am to
11pm on weekdays"*. Gym and shuttle share no topic at all; what they share is
being a **"when is this campus thing open"** question, and the embedding scores
that structural resemblance at 0.461 — closer than three of my five real
questions. The career-fair question lands on `orientation_what_matters.txt`,
which contains the phrase *"The club fair is..."* — overlap on the literal word
"fair" plus general campus-event vocabulary.

**The pattern: both leaks are schedule-and-event questions, and both match on
question shape or shared campus vocabulary rather than subject matter.** That
is one failure, not two. It is also the failure a distance threshold is
structurally unable to fix, because "campus topic we happen to cover" and
"campus topic we don't" are not far apart in embedding space — they are the
same kind of sentence about the same institution.

**No cutoff rescues it.** Sweeping every threshold from 0.40 to 0.78:

```
   cutoff | in-scope kept | near-miss refused | total correct
     0.46 |           3/5 |               8/8 | 11/13   <- best, but loses 2 real questions
     0.54 |           4/5 |               7/8 | 11/13
     0.60 |           5/5 |               6/8 | 11/13   <- current setting
     0.66 |           5/5 |               2/8 |  7/13
```

0.6 is already tied for the best operating point available. Refusing the gym
question needs a cutoff under 0.461, which would also refuse four of my five
genuine questions. The bands overlap, so the trade is forced. **This is not a
threshold that was tuned wrong; it is a threshold doing the only thing it can.**

### Why this didn't reach a user, and why that isn't reassuring

Both leaked questions still came out correct, because `generate.py`'s
`GROUNDING_INSTRUCTION` caught what the gate missed:

```
Q: What are the opening hours for the campus gym?    (gate passed it at 0.461)
   "I do not have enough information to answer your question."

Q: When is the spring career fair?                   (gate passed it at 0.575)
   "I don't have enough information to answer your question, as the documents
    do not mention a spring career fair."
```

So user-visible behaviour is fine and the two-layer design is doing its job.
Three reasons that does not repair criterion 3. The gate's stated purpose in
`gate.py` is that *"a question the gate refuses never reaches the model"* — both
of these reached the model and cost an API call each. Layer two is a model, so
it holds probabilistically rather than always; `gate.py`'s own docstring makes
exactly this argument, that asking nicely means *"it will sometimes ignore you
and write something confident and wrong"*. And criterion 3 is written about the
gate specifically, so a rescue downstream is not the criterion passing.

**Criterion 3 as I tested it: MET. Criterion 3 as it would be tested with
questions anyone would actually ask: MISSED at the embedding stage, masked by
the generation stage.**

### What I would tighten, and to what

**Primary — criterion 3.** Replace the five `OUT_OF_SCOPE` questions with the
eight in `NEAR_MISS`, and add the cost clause the current wording leaves
implicit:

> The relevance gate refuses at least 7 of 8 campus-adjacent questions the
> corpus does not cover, and no refused question reaches the model.

Today that reads 6 of 8 — a real miss, with a diagnosed cause, which is what a
criterion is for. Measuring it needs no model calls.

**Criterion 4:** the sampled-five framing can't fail, so drop the sample —
*"every chunk in the corpus begins at a sentence or heading boundary and ends
on terminal punctuation"*, currently 94/94. A criterion that only holds at 100%
is one a future chunking change can actually break.

**Criterion 1:** require the answer to be retrieved for questions that share no
vocabulary with the source document, rather than for `expects` phrases lifted
from it. That is the harder test I thought I had written and didn't.

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
