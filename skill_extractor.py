
import re

# List of predefined technical skills
SKILLS_DATABASE = [
    "Python",
    "Java",
    "C#",
    "JavaScript",
    "TypeScript",
    "SQL",
    "ASP.NET Core",
    "Angular",
    "Next.js",
    "Node.js",
    "REST API",
    "Entity Framework Core",
    "SQL Server",
    "PostgreSQL",
    "AWS",
    "Docker",
    "Kubernetes",
    "Jenkins",
    "Terraform",
    "Ansible",
    "Git",
    "GitHub",
    "Azure DevOps",
    "Prometheus",
    "Grafana",
    "Prompt Engineering",
    "RAG",
    "LangChain",
    "LangGraph",
    "CrewAI",
    "AI Automation",
    "Agentic AI",
    "LLM",
    "Machine Learning",
]


def skill_pattern(skill):
    """Build a case-insensitive pattern for a complete skill name."""
    escaped_skill = re.escape(skill)
    escaped_skill = escaped_skill.replace(r"\ ", r"\s+")

    return re.compile(
        rf"(?<![A-Za-z0-9_]){escaped_skill}(?![A-Za-z0-9_])",
        re.IGNORECASE,
    )


def extract_skills(resume_text):
    """Extract predefined skills without matching partial words."""
    if not isinstance(resume_text, str) or not resume_text.strip():
        return []

    found_skills = []

    for skill in SKILLS_DATABASE:
        if skill_pattern(skill).search(resume_text):
            found_skills.append(skill)

    return found_skills
