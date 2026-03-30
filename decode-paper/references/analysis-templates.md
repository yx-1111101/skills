# Analysis Templates

Use these templates selectively. Do not force every section into every answer.

## Quick Explain

- Thesis: What is the central claim in one sentence?
- Context: What problem does the paper try to solve, and why is it hard?
- Mechanism: What is the core trick, architecture, or insight?
- Evidence: What experiments or analyses support the claim?
- Caveat: What is the biggest reason to be cautious?

## Structured Reading Note

- Citation: Title, venue, year, authors when available.
- Problem: What gap or limitation motivates the work?
- Contribution: What does the paper add beyond prior work?
- Method: What are the main components and how do they interact?
- Data and setup: Which datasets, tasks, or evaluation settings matter most?
- Results: Which numbers or qualitative findings actually matter?
- Limits: What assumptions, blind spots, or missing ablations stand out?
- Takeaway: When is this paper useful in practice?

## Critique Checklist

- Novelty: Is the contribution actually new, or mainly a recombination?
- Method: Are important implementation or modeling choices underspecified?
- Evidence: Are baselines strong, fair, and up to date for the paper's setting?
- Causality: Do the experiments support the interpretation, or only correlation?
- Robustness: Are failure cases, sensitivity analyses, or ablations missing?
- Scope: Are the claims broader than the tested domain?
- Cost: Are compute, latency, data, or annotation requirements practical?

## Comparison Template

- Shared problem: What common task are the papers addressing?
- Assumptions: What does each paper assume about data, labels, or hardware?
- Method contrast: What are the most important conceptual differences?
- Evidence contrast: Which paper has stronger empirical support, and why?
- Practical choice: Under what conditions would you pick each one?

## Implementation Template

- Required components: Model pieces, training stages, loss terms, data pipeline.
- Explicit details: Hyperparameters or procedures directly stated in the paper.
- Missing details: Choices that will need reproduction judgment.
- Risks: Likely failure points when implementing from scratch.
- Minimal plan: Smallest experiment that can validate the core idea.
