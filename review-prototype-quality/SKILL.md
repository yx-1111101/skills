---
name: review-prototype-quality
description: Review, evaluate, and critique Figma prototypes, wireframes, mockups, and UX flows. Use when asked to 评价原型质量, review a prototype, give design feedback, audit a UI or UX design, check prototype completeness, assess interaction design, evaluate whether a prototype is ready for user testing or developer handoff, or critique screens, user flows, navigation design, visual hierarchy, content coverage, and consistency.
---

# Review Prototype Quality

Evaluate prototypes with the discipline of an experienced design reviewer: understand the design intent, reconstruct the user flow, test the logic of each interaction, and deliver a verdict that is actionable rather than generic.

## What Counts as Prototype Quality

Quality is not visual polish. A high-quality prototype:

- Accurately communicates intent to users, testers, and engineers.
- Covers the flows that matter without unnecessary decoration.
- Makes interaction logic unambiguous.
- Exposes real design decisions rather than deferring them.
- Reaches a testable or shippable level of completeness for its stated purpose.

## Workflow

1. Identify the prototype type and stated purpose.
   - Determine whether this is a low-fidelity wireframe, high-fidelity mockup, clickable prototype, or design spec for handoff.
   - Establish the declared purpose: concept validation, usability testing, stakeholder review, or developer handoff.
   - Calibrate expectations to purpose. A wireframe should not be judged on pixel precision; a handoff file should.

2. Establish evidence level.
   - Note what you can actually observe: screenshots provided, URL accessed, partial flow, or user description.
   - Flag where your observations are incomplete and avoid inferring unobserved screens.

3. Reconstruct the user flow.
   - Identify the entry point, key tasks, branching paths, success states, error states, and exit points.
   - Map which flows are present and which appear absent.

4. Evaluate across the core quality dimensions.
   - Apply the six dimensions below. Not every dimension applies to every review; prioritize by prototype purpose.

5. Summarize findings with severity.
   - Group findings as: critical (blocks testing or use), significant (impairs understanding or usability), and minor (style, polish, or preference).
   - Lead with the most actionable issues.

6. Give a clear verdict.
   - State whether the prototype is ready for its declared purpose.
   - If it is not ready, specify what is required to reach that threshold.

## Six Core Quality Dimensions

### 1. Flow Completeness
- Are the primary user tasks covered end to end?
- Are key branching paths present (success, error, empty state, edge case)?
- Are there dead-end screens, broken links, or missing transitions?
- Is it clear how users enter and exit each major flow?

### 2. Interaction Clarity
- Are interactive elements visually distinct from static ones?
- Do affordances match expected behavior (tap targets, buttons, links, inputs)?
- Is feedback present for key actions (loading, confirmation, error)?
- Is the back/undo/cancel path defined wherever the user might need it?

### 3. Information Hierarchy and Layout
- Does the visual weight match content priority?
- Is the primary action obvious on each screen?
- Is spacing, grouping, and alignment used consistently to signal structure?
- Are there screens where the user's eye has no clear starting point?

### 4. Content Coverage
- Are real or representative content samples used, or only placeholder text?
- Are empty states, zero-data states, and loading states designed?
- Is error copy specific enough to be useful, or is it generic Lorem Ipsum-level?
- Are truncation, overflow, and long-content cases handled?

### 5. Consistency and System Coherence
- Are components, patterns, and vocabulary used consistently across screens?
- Do similar actions look and behave the same way throughout?
- Are there visual outliers that suggest missing system decisions?
- If the prototype references a design system, does it follow it?

### 6. Handoff or Test Readiness
- For user testing: is the prototype clickable and realistic enough for valid feedback?
- For developer handoff: are dimensions, spacing, colors, and component behavior specified?
- Are annotations present where ambiguity exists?
- Is there a clear map of what is in scope and what is intentionally left out?

## Default Output Shape

1. Prototype summary: type, declared purpose, and observable scope.
2. Flow map: what flows are present and what is missing.
3. Findings by dimension: critical, significant, and minor issues per applicable dimension.
4. Verdict: ready or not ready for declared purpose, and what is required to close the gap.

Compress to fewer sections for quick reviews. Expand to screen-by-screen annotation for detailed handoff audits.

## Useful Modes

- Quick audit: overall verdict, top three critical issues, and one recommendation per dimension.
- Flow review: focus on completeness, branching logic, and entry/exit clarity.
- Interaction review: focus on affordances, feedback states, and micro-interaction coherence.
- Handoff audit: focus on specification completeness, annotation quality, and component alignment.
- Usability test readiness: assess whether the prototype is realistic enough to generate valid user feedback.
- Consistency check: identify visual and behavioral inconsistencies across screens.

## Writing Style

- Lead with the verdict on the specific prototype, not generic UX advice.
- Separate observed fact from inference; label gaps explicitly.
- Write findings as specific and locatable as possible: name the screen, section, or element.
- Avoid generic praise. If polish is noted, say what specifically works and why.
- Do not recommend adding features or scope unless the prototype's stated purpose requires it.

## Quality Bar

- Do not fabricate screens or interactions not visible in the source.
- Do not apply handoff-level criteria to a wireframe unless handoff readiness is the declared purpose.
- Distinguish a prototype's deliberate simplification from an actual gap.
- Never rate visual style as a proxy for interaction quality.
- Separate personal preference from objective clarity and completeness issues.

## Common Failure Modes to Catch

- Happy-path only: only the successful case is designed; errors and edge cases are absent.
- Orphaned screens: screens exist but cannot be reached from the main flow.
- Ambiguous affordances: it is unclear what is interactive and what is static.
- Placeholder overload: real content is needed to evaluate layout decisions but is absent.
- Missing system states: loading, error, empty, and disabled states are undesigned.
- Premature polish: high visual fidelity applied before interaction logic is resolved.
- Annotation gap: complex behavior is implied but not specified, creating handoff risk.

## Incomplete Inputs

- If only a Figma URL is provided and the file is not accessible, ask the user for screenshots or a description of the key screens.
- If only a subset of screens is visible, scope the review to what is observable and flag the gap.
- If the prototype purpose is not stated, infer it from fidelity and ask for confirmation before evaluating readiness.
- If the user shares a recording or walkthrough, note the flows observed and flag anything that was not demonstrated.

## Reference File

Read [references/analysis-templates.md](references/analysis-templates.md) when a structured checklist or severity matrix would help organize the findings. Adapt to the specific prototype's fidelity and purpose rather than applying every template section mechanically.
