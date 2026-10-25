
import re

# List of technical skills
SKILLS = [
    "Python",
    "Java",
    "C#",
    "JavaScript",
    "TypeScript",
    "SQL",
    "ASP.NET Core",
    ".NET Core",
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
]


def skill_pattern(skill):
    """Match a complete skill name, ignoring capitalization."""
    escaped_skill = re.escape(skill)
    escaped_skill = escaped_skill.replace(r"\ ", r"\s+")

    return re.compile(
        rf"(?<![A-Za-z0-9_]){escaped_skill}(?![A-Za-z0-9_])",
        re.IGNORECASE,
    )


def extract_skills_nlp(resume_text):
    """
    Extract technical skills using case-insensitive,
    complete-term matching.
    """
    if not isinstance(resume_text, str) or not resume_text.strip():
        return []

    detected_skills = []

    for skill in SKILLS:
        if skill_pattern(skill).search(resume_text):
            detected_skills.append(skill)

    return detected_skills
