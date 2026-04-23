# Strategies — Deep Reference

Load this after reading SKILL.md and choosing a strategy.

---

## Strategy A: Clone & Customize

Best when reference and target share structural similarity. Produces highest visual fidelity.

### A1 — Clone frames to a workspace page

Work in the **same file** as the reference to preserve component instances and variable bindings.

```js
const sourcePage = figma.root.children.find(p => p.name === "SOURCE_PAGE");
await figma.setCurrentPageAsync(sourcePage);
const source = sourcePage.children.find(f => f.id === "FRAME_ID");

const targetPage = figma.root.children.find(p => p.name === "Redesign")
  || (() => { const p = figma.createPage(); p.name = "Redesign"; return p; })();
await figma.setCurrentPageAsync(targetPage);

const clone = source.clone();
clone.name = "1. Screen Name";
clone.x = INDEX * (clone.width + 100);
clone.y = 0;
targetPage.appendChild(clone);
return { cloneId: clone.id };
```

**One frame per `use_figma` call.** Record all clone IDs.

### A2 — Replace text content

```js
const frame = await figma.getNodeByIdAsync("CLONE_ID");
const textNodes = frame.findAll(n => n.type === 'TEXT');
for (const t of textNodes) {
  const fonts = t.fontName === figma.mixed
    ? t.getRangeAllFontNames(0, t.characters.length)
    : [t.fontName];
  for (const f of fonts) await figma.loadFontAsync(f);
  // apply replacements
}
return { modified: textNodes.length };
```

### A3 — Add unique features from the delta list

Build new elements to match the reference's visual language (colors, radii, spacing). Use absolute positioning for non-auto-layout parents; insert into auto-layout when the parent uses it.

### A4 — Hide irrelevant elements

```js
const node = frame.findOne(n => n.name === "Element To Hide");
if (node) node.visible = false; // prefer over .remove() — reversible
```

---

## Strategy B: Extract & Rebuild

When reference and target are structurally different. **Even here, clone individual components** (buttons, cards, inputs) from the reference rather than building from raw rectangles.

### B1 — Extract tokens

Delegate to the upstream `figma-generate-design` skill's token discovery workflow:
1. `search_design_system` with `includeVariables`, `includeStyles`, `includeComponents`
2. Local variables: `figma.variables.getLocalVariableCollectionsAsync()`
3. Manual node inspection as a last resort:

```js
const frame = await figma.getNodeByIdAsync("FRAME_ID");
const tokens = { colors: new Set(), radii: new Set(), fonts: new Set(), spacing: new Set() };
frame.findAll(() => true).forEach(n => {
  if ('fills' in n) n.fills.filter(f => f.type === 'SOLID' && f.visible !== false)
    .forEach(f => tokens.colors.add(`${f.color.r.toFixed(3)},${f.color.g.toFixed(3)},${f.color.b.toFixed(3)}`));
  if ('cornerRadius' in n && n.cornerRadius > 0) tokens.radii.add(n.cornerRadius);
  if (n.type === 'TEXT') tokens.fonts.add(JSON.stringify(n.fontName));
  if ('itemSpacing' in n && n.itemSpacing > 0) tokens.spacing.add(n.itemSpacing);
});
return { colors: [...tokens.colors], radii: [...tokens.radii].sort((a,b) => a-b),
         fonts: [...tokens.fonts].map(f => JSON.parse(f)), spacing: [...tokens.spacing].sort((a,b) => a-b) };
```

### B2 — Build screens section-by-section

Follow the `figma-generate-design` workflow: create wrapper frame → build one section per `use_figma` call → use design system tokens instead of hardcoded values → screenshot after each section.

---

## Strategy C: Multi-Style Exploration

When the user hasn't locked down a visual direction.

### C1 — Lay out 2-3 variants side-by-side

Each variant is a separate top-level frame **on the same page**, numbered and spaced ~100px apart horizontally. Name them `{N}. {Screen} ({Style})` — e.g. `7. Market (iOS 26)`, `9. Market (ChatGPT Style)`.

### C2 — Reuse shared chrome via `.clone()`

Status bars, tab bars, nav shells: clone once from an existing frame, reuse across all variants. Record the source node ID.

```js
const src = await figma.getNodeByIdAsync('STATUS_BAR_NODE_ID');
const sb = src.clone();
newFrame.appendChild(sb);
sb.x = 0; sb.y = 0;
```

### C3 — Build each variant incrementally

Split each frame into 3-4 `use_figma` calls (≤80 lines each):
1. **Shell** — frame + clone status bar + nav bar
2. **Header** — search, hero card, category tabs
3. **Content** — list rows, info sections, CTAs
4. **Verify** — `get_screenshot`

If step 3 fails, steps 1-2 remain intact on canvas.

### C4 — After user picks a direction, pair it with a detail page

Place the detail frame directly to the right of its list frame (~100px gap). This pairing principle applies to any list → detail flow.

### C5 — CTA copy should encode context

| Vague | Contextual |
|---|---|
| Install | Install to conversation |
| View | Use in chat |
| Enable | Add to current assistant |

### C6 — CJK + Latin font pairing

When mixing Chinese and Latin text, load both font families in every script. Specific families depend on the project — check existing frames first. Common pairings: `Noto Sans SC` + `SF Pro`, `PingFang SC` + `Inter`.

---

## Common Patterns

### Track y-cursor for scrollable pages

When building detail pages that exceed device height, track `y` and resize the frame before it clips:

```js
let y = startY;
// ... build sections, incrementing y ...
if (y > frame.height - 40) frame.resize(frame.width, y + 60);
return { createdNodeIds: created, bottomY: y, frameId: frame.id };
```

### Enumerate frames for mapping

```js
const result = [];
for (const p of figma.root.children) {
  await figma.setCurrentPageAsync(p);
  result.push({ page: p.name, id: p.id,
    frames: p.children.map(c => ({ name: c.name, id: c.id, type: c.type,
      size: 'width' in c ? `${Math.round(c.width)}×${Math.round(c.height)}` : null }))
  });
}
return result;
```

### Inspect cloned frame structure

```js
const frame = await figma.getNodeByIdAsync("CLONE_ID");
function walk(n, depth) {
  if (depth > 3) return null;
  const info = { name: n.name, type: n.type, id: n.id };
  if (n.type === 'TEXT') info.text = n.characters.substring(0, 50);
  if ('children' in n) info.children = n.children.map(c => walk(c, depth + 1)).filter(Boolean);
  return info;
}
return walk(frame, 0);
```
