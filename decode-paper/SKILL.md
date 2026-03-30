---
name: decode-paper
description: Interpret, summarize, and critique academic papers, arXiv preprints, journal articles, conference papers, abstracts, and research PDFs. Use when asked to 解读论文, explain a paper, summarize a paper, translate research ideas into plain language, extract contributions, compare methods, assess experiments, identify limitations, or turn a paper into reading notes, review bullets, presentation material, or implementation guidance.
---

# Decode Paper

Enable careful, high-signal paper reading instead of generic summary. Treat the job as: understand the claim, reconstruct the reasoning, test the evidence, and explain the result at the user's level.

## Workflow

1. Identify the source and evidence level.
- Determine whether the user provided a full paper, title/link, abstract, figure, table, or only a claim from memory.
- State the evidence level explicitly. If only the abstract or excerpts are available, say the interpretation is partial and avoid pretending to know missing sections.

2. Calibrate for audience and task.
- Infer whether the user wants a quick overview, beginner explanation, section-by-section walkthrough, critical review, comparison, or implementation takeaways.
- Default to plain language first, then add technical detail.
- If replying in Chinese, keep important technical terms in English on first mention.

3. Reconstruct the paper skeleton.
- Extract: problem, motivation, key idea, method, data or setup, main results, claimed contributions, assumptions, and limitations.
- Distinguish what the paper claims from what the experiments actually support.

4. Explain before critiquing.
- Start with a one-paragraph explanation of what the paper is really trying to do.
- Translate jargon, equations, or architecture choices into intuition when that improves understanding.
- Define unfamiliar terms once, then use the technical term consistently.

5. Critique with discipline.
- Check novelty against the framing in the paper, not against vague expectations.
- Examine methodology, dataset choice, baseline quality, ablations, robustness, external validity, compute or data assumptions, and possible confounders.
- Separate missing detail, weak evidence, and actual flaws.

6. End with actionable takeaways.
- Summarize when to trust the paper, when to be cautious, and what to read, test, or compare next.
- Offer follow-up formats such as study notes, slide outline, rebuttal bullets, implementation plan, or comparison table.

## Default Output Shape

Use this order unless the user asks for something different:

1. One-sentence thesis.
2. Why the paper matters.
3. How the method works.
4. What evidence the paper provides.
5. Main strengths.
6. Main limitations or open questions.
7. Bottom-line verdict in plain language.

Compress to fewer sections for casual asks. Expand to section-by-section analysis for deep reads.

## Quality Bar

- Never fabricate equations, metrics, datasets, baselines, or section details that are not visible in the source.
- Mark inference explicitly with phrases like `likely`, `the paper appears to`, or `based on the abstract`.
- Prefer paper-specific explanation over stock machine-learning boilerplate.
- Quote paper terminology accurately, but explain it in simpler language.
- Be especially careful with causal claims, SOTA claims, and benchmark deltas.
- If the paper is outside your confident domain, keep claims narrow and uncertainty visible.

## Incomplete Or Messy Inputs

- If the user shares only a title or link, obtain the paper or abstract first when tools allow.
- If the PDF is scanned, incomplete, or inaccessible, fall back to whatever reliable text is available and clearly label the gap.
- If the user only shares figures or tables, explain what each visual is trying to demonstrate before interpreting the values.
- If the user wants implementation advice from a paper, separate directly specified details from guessed engineering choices.

## Useful Modes

- Quick explain: give the thesis, mechanism, evidence, and caveat in under 200 words.
- Beginner mode: reduce jargon, add intuition, and explain why each component exists.
- Reading notes: produce compact, reusable study notes.
- Review mode: emphasize novelty, evidence quality, limitations, and unanswered questions.
- Comparison mode: compare problem setting, assumptions, methods, and empirical support across papers.
- Implementation mode: extract steps, components, hyperparameters, missing details, and likely reproduction risks.

## Reference File

Read [references/analysis-templates.md](references/analysis-templates.md) only when a reusable response structure or critique checklist would help. Keep the main answer tailored to the specific paper instead of mechanically filling every section.
