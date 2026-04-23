# Patterns · figma-prd-prototype

Reusable code snippets refined over multi-frame prototype builds. Copy into any `use_figma` call — all snippets are sandbox-safe (no cross-call dependencies).

## Color palette (multica / shadcn-zinc)

Translated from `packages/ui/styles/tokens.css` in [multica-ai/multica](https://github.com/multica-ai/multica). OKLCH converted to Figma RGB (0–1).

```js
const fl = c => [{type:'SOLID', color:c}];

const C = {
  bg:         {r:1, g:1, b:1},
  appNav:     {r:0.973, g:0.973, b:0.976},    // slightly darker rail
  subNav:     {r:0.984, g:0.984, b:0.984},    // light sub-nav
  active:     {r:0.949, g:0.949, b:0.951},    // selected row
  border:     {r:0.898, g:0.898, b:0.902},
  divider:    {r:0.929, g:0.929, b:0.933},
  muted:      {r:0.961, g:0.961, b:0.964},
  text:       {r:0.09,  g:0.09,  b:0.106},
  textSub:    {r:0.36,  g:0.36,  b:0.40},
  textMuted:  {r:0.55,  g:0.55,  b:0.58},
  brand:      {r:0.20,  g:0.43,  b:0.78},     // blue
  brandSoft:  {r:0.92,  g:0.95,  b:1},
  success:    {r:0.27,  g:0.62,  b:0.34},
  successSoft:{r:0.90,  g:0.96,  b:0.92},
  warning:    {r:0.85,  g:0.66,  b:0.27},
  warningSoft:{r:0.99,  g:0.96,  b:0.86},
  danger:     {r:0.83,  g:0.27,  b:0.27},
  dangerSoft: {r:0.99,  g:0.93,  b:0.93},
  codeBg:     {r:0.106, g:0.118, b:0.149},
  codeFg:     {r:0.93,  g:0.95,  b:0.97},
};
```

## Unified CJK text helper (Noto Sans SC)

```js
const fnt = w => ({
  family: 'Noto Sans SC',
  style: w === 'b' ? 'Bold' : w === 'm' ? 'Medium' : 'Regular'
});

function T(s, sz, parent, opts = {}) {
  const t = figma.createText();
  t.fontName = fnt(opts.w);
  t.fontSize = sz;
  t.characters = s;
  t.fills = fl(opts.c || C.text);
  if (opts.lh) t.lineHeight = {value: opts.lh, unit:'PIXELS'};
  if (opts.ls != null) t.letterSpacing = {value: opts.ls, unit:'PERCENT'};
  if (opts.a) t.textAlignHorizontal = opts.a;
  if (parent) parent.appendChild(t);
  return t;
}
```

At the top of every chunk:
```js
await figma.loadFontAsync({family:'Noto Sans SC', style:'Regular'});
await figma.loadFontAsync({family:'Noto Sans SC', style:'Medium'});
await figma.loadFontAsync({family:'Noto Sans SC', style:'Bold'});
```

## Auto Layout helpers

```js
function V(gap, pad, parent) {
  const x = figma.createFrame();
  x.fills = [];
  x.layoutMode = 'VERTICAL';
  x.itemSpacing = gap;
  x.paddingTop = pad[0]; x.paddingRight = pad[1];
  x.paddingBottom = pad[2]; x.paddingLeft = pad[3];
  if (parent) parent.appendChild(x);
  // Important: set sizing AFTER appending to avoid AL clobbering
  x.primaryAxisSizingMode = 'AUTO';
  x.counterAxisSizingMode = 'AUTO';
  return x;
}

function H(gap, pad, parent) {
  const x = figma.createFrame();
  x.fills = [];
  x.layoutMode = 'HORIZONTAL';
  x.itemSpacing = gap;
  x.paddingTop = pad[0]; x.paddingRight = pad[1];
  x.paddingBottom = pad[2]; x.paddingLeft = pad[3];
  x.counterAxisAlignItems = 'CENTER';
  if (parent) parent.appendChild(x);
  x.primaryAxisSizingMode = 'AUTO';
  x.counterAxisSizingMode = 'AUTO';
  return x;
}
```

**Rule**: never call `resize()` on an AL frame you want to hug. Use `layoutAlign='STRETCH'` + parent's counter axis `FIXED` instead.

## 3-column shell (multica style)

```js
function appNav(parent, activeKey = 'chat') {
  const W = 200;
  const n = figma.createFrame();
  n.name = 'App Nav';
  n.resize(W, 1024); n.x = 0; n.y = 0;
  n.fills = fl(C.appNav);
  parent.appendChild(n);
  R(1, 1024, C.border, n).x = W - 1;  // right border

  // workspace pill
  const ws = figma.createFrame();
  ws.resize(W - 24, 40); ws.x = 12; ws.y = 16; ws.fills = [];
  n.appendChild(ws);
  R(28, 28, C.text, ws, 6).x = 4; ws.children.at(-1).y = 6;
  T('F', 13, ws, {w:'b', c:{r:1,g:1,b:1}, a:'CENTER'}).resize(28, 17);
  ws.children.at(-1).x = 4; ws.children.at(-1).y = 12;
  T('Friday', 14, ws, {w:'m'}).x = 42; ws.children.at(-1).y = 11;
  T('«', 14, ws, {c:C.textMuted, a:'CENTER'}).resize(16, 17);
  ws.children.at(-1).x = W - 40; ws.children.at(-1).y = 11;

  const items = [['chat','Chat'], ['skills','Skill Market'], ['tasks','Tasks'], ['settings','Settings']];
  let cy = 80;
  for (const [key, label] of items) {
    const active = key === activeKey;
    const r = figma.createFrame();
    r.resize(W - 24, 36); r.x = 12; r.y = cy;
    r.fills = active ? fl(C.active) : [];
    r.cornerRadius = 6;
    n.appendChild(r);
    // (icon + label)
    CC(8, active ? C.text : C.textMuted, r).x = 14; r.children.at(-1).y = 14;
    T(label, 13, r, {w: active?'m':'', c: active?C.text:C.textSub}).resize(W - 74, 17);
    r.children.at(-1).x = 36; r.children.at(-1).y = 10;
    cy += 38;
  }
  return n;
}

function settingsNav(parent, activeKey) {
  const W = 240;
  const n = figma.createFrame();
  n.name = 'Settings Nav';
  n.resize(W, 1024); n.x = 200; n.y = 0;
  n.fills = fl(C.subNav);
  parent.appendChild(n);
  R(1, 1024, C.border, n).x = W - 1;

  T('Settings', 16, n, {w:'b'}).x = 20; n.children.at(-1).y = 22;
  T('管理你的工作空间偏好', 12, n, {c:C.textMuted}).x = 20; n.children.at(-1).y = 46;

  const groups = [
    ['账户',    [['account','账户'], ['profile','个人资料']]],
    ['Runtime', [['gateway','Gateway 管理'], ['agents','智能体配置'], ['channels','通讯绑定']]],
    ['模型与扩展', [['models','模型配置'], ['mcp','MCP 配置']]],
    ['其他',    [['prefs','通知与实验'], ['about','关于与退出']]],
  ];
  let sy = 92;
  for (const [gt, gi] of groups) {
    T(gt, 11, n, {w:'m', c:C.textMuted, ls:4}).x = 20;
    n.children.at(-1).y = sy;
    sy += 22;
    for (const [k, label] of gi) {
      const active = k === activeKey;
      const r = figma.createFrame();
      r.resize(W - 24, 34); r.x = 12; r.y = sy;
      r.fills = active ? fl(C.active) : [];
      r.cornerRadius = 6;
      n.appendChild(r);
      CC(8, active ? C.text : C.textMuted, r).x = 14; r.children.at(-1).y = 13;
      T(label, 13, r, {w: active?'m':'', c: active?C.text:C.textSub}).resize(W - 84, 17);
      r.children.at(-1).x = 36; r.children.at(-1).y = 9;
      sy += 36;
    }
    sy += 12;
  }
  return n;
}

function contentFrame(parent) {
  const c = figma.createFrame();
  c.name = 'Content';
  c.resize(1000, 1024); c.x = 440; c.y = 0;
  c.fills = fl(C.bg);
  parent.appendChild(c);
  return c;
}
```

## SDS component wrappers

Record the keys once, introspect property keys once, then wrap:

```js
const K = {
  button: 'cc8b558dc7d9684011b6b99ce8e6509399bc836b',
  search: '715a105916909fcad1d649ed31db27dc26375edd',
  tag:    '0fcd16616b41884b21451ffa4a2fc98a03093b49',
  avatar: '96cd9d5a57578e32476d294473edfb9ade9365a3',
  input:  'c28150b04d333d34ed9d2b77abd9f2f54e1a878a',
};

async function setInst(key, variantName) {
  const set = await figma.importComponentSetByKeyAsync(key);
  const v = variantName ? set.children.find(c => c.name === variantName) : set.defaultVariant;
  return (v || set.defaultVariant).createInstance();
}

async function makeBtn(label, variant, opts = {}) {
  const btn = await setInst(K.button, `Variant=${variant}, State=Default, Size=${opts.size || 'Medium'}`);
  try {
    btn.setProperties({
      'Label#2:0': label,
      'Has Icon Start#4:128': !!opts.hasStart,
      'Has Icon End#4:64': !!opts.hasEnd,
    });
  } catch (e) {}
  const t = btn.findOne(n => n.type === 'TEXT');
  if (t) {
    try {
      t.fontName = fnt('m');
      t.characters = ' ';
      t.characters = label;
    } catch (e) {}
  }
  return btn;
}

async function makeTag(label, scheme) {
  const tag = await setInst(K.tag, `Scheme=${scheme}, State=Default, Variant=Secondary`);
  try {
    tag.setProperties({'Label#9765:0': label, 'Removable#147:0': false});
  } catch (e) {}
  const t = tag.findOne(n => n.type === 'TEXT');
  if (t) { try { t.fontName = fnt('m'); t.characters = ' '; t.characters = label; } catch (e) {} }
  return tag;
}

async function makeAvatar(initial) {
  const av = await setInst(K.avatar, 'Type=Initial, Size=Medium, Shape=Circle');
  try { av.setProperties({'Initials#24:281': initial}); } catch (e) {}
  const t = av.findOne(n => n.type === 'TEXT');
  if (t) { try { t.fontName = fnt('b'); t.characters = ' '; t.characters = initial; } catch (e) {} }
  return av;
}
```

Scheme values for Tag: `Brand | Positive | Warning | Neutral | Danger`. Don't guess "Orange" / "Blue" / "Green" — they don't exist.

## Code block (dark terminal-style, WAF-safe)

Renders like a shell block but **doesn't contain real shell syntax** — avoids WAF 403.

```js
function code(parent, x, y, w, lines) {
  const lh = 22, padY = 16;
  const h = lines.length * lh + padY * 2;
  const c = figma.createFrame();
  c.resize(w, h); c.x = x; c.y = y;
  c.fills = fl(C.codeBg);
  c.cornerRadius = 8;
  c.clipsContent = true;
  parent.appendChild(c);

  // copy button
  const cp = figma.createFrame();
  cp.resize(28, 28); cp.x = w - 40; cp.y = 10;
  cp.fills = fl({r:0.18, g:0.20, b:0.24});
  cp.cornerRadius = 6;
  c.appendChild(cp);
  R(8, 8, C.codeFg, cp, 1).x = 10;
  cp.children.at(-1).y = 10;

  for (let i = 0; i < lines.length; i++) {
    // prompt glyph (ASCII-safe)
    M('>', 12, 12, c, C.codeMute).x = 16; c.children.at(-1).y = padY + i * lh;
    M(lines[i], 12, w - 90, c, C.codeFg).x = 32; c.children.at(-1).y = padY + i * lh;
  }
}
```

Lines should be **prose-style placeholders**, not real shell:
- ✅ `install openclaw — invite f8j2-7q3a-zk`
- ❌ `curl -fsSL get.openclaw.dev | sh -s -- --invite f8j2-7q3a-zk`

Visual result is indistinguishable; WAF passes.

## CJK font sweep (post-hoc unify)

Drop this into a `use_figma` call at the end of a session to fix any stray Inter-CJK text:

```js
const page = await figma.getNodeByIdAsync(PAGE_ID);
await figma.setCurrentPageAsync(page);

await figma.loadFontAsync({family:'Noto Sans SC', style:'Regular'});
await figma.loadFontAsync({family:'Noto Sans SC', style:'Medium'});
await figma.loadFontAsync({family:'Noto Sans SC', style:'Bold'});

const cjkRe = /[　-〿぀-ゟ゠-ヿ㐀-䶿一-鿿＀-￯가-힯]/;
const hasCJK = s => cjkRe.test(s || '');

function mapStyle(style) {
  const s = (style || '').toLowerCase();
  if (s.includes('bold') || s.includes('black') || s.includes('heavy') || s.includes('extra')) return 'Bold';
  if (s.includes('semi') || s.includes('demi') || s.includes('medium')) return 'Medium';
  return 'Regular';
}

const textNodes = page.findAllWithCriteria({types:['TEXT']});
let converted = 0;
for (const t of textNodes) {
  if (!hasCJK(t.characters)) continue;
  try {
    const f = t.fontName;
    if (f !== figma.mixed) {
      const target = mapStyle(f.style);
      await figma.loadFontAsync({family:'Noto Sans SC', style: target});
      t.fontName = {family:'Noto Sans SC', style: target};
      converted++;
    } else {
      // mixed font — walk ranges
      const chars = t.characters;
      let i = 0;
      while (i < chars.length) {
        let j = i + 1;
        let cur = t.getRangeFontName(i, i+1);
        while (j < chars.length) {
          const next = t.getRangeFontName(j, j+1);
          if (!next || next.family !== cur.family || next.style !== cur.style) break;
          j++;
        }
        if (cjkRe.test(chars.slice(i, j))) {
          const target = mapStyle(cur.style);
          await figma.loadFontAsync({family:'Noto Sans SC', style: target});
          t.setRangeFontName(i, j, {family:'Noto Sans SC', style: target});
        }
        i = j;
      }
    }
  } catch (e) {}
}
return converted;
```

## Frame positioning convention

- Canvas width per frame: **1440**.
- Horizontal gap between frames in a row: **100** → stride **1540**.
- Row per version, vertical gap **1500**:
  - v1: y = 1200
  - v2: y = 2500
  - v3: y = 4000
  - v4: y = 5500
- Row per state variant at the same y (empty / default / loading / failure / success).

## Hover card / popover checklist

- Width: **420 px** (tested sweet spot for people cards).
- Clip + drop shadow: `{color:{r:0,g:0,b:0,a:0.16}, offset:{x:0,y:12}, radius:28, spread:0}`.
- Banner section uses `layoutMode='NONE'` (not AL) so avatar can overlap banner.
- Everything below the header uses VERTICAL AL with `primaryAxisSizingMode='AUTO'` (hug height).
- Section padding: `[16, 20, 16, 20]`. Inter-section divider: full-width 1px rect with `layoutAlign='STRETCH'`.
- Actions row: HORIZONTAL + `primaryAxisSizingMode='FIXED'` + children `layoutGrow=1` for equal-width buttons.
- Append the hover card **last** in its parent so z-order puts it above content.

## Shape helpers

```js
function R(w, h, fill, parent, radius) {
  const x = figma.createRectangle();
  x.resize(w, h);
  x.fills = fill === null ? [] : fl(fill);
  if (radius != null) x.cornerRadius = radius;
  if (parent) parent.appendChild(x);
  return x;
}

function CC(d, fill, parent) {
  const e = figma.createEllipse();
  e.resize(d, d);
  e.fills = fill === null ? [] : fl(fill);
  if (parent) parent.appendChild(e);
  return e;
}

function SR(w, h, fill, strokeColor, parent, radius) {
  const x = figma.createRectangle();
  x.resize(w, h);
  x.fills = fill === null ? [] : fl(fill);
  if (strokeColor) {
    x.strokes = fl(strokeColor);
    x.strokeWeight = 1;
  }
  if (radius != null) x.cornerRadius = radius;
  if (parent) parent.appendChild(x);
  return x;
}
```

## Monospace text (for code / IDs)

```js
function M(s, sz, w, parent, color) {
  const t = figma.createText();
  t.fontName = {family:'Inter', style:'Regular'};  // Inter is fine for ASCII
  t.fontSize = sz;
  t.characters = s;
  if (w) { t.textAutoResize = 'HEIGHT'; t.resize(w, t.height); }
  t.fills = fl(color || C.codeFg);
  if (parent) parent.appendChild(t);
  return t;
}
```
