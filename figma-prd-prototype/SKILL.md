---
name: figma-prd-prototype
description: Generate a full multi-frame Figma prototype from a PRD (Notion/Markdown) for web apps. Covers PRD ingestion, frame planning, multi-column shell reuse, team component library integration, and iterative state frames (default/empty/loading/failure/success). Activate when the user shares a PRD URL plus a Figma target and asks to 生成原型 / 补页面 / 做一版 / build a prototype from this spec.
---

# Figma PRD → Prototype

End-to-end workflow for turning a PRD into a full set of Figma frames: information architecture → page states → component reuse → cross-frame consistency.

## Prerequisites

Before any `use_figma` call, load upstream skills (API rules, screen building, error recovery):

1. figma-use
2. figma-generate-design (when building screens from scratch)
3. figma-style-migration (sibling skill — reuse its pitfalls.md and style-catalog.md)

Always pass `skillNames: "figma-prd-prototype"` on `use_figma` calls.

## Decision Tree

```
User shares PRD + Figma target
  │
  ├─ PRD lists 3+ pages with multiple states ─► Plan frame matrix first, build in rows
  │    (most common case)
  │
  ├─ PRD is a single-page feature spec ──────► Build state variants side-by-side
  │    (empty / default / loading / failure / success)
  │
  └─ PRD is a full app (>10 pages) ──────────► Stage in versions (v1..vN)
       (IA first, generate shell, fill iteratively)
```

## Workflow

### 1. Ingest the PRD

- Fetch the PRD with the relevant MCP (Notion MCP preferred; fall back to WebFetch).
- Extract per page: **goal**, **entry conditions**, **layout areas**, **states** (core/empty/loading/fail/success), **acceptance rules**.
- Identify global context rules (current Gateway / tenant / workspace) — these become fixed UI elements that survive across every frame.

### 2. Plan the frame matrix

Before touching Figma, list the frames in a row. Example matrix:

| # | Module | Frame | x | y |
|---|---|---|---|---|
| 1 | Gateway 管理 | P1 空状态 | 0 | 2500 |
| 2 | Gateway 管理 | P2 列表 | 1540 | 2500 |
| 3 | Gateway 管理 | P2 管理侧面板展开 | 3080 | 2500 |
| 4 | Gateway 管理 | 重命名模态 | 4620 | 2500 |

Rules:
- Horizontal spacing = 1440 (canvas width) + 100 gap = **1540**
- Rows separated by 1500+ vertical space, one row per version (v1 at y=1200, v2 at y=2500, v3 at y=4000).
- Keep old versions alive for diffing until the user signs off on the new one.

### 3. Propose layout before building

For non-obvious structures (3-col vs 4-col, modal vs full-page, tabs vs sub-nav), write a markdown proposal with column widths and section mapping first. Wait for confirmation before executing `use_figma`. Skipping this costs a full rebuild.

### 4. Build shell first, content after

1. **Shell chunk**: app nav + sub nav + content frame + breadcrumb strip. Return frame + content IDs.
2. **Content chunks**: each card/section in its own `use_figma` call, reading back the parent frame via `getNodeByIdAsync`.
3. **Overlays last**: modals / hover cards / popovers appended at the very end so z-order (= child index) puts them on top.

### 5. Enforce cross-frame consistency

- Side nav / sub nav helpers (`appNav(f)`, `settingsNav(f, activeKey)`) live inline in every chunk — each chunk re-defines them because sandboxes are fresh.
- Keep the same color table `C` in every call: bg / appNav / subNav / active / border / divider / muted / text / textSub / textMuted / brand / success / warning / danger.
- Active-nav key is a parameter, not a branch — makes every state frame a one-line difference.

### 6. Unify Chinese typography

Any frame with Chinese must use a single CJK font (**Noto Sans SC** is most reliable in Figma Desktop). Inter + CJK causes glyph fallback.

After building, run a page-wide font sweep: `findAllWithCriteria({types:['TEXT']})` → detect CJK → re-apply `Noto Sans SC` at mapped weight (Regular / Medium / Bold; no Semi Bold in Noto SC — map Inter Semi Bold → Noto Sans SC Bold).

See [patterns.md](patterns.md) for the exact sweep snippet.

### 7. Iterate versioned — don't overwrite

When the user pushes back on style, generate the new version **next to** the old one. Never delete the previous version until they explicitly approve. Typical progression we've seen:

- v1: hand-drawn → rejected for visual polish
- v2: team library components (e.g. SDS) → color scheme mismatch
- v3: Claude style → reference palette mismatch
- v4: shadcn-zinc 3-col (multica-style) → accepted
- v5: v4 + multi-agent + hover card → accepted

## When NOT to use this skill

- Single component / micro-edit — use figma-use directly.
- Pure style migration where PRD is unchanged — use figma-style-migration.
- Capturing a web page into Figma for the first time — use figma-generate-design.

## Supporting files

- [patterns.md](patterns.md) — reusable code: 3-col shell, SDS component wrappers, CJK sweep, Auto Layout helpers.
- [pitfalls.md](pitfalls.md) — non-obvious traps (WAF chunking, Auto Layout resize bug, z-order, CJK rendering).
- [prd-parsing.md](prd-parsing.md) — how to extract frame matrix from a Notion PRD with tables + callouts.
