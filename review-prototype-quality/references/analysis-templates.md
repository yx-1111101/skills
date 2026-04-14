# Analysis Templates

Use these templates selectively. Adapt to the prototype's fidelity and declared purpose. Do not force every section into every review.

## Quick Audit

- Type: What kind of prototype is this (wireframe, mockup, clickable prototype, handoff spec)?
- Purpose: What is the prototype meant to accomplish (concept validation, usability test, dev handoff)?
- Top issue: What is the single most critical problem?
- Verdict: Ready or not ready for its stated purpose?
- Required to close the gap: What specifically must change?

## Flow Completeness Checklist

- [ ] Entry point is defined and reachable.
- [ ] Primary user task is covered end to end.
- [ ] At least one error or failure path is designed.
- [ ] Empty and zero-data states are present where applicable.
- [ ] Exit paths (cancel, back, close) are defined.
- [ ] No orphaned screens unreachable from the main flow.
- [ ] No dead-end screens with no forward path.

## Interaction Clarity Checklist

- [ ] Interactive elements are visually distinct from static content.
- [ ] Tap targets and click areas are appropriately sized and labeled.
- [ ] System feedback is present for key actions (loading, success, error).
- [ ] Undo, back, and cancel paths are available where destructive actions occur.
- [ ] Form validation and input error states are specified.
- [ ] Transitions between screens communicate directionality and context.

## Information Hierarchy Checklist

- [ ] Primary action is immediately apparent on each screen.
- [ ] Visual weight matches content priority.
- [ ] Spacing and grouping consistently signal structure.
- [ ] Every screen has a clear starting point for the eye.
- [ ] Secondary and tertiary content is visually subordinate.

## Content Coverage Checklist

- [ ] Real or representative content is used in key screens.
- [ ] Long content, truncation, and overflow cases are handled.
- [ ] Empty states are designed with a clear message and next action.
- [ ] Error messages are specific and actionable, not generic.
- [ ] Loading states are shown for asynchronous operations.

## Consistency Checklist

- [ ] Components and patterns are reused across equivalent contexts.
- [ ] Vocabulary and labels are consistent across screens.
- [ ] Similar actions look and behave the same way throughout.
- [ ] Color, typography, and spacing follow a visible system.
- [ ] No visual outliers that suggest an unresolved design decision.

## Severity Matrix

| Severity    | Definition                                                                 | Action Required                          |
|-------------|----------------------------------------------------------------------------|------------------------------------------|
| Critical    | Blocks the prototype from being used for its stated purpose.               | Must fix before proceeding.              |
| Significant | Impairs understanding, usability, or testability in a meaningful way.      | Should fix before user testing or handoff. |
| Minor       | Polish issue, style preference, or non-blocking inconsistency.             | Address in a later iteration.            |

## Handoff Readiness Checklist

- [ ] Dimensions and spacing are specified or accessible in the design tool.
- [ ] Color values and typography styles are named and consistent.
- [ ] Component states (default, hover, active, disabled, error) are all present.
- [ ] Annotations explain behavior that cannot be inferred from visuals alone.
- [ ] Prototype scope is documented: what is in and what is intentionally out.
- [ ] Assets and icons are exportable at correct resolutions.
- [ ] Motion or animation intent is described where relevant.

## Usability Test Readiness Checklist

- [ ] The prototype is clickable and covers the tasks to be tested.
- [ ] Fidelity is sufficient for participants to engage without confusion.
- [ ] Placeholder content does not distract or mislead testers.
- [ ] The prototype can be reset to a starting state between sessions.
- [ ] At least one realistic failure scenario is accessible.
- [ ] Test facilitator can narrate what is intentionally out of scope.
