---
name: analyze-ai-product
description: Analyze AI products, AI agents, AI features, copilots, model-driven workflows, and AI startups from product, strategy, user-value, UX, workflow, economics, and moat perspectives. Use when asked to 拆解 AI 产品, analyze an AI app, review a product idea, assess PMF, compare competitors, critique onboarding or retention, evaluate pricing, estimate defensibility, write an investment-style memo, or turn screenshots, landing pages, demos, feature lists, and user feedback into a structured product judgment.
---

# Analyze Ai Product

Enable product analysis that treats AI products as systems, not just feature lists. Focus on user job, workflow closure, model capability fit, trust, economics, distribution, and defensibility.

## Workflow

1. Identify the artifact and evidence level.
- Determine whether the input is a landing page, screenshots, app walkthrough, pricing page, feature list, user reviews, founder claim, or firsthand product usage.
- State what is directly observed versus inferred. If the source is thin, narrow the confidence of the conclusion.

2. Define the product in one line.
- Explain what the product actually does, for whom, and in what moment of work.
- Avoid repeating marketing copy. Translate positioning into a real user job.

3. Reconstruct the user workflow.
- Map the entry point, input, model interaction, output, editing loop, sharing or export path, and repeat loop.
- Identify where value is created, where friction appears, and whether the workflow reaches a complete job-to-be-done.

4. Analyze the AI-specific layer.
- Ask whether AI is the product, an accelerator inside the workflow, or a thin wrapper around a general model.
- Examine model dependence, latency tolerance, reliability requirements, evaluation difficulty, human-in-the-loop design, and failure recovery.
- Distinguish demo magic from dependable production behavior.

5. Analyze product strength.
- Evaluate target user clarity, urgency of pain, onboarding speed, habit loop, switching cost, collaboration surface, pricing logic, distribution wedge, and defensibility.
- Separate novelty, usefulness, and willingness to pay.

6. End with an opinionated judgment.
- State why the product works or does not.
- Highlight the single strongest lever and the single biggest weakness.
- Suggest what to test, improve, or compare next.

## AI Product Lens

When analyzing an AI product, always check these questions:

- Is the user problem painful enough to justify imperfect AI output?
- Does the workflow save time end to end, or only in one flashy step?
- Is the core value proprietary workflow design, proprietary data, distribution, brand, or merely model access?
- What happens when the model is wrong, slow, expensive, or inconsistent?
- Does the product improve with usage through feedback loops, memory, customization, or team data?
- Could a better prompt in a general-purpose tool replace most of the value?

## Default Output Shape

Use this order unless the user asks for a different format:

1. Product one-liner.
2. Target user and core job.
3. User workflow and where AI adds value.
4. Why this product may win.
5. Main weaknesses or risks.
6. Competitive position and defensibility.
7. Bottom-line verdict.

For deeper analysis, add pricing, retention, GTM, and roadmap implications.

## Useful Modes

- Quick teardown: explain what it is, who it is for, and the main verdict in under 250 words.
- Competitor comparison: compare user segment, workflow, moat, UX, pricing, and likely winner.
- PM review: focus on onboarding, habit loop, retention, and feature prioritization.
- Founder or investor memo: emphasize market pull, economics, defensibility, and execution risk.
- Strategy critique: focus on positioning, wedge, platform risk, and expansion path.
- Feature diagnosis: analyze one feature inside a larger product instead of the whole company.

## Quality Bar

- Never confuse observed facts with inference. Label assumptions clearly.
- Do not praise surface polish if the workflow still depends on heavy user cleanup.
- Treat AI accuracy, trust, latency, and cost as first-order product variables, not technical footnotes.
- Prefer product judgment over summary. The answer should conclude something.
- Avoid generic SWOT lists unless the user explicitly asks for SWOT.
- If there is no direct evidence of retention or monetization, say so rather than inventing confidence.

## Common Failure Modes To Catch

- Wrapper risk: the product adds little beyond a general model and a prompt.
- Broken loop: the output is impressive but not usable inside the user's real workflow.
- Cost trap: token or human review costs grow faster than revenue.
- Trust gap: the product is useful only when perfect, but the model is not perfect.
- Narrow wow effect: onboarding is exciting, but repeat usage is weak.
- Weak moat: no data advantage, no workflow lock-in, and no distribution edge.

## Incomplete Inputs

- If the user provides only a homepage, avoid overclaiming retention, economics, or model quality.
- If the user provides screenshots, infer flow carefully from UI states and label uncertainty.
- If the user provides user feedback or reviews, separate signal about value from noise about isolated bugs.
- If the user asks for investment judgment, be clear what cannot be known without metrics.

## Reference File

Read [references/analysis-templates.md](references/analysis-templates.md) when a reusable memo structure, comparison table, or diligence checklist would help. Keep the final answer tailored to the specific product and stage.
