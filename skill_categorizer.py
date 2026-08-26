def categorize_skills(detected_skills):
    """
    Categorizes detected skills into different domains.
    """

    categories = {

        "Programming Languages": [
            "Python",
            "Java",
            "C",
            "C++",
            "C#",
            "JavaScript",
            "TypeScript",
            "SQL"
        ],

        "Frontend": [
            "HTML",
            "CSS",
            "Bootstrap",
            "Angular",
            "React",
            "Next.js"
        ],

        "Backend": [
            "ASP.NET Core",
            ".NET Core",
            "Node.js",
            "REST API",
            "Entity Framework Core"
        ],

        "Database": [
            "SQL Server",
            "MySQL",
            "PostgreSQL",
            "MongoDB"
        ],

        "Cloud": [
            "AWS",
            "Azure",
            "Google Cloud"
        ],

        "DevOps": [
            "Docker",
            "Kubernetes",
            "Jenkins",
            "Terraform",
            "Ansible",
            "Azure DevOps",
            "Git",
            "GitHub",
            "Prometheus",
            "Grafana"
        ],

        "Artificial Intelligence": [
            "Machine Learning",
            "Deep Learning",
            "NLP",
            "LLM",
            "Prompt Engineering",
            "RAG",
            "LangChain",
            "LangGraph",
            "CrewAI",
            "AI Automation",
            "Agentic AI"
        ]

    }

    categorized = {}

    for category, skills in categories.items():

        matched = []

        for skill in skills:

            if skill in detected_skills:
                matched.append(skill)

        if matched:
            categorized[category] = matched

    return categorized