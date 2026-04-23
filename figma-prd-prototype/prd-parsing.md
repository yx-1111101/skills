# PRD Parsing · figma-prd-prototype

How to read a Notion / Markdown PRD and extract what you need to build Figma frames. Written against the OpenFriday PRD V2.3 format but generalizable.

## 1. Fetch the PRD

```js
// Notion
mcp__claude_ai_Notion__notion-fetch({
  id: 'https://www.notion.so/<page-id>'
});

// Nested pages: the parent usually contains a "详细功能页" list of child links.
// Fetch the parent first to discover the full page map, then fetch each child.
```

Don't try to WebFetch Notion pages — the rendered HTML is JS-heavy and often useless. Use the Notion MCP.

## 2. Extract this in order

### 2.1 Module list (what to build)

Look for a section titled **"详细功能页" / "模块大纲" / "功能列表"** or numbered headings like `4.1`, `4.2`, `4.3`. Each becomes a top-level frame group.

Example extraction from OpenFriday PRD V2.3 §10:

| PRD § | Module | Frame count estimate |
|---|---|---|
| 4.1 | AUTH 冷启动与登录 | 1 (login page) |
| 4.2 | Gateway 管理 | 5 (P1 empty, P2 list, P2 detail, rename modal, unbind modal) |
| 4.3 | 添加 Friday Gateway | 2–3 (entry, pairing, success) |
| 4.4 | 添加外部 Gateway | 4 (P1 OpenClaw, P1 Hermes, failure, success) |
| 4.5 | 核心对话 | 2+ (default, multi-agent collab, offline, read-only) |
| 4.6 | 模型选择 | 1 popover + 1 settings page |
| 4.8 | 任务看板 | 2 (单次 / 长期 tabs) |
| 4.9 | 设置中心 | ~8 (one per sub-module) |

### 2.2 Per-module state list

Every module PRD page usually has a **"状态" / "States" / "页面说明"** table. Each row = one frame variant.

Canonical state set you should look for:
- **Empty** (no data, first-time user)
- **Default** (normal populated)
- **Loading** / processing
- **Failure** (inline with recovery actions — per PRD rule "先说发生了什么，再说可以做什么")
- **Success** (confirmation of a completed action)

If the PRD lists state enums (e.g. `anonymous | auth_processing | logged_in_no_gateway | logged_in_ready`), each one is a potential frame.

### 2.3 Global context that must appear everywhere

Scan the PRD "全局规则" / "对象模型" / "上下文规则" section. For OpenFriday:
- Current Gateway name + online status
- Current Agent
- Current Session / Model

These become fixed UI elements (sidebar pill, context bar, avatar) that appear in **every** frame. Bake them into your shell helpers (`appNav`, `contextBar`) so consistency is automatic.

### 2.4 Acceptance rules → UI affordances

Each module page ends with **"验收要点" / "Acceptance criteria"**. Translate each rule into a visible UI element:

| PRD rule | UI affordance |
|---|---|
| "中止需二次确认" | Destructive button must open a confirm modal, not act immediately |
| "凭证一次性有效" | Show TTL countdown (e.g. "有效 09:42 后失效") next to input |
| "目标未就绪必须明确返回" | Inline red banner with specific cause + "重新获取凭证" action |
| "切换 Gateway 后 Session 必须收敛" | Gateway pill switches → session list filters / reloads |
| "最多开启 6 个" | Counter in card header ("4 / 6") + disabled state on toggles when at limit |

### 2.5 Copy that's fixed by PRD

Any PRD that quotes error strings ("当前配对码已过期，请重新获取") — use those **verbatim** in the frame. Don't paraphrase or translate. Spec copy is often legally / compliance reviewed.

## 3. Frame matrix template

Fill this in before touching Figma:

```markdown
## Module: {name} (PRD §{section})

### Frames
| # | State | Entry | What's different vs default |
|---|---|---|---|
| 1 | Empty | First visit, 0 items | Hero illustration + 2 CTA cards |
| 2 | Default | Has items | Table / list of items |
| 3 | Detail | Click item | Side panel or /detail route |
| 4 | Loading | Submit pressed | Button in loading state |
| 5 | Failure | Submit fails | Inline red banner + recovery chips |
| 6 | Success | Action complete | Centered success card |

### Context always visible
- App nav (Chat / Skill Market / Tasks / Settings)
- Gateway pill (name + online status)
- (if settings) Sub-nav with active key

### Positions (y = 2500 for v4)
| # | x | Frame name |
|---|---|---|
| 1 | 0     | v4 {module} Empty |
| 2 | 1540  | v4 {module} Default |
| 3 | 3080  | v4 {module} Detail |
| 4 | 4620  | v4 {module} Loading |
| 5 | 6160  | v4 {module} Failure |
| 6 | 7700  | v4 {module} Success |
```

## 4. Ambiguities to clarify before building

If the PRD has any of these, ask the user first:

- **Modal vs full page**: PRD says "弹出" could mean either. Ask.
- **Tabs vs sub-nav**: `Settings > General > Theme` — is the leftmost column Settings sub-nav, or horizontal tabs under a header?
- **Column count**: "三栏" vs "四栏" is a load-bearing decision. Write a markdown layout proposal and wait for 确认.
- **Style reference**: if they haven't named a visual (Claude / multica / ChatGPT / Teams), ask for a Figma reference URL. Never guess.

## 5. Signals that the PRD is under-spec'd

Any of these means the frame can't be built precisely yet — flag it and ask:

- State table lacks a "loading" or "failure" row (but the flow clearly has async work).
- Copy is described abstractly ("展示失败原因") without actual strings.
- Numbers are placeholders (`GR-003`, `GR-006`) — go fetch the referenced rules doc before assuming.
- No acceptance criteria for a destructive action (delete / unbind / logout).

Build what you can, explicitly call out what you had to assume, and link back to the PRD section.
