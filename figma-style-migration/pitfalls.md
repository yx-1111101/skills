# Pitfalls — Additive to figma-use

These are traps **not covered** by the upstream `figma-use` skill. For general API rules (font loading, color ranges, page context, layoutSizing order, error recovery), refer to `figma-use` directly.

---

## 1. Cross-file component import fails for community files

`importComponentByKeyAsync(key)` silently returns null or throws for community/third-party files (e.g. iOS Design Kit). Component keys are not publicly addressable.

**Workaround**: Copy needed components into the working file via Figma desktop first, then `.clone()` by node ID. Or build manually.

## 2. Clone preserves position — always reposition

Cloned frames land at the source's coordinates, overlapping the original.

```js
const clone = source.clone();
targetPage.appendChild(clone);
clone.x = desiredX; // must set after clone
clone.y = desiredY;
```

## 3. Instance children can't be added/removed

Component instances don't allow structural changes. Either detach first (`instance.detachInstance()` → returns a frame) or modify via exposed properties (`instance.setProperties({...})`).

## 4. Script timeout on large traversals

Traversing thousands of nodes in a single `use_figma` call may time out. **One frame per call** — one clone, one text replacement batch, or one structural modification.

## 5. Never generate icons — use the file's icon library

**DO NOT** create icons via `createNodeFromSvg()`, manually constructed vectors, or any other code-generated approach. The results are always lower quality than hand-crafted assets.

**Instead**, clone icons from the **"icon" page** already present in the working Figma file:

- **Page**: `icon` (id `45936:1338`)
- **Frame**: `General` (id `45936:1339`) — contains 50+ icons at 24×24
- **Reference icon URL**: https://www.figma.com/design/sjJwCaXmcPCrY4q9UkuwxX/chatGPT--Copy-?node-id=45936-1343

```js
// WRONG — generating a gear icon from SVG
const svg = '<svg ...>';
const icon = figma.createNodeFromSvg(svg); // ugly, inconsistent

// CORRECT — clone from the icon library page
const iconPage = figma.root.children.find(p => p.name === 'icon');
await figma.setCurrentPageAsync(iconPage);
const iconSource = iconPage.findOne(n => n.id === '45936:1343'); // gear icon
const icon = iconSource.clone();
await figma.setCurrentPageAsync(targetPage); // switch back
targetPage.appendChild(icon);
icon.x = desiredX;
icon.y = desiredY;
```

If the needed icon doesn't exist in the library, **ask the user** to add it to the icon page first rather than generating it.

## 6. Never use emoji as icon placeholders

**DO NOT** use emoji characters (🔍, ☁️, 📌, 💬, etc.) as stand-ins for UI icons. Emoji render inconsistently across devices and platforms, produce non-scalable bitmap glyphs, and cannot be tinted or restyled.

This applies to **all contexts**: shortcut rows, search bars, header buttons, upload zones, empty states, badges — anywhere an icon is needed.

**The rule**: If a proper vector icon doesn't exist in the file's icon library yet, ask the user to add one. Do not substitute an emoji and "fix it later."

```js
// WRONG — emoji as placeholder
const t = figma.createText();
t.characters = '🔍'; // will look broken at small sizes, can't be tinted

// CORRECT — clone the search icon from the icon library
const iconPage = figma.root.children.find(p => p.name === 'icon');
await figma.setCurrentPageAsync(iconPage);
const searchSrc = iconPage.findOne(n => n.id === '45936:1366'); // magnifying glass
const searchIcon = searchSrc.clone();
await figma.setCurrentPageAsync(targetPage);
targetPage.appendChild(searchIcon);
parentFrame.appendChild(searchIcon);
searchIcon.x = 10; searchIcon.y = 10;
try { searchIcon.resize(16, 16); } catch (_) {}
```

**Exception**: emoji that are part of actual *content* (e.g. a chat message "Feel free to ask anything 😊") are fine — only replace icon-role emoji.

## 7. Frame height overflow

Content exceeding device height (e.g. 874px iPhone) gets clipped. Track your `y` cursor; resize when `y > frame.height - 40`:

```js
if (y > frame.height - 40) frame.resize(frame.width, y + 60);
return { createdNodeIds: created, bottomY: y };
```
