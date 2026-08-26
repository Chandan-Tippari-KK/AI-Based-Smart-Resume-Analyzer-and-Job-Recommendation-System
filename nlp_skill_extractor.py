import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")


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
    "LLM"
]


def extract_skills_nlp(resume_text):
    """
    Extracts skills using token-based NLP matching.
    """

    doc = nlp(resume_text)

    # Convert the resume into lowercase tokens
    tokens = {token.text.lower() for token in doc}

    detected_skills = []

    for skill in SKILLS:

        # Single-word skills
        if " " not in skill:
            if skill.lower() in tokens:
                detected_skills.append(skill)

        # Multi-word skills
        else:
            if skill.lower() in resume_text.lower():
                detected_skills.append(skill)

    return detected_skills