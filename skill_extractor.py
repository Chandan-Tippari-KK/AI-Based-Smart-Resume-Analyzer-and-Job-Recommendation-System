# List of predefined skills

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
    "Machine Learning"
]


def extract_skills(resume_text):

    found_skills = []

    resume_text_lower = resume_text.lower()

    for skill in SKILLS_DATABASE:

        if skill.lower() in resume_text_lower:
            found_skills.append(skill)

    return found_skills