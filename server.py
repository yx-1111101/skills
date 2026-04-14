#!/usr/bin/env python3
"""MCP server that exposes skills as tools and resources."""

from pathlib import Path
import yaml
from mcp.server.fastmcp import FastMCP

BASE_DIR = Path(__file__).parent

mcp = FastMCP(
    "skills",
    instructions="Provides structured analysis skills as callable tools. "
                 "Use list_skills to see available skills, get_skill_instructions to load a skill's framework, "
                 "and get_skill_reference to load a skill's reference documents.",
)


def _parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from markdown content."""
    if content.startswith("---\n"):
        parts = content.split("---\n", 2)
        if len(parts) == 3:
            meta = yaml.safe_load(parts[1]) or {}
            return meta, parts[2].strip()
    return {}, content.strip()


def _discover_skills() -> dict:
    """Auto-discover all skill directories containing a SKILL.md file."""
    skills = {}
    for path in sorted(BASE_DIR.iterdir()):
        if path.is_dir() and not path.name.startswith("."):
            skill_md = path / "SKILL.md"
            if skill_md.exists():
                content = skill_md.read_text(encoding="utf-8")
                meta, body = _parse_frontmatter(content)
                skills[path.name] = {
                    "name": meta.get("name", path.name),
                    "description": meta.get("description", ""),
                    "instructions": body,
                    "path": path,
                }
    return skills


SKILLS = _discover_skills()


@mcp.tool()
def list_skills() -> str:
    """List all available skills with their IDs and descriptions."""
    if not SKILLS:
        return "No skills found."
    lines = []
    for skill_id, skill in SKILLS.items():
        lines.append(f"- `{skill_id}`: {skill['description'][:200]}")
    return "\n".join(lines)


@mcp.tool()
def get_skill_instructions(skill_id: str) -> str:
    """Get the full instruction framework for a specific skill.

    Args:
        skill_id: The skill directory name, e.g. 'analyze-company-product' or 'decode-paper'.
                  Use list_skills to see all available IDs.
    """
    if skill_id not in SKILLS:
        available = ", ".join(f"`{k}`" for k in SKILLS)
        return f"Unknown skill '{skill_id}'. Available skills: {available}"
    return SKILLS[skill_id]["instructions"]


@mcp.tool()
def get_skill_reference(skill_id: str, filename: str) -> str:
    """Get a reference document for a specific skill.

    Args:
        skill_id: The skill directory name (use list_skills to see available IDs).
        filename: Reference filename without .md extension, e.g. 'analysis-templates'.
    """
    if skill_id not in SKILLS:
        available = ", ".join(f"`{k}`" for k in SKILLS)
        return f"Unknown skill '{skill_id}'. Available skills: {available}"

    refs_dir = SKILLS[skill_id]["path"] / "references"
    if not refs_dir.exists():
        return f"Skill '{skill_id}' has no reference documents."

    for candidate in [refs_dir / f"{filename}.md", refs_dir / filename]:
        if candidate.exists():
            return candidate.read_text(encoding="utf-8")

    available_refs = sorted(p.stem for p in refs_dir.glob("*.md"))
    return (
        f"Reference '{filename}' not found in skill '{skill_id}'. "
        f"Available references: {', '.join(available_refs) or 'none'}"
    )


# Expose skills and reference files as MCP resources via URI templates.

@mcp.resource("skill://{skill_id}/instructions")
def get_skill_resource(skill_id: str) -> str:
    """Retrieve the full instruction framework for a skill."""
    if skill_id not in SKILLS:
        return f"Unknown skill '{skill_id}'. Available: {', '.join(SKILLS)}"
    return SKILLS[skill_id]["instructions"]


@mcp.resource("skill://{skill_id}/references/{ref_name}")
def get_skill_ref_resource(skill_id: str, ref_name: str) -> str:
    """Retrieve a reference document for a skill."""
    if skill_id not in SKILLS:
        return f"Unknown skill '{skill_id}'. Available: {', '.join(SKILLS)}"
    refs_dir = SKILLS[skill_id]["path"] / "references"
    ref_file = refs_dir / f"{ref_name}.md"
    if not ref_file.exists():
        available = sorted(p.stem for p in refs_dir.glob("*.md")) if refs_dir.exists() else []
        return f"Reference '{ref_name}' not found. Available: {', '.join(available) or 'none'}"
    return ref_file.read_text(encoding="utf-8")


if __name__ == "__main__":
    mcp.run()
