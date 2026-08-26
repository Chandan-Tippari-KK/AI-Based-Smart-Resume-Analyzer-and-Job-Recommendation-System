def analyze_skill_gap(skills, career):

    required_skills = {

        "AI Engineer": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "LLM",
            "LangChain",
            "Vector Databases",
            "RAG"
        ],

        "Backend Developer": [
            ".NET Core",
            "ASP.NET Core",
            "SQL Server",
            "REST API",
            "Entity Framework Core",
            "Docker",
            "Azure"
        ],

        "Frontend Developer": [
            "Angular",
            "JavaScript",
            "TypeScript",
            "HTML",
            "CSS",
            "React"
        ],

        "Cloud Engineer": [
            "AWS",
            "Docker",
            "Kubernetes",
            "Terraform",
            "Jenkins"
        ]
    }

    required = required_skills.get(career, [])

    existing = []

    missing = []

    for skill in required:

        if skill in skills:
            existing.append(skill)
        else:
            missing.append(skill)

    completion = 0

    if len(required) > 0:
        completion = round(len(existing) / len(required) * 100)

    return {

        "Existing": existing,

        "Missing": missing,

        "Completion": completion

    }