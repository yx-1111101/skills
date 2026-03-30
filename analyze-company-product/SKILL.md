---
name: analyze-company-product
description: Analyze companies, products, startups, apps, software, platforms, consumer brands, enterprise tools, and AI or non-AI businesses from product, strategy, positioning, workflow, economics, financing, team background, and moat perspectives. Use when asked to 拆解公司, 拆解产品, analyze a company or product, review a startup idea, assess PMF, compare competitors, critique onboarding or retention, evaluate pricing, estimate defensibility, summarize funding history, profile the founding team or org structure, write an investment-style memo, or turn screenshots, landing pages, demos, feature lists, company information, and user feedback into a structured judgment.
---

# Analyze Company Product

Enable general company and product analysis rather than a feature checklist. Use structured teardown to identify success factors, product advantages, technical or operational advantages, structural weaknesses, market positioning, financing signals, and future prospects across different kinds of companies and products.

## Minimum Coverage

When evidence is available, the analysis should include at least these six parts:

1. Team background and organization.
- Identify founders, key executives, notable prior experience, and any visible product or research organization structure.
- If the org chart is not public, infer carefully from hiring, public bios, product scope, and company stage, and label that as inference.

2. Product philosophy, positioning, and design principles.
- Explain the product's core belief about how it should help users or win in the market.
- Summarize target market, target user, product positioning, and recurring design choices such as speed, autonomy, trust, human control, or collaboration.

3. Financing history.
- List funding rounds, investors, timing, and any available valuation or capital intensity signal.
- Explain what the financing suggests about market narrative, investor conviction, and expected growth pressure.

4. Commercial model and product matrix.
- Explain how the company makes money: subscription, seat-based pricing, usage-based pricing, enterprise contracts, services, or hybrid.
- Map the product matrix: consumer, prosumer, enterprise, API, agent, platform, workflow modules, or adjacent tools.

5. Core technical advantage and leadership.
- Identify where technical or operating advantage may come from: technology, product architecture, workflow design, proprietary data, distribution system, supply chain, integrations, infrastructure, brand, or execution.
- Separate true capability lead from packaging or marketing strength.

6. Overall judgment.
- Analyze the product's strengths, why it was able to get funded, what its success factors are, what is reusable as a lesson, and what its future outlook looks like.
- Keep this section objective: include upside, downside, execution risk, and platform or market risk.

## Workflow

1. Identify the artifact and evidence level.
- Determine whether the input is a landing page, screenshots, app walkthrough, pricing page, feature list, user reviews, founder claim, or firsthand product usage.
- State what is directly observed versus inferred. If the source is thin, narrow the confidence of the conclusion.

2. Define the product in one line.
- Explain what the product actually does, for whom, and in what moment of work.
- Avoid repeating marketing copy. Translate positioning into a real user job.

3. Reconstruct the user workflow.
- Map the entry point, input, core interaction, output, editing loop, sharing or export path, and repeat loop.
- Identify where value is created, where friction appears, and whether the workflow reaches a complete job-to-be-done.

4. Analyze the core capability layer.
- Identify what capability actually powers the product: AI, software workflow, marketplace dynamics, service operations, data advantage, hardware integration, brand, or channel control.
- If AI is involved, ask whether it is the product, an accelerator inside the workflow, or a thin wrapper around a general model.
- Distinguish surface presentation from dependable underlying capability.

5. Analyze product strength.
- Evaluate target user clarity, urgency of pain, onboarding speed, habit loop, switching cost, collaboration surface, pricing logic, distribution wedge, and defensibility.
- Separate novelty, usefulness, and willingness to pay.

6. Add company and financing context when relevant.
- Gather team background, funding history, market timing, and org clues.
- Use these signals to explain not just what the product is, but why the company may have attracted capital and attention.

7. End with an opinionated judgment.
- State why the product works or does not.
- Highlight the single strongest lever and the single biggest weakness.
- Suggest what to test, improve, or compare next.

## Core Analysis Lens

When analyzing a company or product, always check these questions:

- Is the user problem painful enough to create real demand?
- Does the workflow save time end to end, or only in one flashy step?
- Is the core value driven by technology, workflow, data, supply, brand, distribution, or cost structure?
- What breaks the experience when the product underperforms, scales poorly, or faces competition?
- Does the offering improve with usage through feedback loops, customization, network effects, or operational learning?
- Can the product be easily substituted by a simpler alternative?

## Default Output Shape

Use this order unless the user asks for a different format:

1. Product one-liner.
2. Team background and organizational context.
3. Product philosophy, market positioning, and design principles.
4. Business model and product matrix.
5. User workflow and where the core value is created.
6. Financing history and what it signals.
7. Technical advantage and competitive position.
8. Main strengths, key reasons it won funding, reusable lessons, and future outlook.

For deeper analysis, add retention, GTM, roadmap implications, and downside scenarios.

## Useful Modes

- Quick teardown: explain what it is, who it is for, and the main verdict in under 250 words.
- Competitor comparison: compare user segment, workflow, moat, UX, pricing, and likely winner.
- PM review: focus on onboarding, habit loop, retention, and feature prioritization.
- Founder or investor memo: emphasize market pull, economics, defensibility, and execution risk.
- Company profile: emphasize founding team, org capability, capital history, and strategic direction.
- AI-specific review: if the company is AI-native, add model fit, trust, latency, and wrapper risk.
- Strategy critique: focus on positioning, wedge, platform risk, and expansion path.
- Feature diagnosis: analyze one feature inside a larger product instead of the whole company.

## Quality Bar

- Never confuse observed facts with inference. Label assumptions clearly.
- Do not fake organizational structure or financing details. If public information is missing, say the section is evidence-constrained.
- Do not praise surface polish if the workflow still depends on heavy user cleanup.
- Treat the true source of advantage as a first-order variable, not a footnote.
- Prefer product judgment over summary. The answer should conclude something.
- Avoid generic SWOT lists unless the user explicitly asks for SWOT.
- If there is no direct evidence of retention or monetization, say so rather than inventing confidence.

## Common Failure Modes To Catch

- Thin-value risk: the product adds little beyond a generic alternative.
- Broken loop: the output is impressive but not usable inside the user's real workflow.
- Cost trap: delivery, service, infrastructure, or support costs grow faster than revenue.
- Trust gap: the product is useful only when it performs near-perfectly, but real-world delivery is inconsistent.
- Narrow wow effect: onboarding is exciting, but repeat usage is weak.
- Weak moat: no data advantage, no workflow lock-in, and no distribution edge.

## Incomplete Inputs

- If the user provides only a homepage, avoid overclaiming retention, economics, or underlying capability quality.
- If the user asks for team background, org structure, or funding details, obtain them from reliable public sources when tools allow.
- If the user provides screenshots, infer flow carefully from UI states and label uncertainty.
- If the user provides user feedback or reviews, separate signal about value from noise about isolated bugs.
- If the user asks for investment judgment, be clear what cannot be known without metrics.

## Reference File

Read [references/analysis-templates.md](references/analysis-templates.md) when a reusable memo structure, comparison table, or diligence checklist would help. Keep the final answer tailored to the specific product and stage.
