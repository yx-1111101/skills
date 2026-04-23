# Style Catalog — Common UI Design Languages

Load this when the user references a specific product style (e.g. "ChatGPT 风格", "iOS 风", "Linear 那种感觉"). Find the matching section and use its principles to guide design decisions during multi-style exploration (Strategy C) or rebuild (Strategy B).

Each entry describes the **design language** — not pixel specs. Adapt to the target's content and device.

### Master Reference File

All style templates below live in a single Figma file for side-by-side comparison:

- **File**: `https://www.figma.com/design/sjJwCaXmcPCrY4q9UkuwxX`
- **Page**: `Claw Redesign`

| Frame | Node ID | Style | Type |
|---|---|---|---|
| 5A. Skill Market (Apps Style) | `45795:1195` | Apps / Card Grid | List |
| 5B. My Skills (Apps Style) | `45800:1206` | Apps / Card Grid | List |
| 5C. Skill Detail Modal | `45808:1266` | Apps / Modal | Detail |
| 7. Skill Market (iOS 26) | `45811:1246` | iOS Settings | List |
| 8. Skill Detail (iOS 26) | `45823:1257` | iOS Settings | Detail |
| 9. Skill Market (ChatGPT Style) | `45844:1268` | ChatGPT / Minimal | List |
| 10. Skill Detail (ChatGPT Style) | `45850:1279` | ChatGPT / Minimal | Detail |
| 1A. New Chat (Keyboard Active) | `45856:1290` | ChatGPT / Chat | Keyboard Standby |
| 1B. New Chat (Typing) | `45859:1457` | ChatGPT / Chat | Typing State |

Supporting frames: `3A. Sidebar (Skill Market Entry)` (`45793:1159`), `6. Chat (Skill Picker)` (`45803:1217`)

### Community Reference Templates

| Template | URL | Key Frames |
|---|---|---|
| ChatGPT iOS App UI (Free) | `https://www.figma.com/design/iSeDyt5jHT6aNsCgSdlwmO` | Keyboard Standby (`2:3459`), Typing (`2:3506`), Main View (`13:801`), Getting Answer (`13:803`), Scrolling (`1:441`), Settings (`24:703`) |

Use `get_screenshot` with any node ID above to quickly recall the visual treatment.

---

## ChatGPT / GPT Store Style

**Reference**: [chatgpt.com/gpts](https://chatgpt.com/gpts) — GPT Store / Explore GPTs page

**Figma templates** (Claw Redesign file):
- `9. Skill Market (ChatGPT Style)` — node `45844:1268` (402×874)
- `10. Skill Detail (ChatGPT Style)` — node `45850:1279` (402×1100)
- File: `https://www.figma.com/design/sjJwCaXmcPCrY4q9UkuwxX`  Page: `Claw Redesign`

**Core feel**: Minimal, content-first, conversational. The interface recedes; the content speaks.

| Dimension | Pattern |
|---|---|
| Layout | Single-column, generous vertical spacing, full-width search at top |
| Color | Near-monochrome (white/gray). One accent gradient for featured card only |
| Typography | Clean sans-serif, two levels max (title bold + subtitle regular). No decorative fonts |
| Icons | Absent or extremely subtle. Lists rely on title + subtitle + chevron `›` |
| Cards | One prominent "hero" card (gradient background, prompt bubble, preview area). Remaining items are flat list rows |
| Navigation | Text-only horizontal tabs (no pill/chip backgrounds for inactive states). Active = bold + dark, inactive = regular + gray |
| CTAs | Full-width rounded buttons. Primary = dark fill + white text. Secondary = ghost (border only) |
| Detail page | Large title, category pill, description paragraph, primary + secondary CTA, then sections ("Examples", "About", "Info") with section headings |
| Density | Low — ample whitespace between sections. No dividers between major blocks, thin hairlines between list rows only |
| Motion | None visible in static mocks; transitions implied to be simple fades |

### List / Market Page — Anatomy (top to bottom)

```
┌─────────────────────────────────────┐
│  ≡        Page Title        [Beta]  │ ← Top bar: hamburger left, centered title,
│                                     │   optional pill badge right
├─────────────────────────────────────┤
│  🔍 Search placeholder...          │ ← Full-width pill search bar
├─────────────────────────────────────┤
│ ╔═══════════════════════════════╗   │
│ ║  Title              [查看]   ║   │ ← Hero card: gradient fill (blue→teal)
│ ║  Subtitle                    ║   │
│ ║  ┌─@mention prompt────────┐  ║   │ ← Prompt bubble: white, high opacity
│ ║  └────────────────────────┘  ║   │
│ ║  ┌─ preview area ─────────┐  ║   │ ← Preview: white, low opacity (~35%)
│ ║  └────────────────────────┘ ›║   │
│ ╚═══════════════════════════════╝   │
├─────────────────────────────────────┤
│  **Active**  Tab2  Tab3  Tab4  Tab5 │ ← Text tabs, no backgrounds
├─────────────────────────────────────┤
│  Title                          ›   │ ← List rows: no icon, title + subtitle
│  subtitle                           │   + right chevron. Hairline divider
│─────────────────────────────────────│   between rows (inset, not full-width).
│  Title                          ›   │   No divider after last row.
│  subtitle                           │
└─────────────────────────────────────┘
```

**Top bar details**:
- Hamburger icon (`≡`) on left, page title centered (medium weight, ~17px), optional pill on right
- Pill: small rounded rectangle (cornerRadius ≈ 14), light gray fill + 1px border, small text

**Search bar details**:
- Full-width with horizontal padding (~16px from edges)
- Pill shape (cornerRadius ≈ height/2), light gray background (no border)
- Magnifying glass icon + placeholder text, both in muted gray

**Hero card details**:
- Width fills available space (minus page margins), height ~200px, cornerRadius ~20
- Gradient: cool blue → teal (left to right or top-left to bottom-right)
- Content layers from top: title (bold white) + subtitle (white ~88% opacity) → prompt bubble → preview area
- Prompt bubble: white background (~95% opacity), cornerRadius ~14, contains `@name` + sample command
- Preview area: white background (~35% opacity), cornerRadius ~12, centered label text
- Optional "View" button: top-right, semi-transparent white fill (~22% opacity), small text
- Single chevron `›` at right edge, white ~85% opacity

**Category tabs details**:
- Horizontal text row below hero card, ~16px left padding
- Active tab: bold + near-black. Inactive tabs: regular weight + medium gray
- Spacing between tabs: ~20px. No underlines, no pill backgrounds, no indicators

**List row details**:
- Height ~72px per row
- Title: medium weight, ~16px, near-black. Positioned ~14px from top
- Subtitle: regular weight, ~13px, medium gray. Positioned ~38px from top
- Chevron `›`: right-aligned, light gray, vertically centered
- Hairline divider: 1px, very light gray, inset (starts at left padding, not full width)
- No divider after the final row

### Detail Page — Anatomy (top to bottom)

```
┌─────────────────────────────────────┐
│  ‹         Detail Title             │ ← Nav bar: back arrow + centered title
│─────────────────────────────────────│   + hairline bottom border
│                                     │
│  Large Bold Title                   │ ← Title: large (24-26px), bold, near-black
│  ┌─────┐                           │
│  │ Tag │                            │ ← Category pill: small, gray bg + border
│  └─────┘                           │
│  Description paragraph in gray,     │ ← Description: regular ~15px, gray,
│  wrapping to fill available width.  │   auto-height, generous line-height
│                                     │
│  ╔═════════════════════════════╗    │
│  ║    Primary CTA Button      ║    │ ← Primary: full-width, dark fill,
│  ╚═════════════════════════════╝    │   white text, large cornerRadius (~24)
│  ┌─────────────────────────────┐    │
│  │    Secondary CTA Button     │    │ ← Secondary: same size, ghost (border
│  └─────────────────────────────┘    │   only), dark text
│                                     │
│  Section Title (bold)               │ ← "Examples" / "About" / "Info"
│  ╔═══════════════════════════╗      │
│  ║  Gradient card with       ║      │ ← Reuses hero gradient treatment
│  ║  @mention bubble + preview║      │
│  ╚═══════════════════════════╝      │
│                                     │
│  Section Title (bold)               │
│  Body text paragraph...             │ ← "About" section: plain paragraph
│                                     │
│  Section Title (bold)               │
│  ┌ Label ──────── Value ─────┐      │ ← "Info" section: key-value rows,
│  │─────────────────────────── │      │   label (gray left) + value (dark right)
│  │ Label ──────── Value       │      │   hairline dividers, ~44px row height
│  └────────────────────────────┘     │
└─────────────────────────────────────┘
```

**Nav bar details**:
- Back arrow `‹` (large, ~28px), page title centered (medium weight ~17px)
- Hairline bottom border (full width, ~0.5px, very light gray)

**Title + tag area**:
- Title: bold, 24-26px, near-black, left-aligned
- Category pill directly below title: small (cornerRadius ~10), light gray fill + 1px border, small text (~12px) in medium gray
- Gap between title and pill: ~8px

**Description**:
- Regular weight, ~15px, medium gray
- Text wraps within available width (auto-resize height)
- Gap to CTAs below: ~20px

**CTA buttons**:
- Both full-width (fill available minus page margins), height ~48px, cornerRadius ~24
- Primary: dark near-black fill, white text (medium weight ~16px), centered
- Secondary: no fill, 1px gray border, dark text, same dimensions
- Gap between primary and secondary: ~10px
- Gap to next section: ~24px

**Section structure**:
- Section heading: bold, ~17px, near-black
- Gap heading → content: ~12px
- Gap between sections: ~24-28px

**Info table rows**:
- Row height ~44px
- Label: regular weight ~14px, muted gray, left-aligned
- Value: medium weight ~14px, near-black, positioned ~120px from left (or right-aligned)
- Hairline divider at bottom of each row

### Color Palette (Figma 0-1 range)

| Token | RGB (0-1) | Usage |
|---|---|---|
| text-primary | `0.06–0.12, 0.06–0.12, 0.08–0.14` | Titles, values, active tabs |
| text-secondary | `0.42–0.50, 0.42–0.50, 0.45–0.52` | Subtitles, descriptions, labels, placeholders |
| surface-search | `0.96, 0.96, 0.97` | Search bar fill |
| surface-pill | `0.95, 0.95, 0.96` | Pill/badge fill |
| border-pill | `0.88, 0.88, 0.90` | Pill/badge stroke |
| divider | `0.90, 0.90, 0.92` | Hairline row separators |
| hero-gradient-start | `0.25, 0.55, 0.85` | Hero card gradient (blue) |
| hero-gradient-end | `0.35, 0.75, 0.82` | Hero card gradient (teal) |
| white-high | opacity 0.95 | Prompt bubble bg |
| white-low | opacity 0.30–0.35 | Preview area bg |
| white-button | opacity 0.22 | Hero inline button bg |
| cta-primary-fill | `0.12, 0.12, 0.14` | Primary button fill |

### Spacing System

| Token | Value | Usage |
|---|---|---|
| page-margin | 16–20px | Left/right padding from frame edge |
| element-gap-sm | 8–10px | Between tightly related elements (title↔pill, primary↔secondary CTA) |
| element-gap-md | 12–14px | Section heading → content |
| section-gap | 20–28px | Between major sections |
| list-row-height | ~72px | Each list row in market page |
| info-row-height | ~44px | Each key-value row in detail page |
| search-height | ~44px | Search bar |
| cta-height | ~48px | Full-width buttons |
| hero-height | ~200px (market), ~168px (detail) | Featured card |
| tab-spacing | ~20px | Between category tab labels |

### Typography Scale

| Level | Weight | Size | Color token |
|---|---|---|---|
| Page title (nav bar) | Medium | ~17px | text-primary |
| Large title (detail) | Bold | 24–26px | text-primary |
| Hero title | Bold | ~18px | white |
| Hero subtitle | Regular | ~13px | white 88% |
| Section heading | Bold | ~17px | text-primary |
| List row title | Medium | ~16px | text-primary |
| List row subtitle / Description | Regular | 13–15px | text-secondary |
| Pill / Badge text | Medium | ~12px | text-secondary |
| CTA text | Medium | ~16px | white (primary) or text-primary (secondary) |
| Info label | Regular | ~14px | text-secondary |
| Info value | Medium | ~14px | text-primary |

### Signature Element — Prompt Bubble

The `@mention` bubble inside the hero card is the defining visual motif. It communicates "this is a conversational tool, not a traditional app" in a single glance.

Construction:
- Container: white fill at ~95% opacity, cornerRadius ~14, padding ~12px horizontal
- Text: `@name` + sample command in dark color, regular weight ~12-13px
- Sits inside the gradient hero card, below title/subtitle, above preview area

### Implementation Lessons

1. **Build the hero card as a standalone section** — it has the most visual complexity (gradient, semi-transparent layers, bubble). Get this right before adding the list below it.
2. **The "view" button on the hero** uses semi-transparent white fill (~22%), not a solid color. This lets the gradient show through while remaining tappable.
3. **Preview area inside hero** is a simple frame with low-opacity white fill and centered text — don't over-engineer it with actual content.
4. **Category tabs are plain text nodes**, not components. Position them with a manual x offset (accumulate previous text width + gap). Bold the active tab; keep others regular weight.
5. **List rows without icons feel empty at first** — this is by design. The generous row height (~72px) and two-line text (title + subtitle) fill the space. Trust the whitespace.
6. **Detail page often exceeds device viewport** — the sections stack up (title + CTAs + example + about + info). Plan for a frame taller than 874px or design a clear scroll fold.
7. **Info table alignment**: don't use a full table component. Simple frames with a label text (left, gray) + value text (right offset ~120px, dark) + bottom hairline are cleaner and more ChatGPT-like.
8. **Primary CTA copies should be contextual** ("Install to conversation", not just "Install") — extra words clarify where the action takes effect.

**Anti-patterns to avoid**: Left-side icons on every list row. Colored category badges per row. Dense system-style info tables. Heavy shadows or elevation. Pill-shaped tab indicators. Anything that makes it feel like an app store rather than a conversation tool.

---

## iOS / Apple Settings Style

**Reference**: iOS Settings app, App Store detail page

**Figma templates** (Claw Redesign file):
- `7. Skill Market (iOS 26)` — node `45811:1246` (402×874)
- `8. Skill Detail (iOS 26)` — node `45823:1257` (402×874)
- File: `https://www.figma.com/design/sjJwCaXmcPCrY4q9UkuwxX`  Page: `Claw Redesign`

**Core feel**: System-native, structured, information-dense. Familiar and predictable.

| Dimension | Pattern |
|---|---|
| Layout | Grouped inset list sections with rounded corners, section headers in uppercase gray |
| Color | System white/gray backgrounds. Tinted icons (SF Symbols in colored circles) |
| Typography | SF Pro. System sizes (17pt body, 22pt large title). Dynamic Type support implied |
| Icons | Round colored squares (cornerRadius ~10) with white SF Symbol glyphs. Category-coded colors |
| Cards | Rare — information lives in grouped list rows |
| Navigation | Large title collapses on scroll. Back button = `‹` + previous title. Right-side action buttons |
| CTAs | Blue tinted text (system blue) for actions. Destructive = red. Toggle switches for on/off |
| Detail page | Large icon + title + subtitle at top. "Get/Install" pill button. Horizontal preview carousel. Info table (key-value rows with hairline separators) |
| Density | Medium-high — compact rows (~44pt) with left icon, title, right accessory |
| Dividers | Inset hairlines (left-aligned to text, not full-width) |

**Key pattern — Letter Avatar**: When custom icons aren't available, use a colored square with the first letter of the item name in white. Assign colors by category.

**Anti-patterns to avoid**: Gradients on cards. Full-bleed hero images. Custom fonts replacing system type.

---

## Apps / Card Grid Style

**Reference**: [chatgpt.com/gpts](https://chatgpt.com/gpts) (desktop grid view), App Store "Today" tab

**Figma templates** (Claw Redesign file):
- `5A. Skill Market (Apps Style)` — node `45795:1195` (402×874)
- `5B. My Skills (Apps Style)` — node `45800:1206` (402×874)
- `5C. Skill Detail Modal` — node `45808:1266` (402×874)

**Core feel**: Visual, browsable, discovery-oriented. Items presented as equal-weight cards in a grid.

| Dimension | Pattern |
|---|---|
| Layout | 2-column card grid, each card roughly square or 3:4 ratio |
| Color | White cards on light gray page background. Category-colored icon circles |
| Typography | Card title (medium 14-15px) + subtitle (regular 12px, gray). Minimal text per card |
| Icons | Prominent — colored circle or rounded square with glyph/letter, placed top of card or inline left |
| Cards | Equal-sized, uniform cornerRadius (~16), subtle shadow or border. Tap → modal or push detail |
| Navigation | Segmented control or pill tabs at top (e.g. "Explore / My Skills") |
| CTAs | Inside detail modal: "Install" pill button near title |
| Density | Medium — 2 cards per row, 4-6 visible without scrolling |

**Key pattern — Card as entry point**: Each skill/GPT is a self-contained card with icon + title + one-line description. The grid layout encourages browsing; the detail lives in a modal overlay rather than a full page push.

**When to use over ChatGPT style**: When items have distinct visual identities (icons, colors) and the user benefits from scanning many items at once. Less suitable when items are text-heavy or when one item should be highlighted above others.

---

## Linear Style

**Core feel**: Engineering-grade, dark-mode-first, keyboard-driven. Precision and speed.

| Dimension | Pattern |
|---|---|
| Layout | Sidebar (collapsible) + main content. Tight spacing, high information density |
| Color | Dark gray backgrounds (#1a1a1a–#2a2a2a). Subtle purple/blue accents. White text |
| Typography | Inter or similar geometric sans. Small sizes (13-14px body). Monospace for IDs/codes |
| Icons | Outline-style, 16px, muted gray. Colorized only for status (green = done, yellow = in progress) |
| Cards | Minimal — content in flat rows with hover highlights |
| Navigation | Sidebar with icon + label. Command palette (⌘K) as primary nav. Breadcrumbs in header |
| CTAs | Small, contained buttons. Primary = subtle fill. Ghost buttons common |
| Density | Very high — maximize information per viewport |
| Motion | Quick, physics-based transitions. No bouncy or playful motion |

---

## Notion Style

**Core feel**: Document-centric, flexible, block-based. Clean but customizable.

| Dimension | Pattern |
|---|---|
| Layout | Left sidebar (page tree) + center-aligned content column (max-width ~720px) |
| Color | Light: warm white (#ffffff) with light gray accents. Icons use muted category colors |
| Typography | System default or serif option. Title = large bold. Body = 16px regular. Generous line-height (~1.6) |
| Icons | Emoji or simple outlined glyphs as page icons. Colored backgrounds rare |
| Cards | Gallery view = image + title cards in grid. List view = flat rows. Board view = kanban columns |
| Navigation | Breadcrumb trail. `/` command for block insertion. Hover-to-reveal actions |
| CTAs | Subtle — text buttons ("New page", "+ Add") rather than prominent filled buttons |
| Density | Medium — generous paragraph spacing, wide margins |

---

## Adding New Styles

To extend this catalog, add a new `## Style Name` section with:
1. **Reference** — product URL or Figma community link
2. **Figma templates** — node IDs of implemented frames in the master file (if available)
3. **Core feel** (one sentence)
4. **Dimension table** (layout, color, typography, icons, cards, navigation, CTAs, density, motion)
5. **Key pattern** (the signature element)
6. **Anti-patterns** (what NOT to do)
7. *(Optional)* Fine-grained specs (anatomy diagrams, color palette, spacing system, typography scale, implementation lessons) — add these after real production use, not speculatively

When implementing a new style, add the resulting Figma frames to the **Master Reference File** table at the top of this document.
