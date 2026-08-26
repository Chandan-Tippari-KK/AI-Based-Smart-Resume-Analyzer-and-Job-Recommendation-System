JOB_DATABASE = {

    "Backend Developer": [
        "C#",
        "ASP.NET Core",
        "SQL",
        "SQL Server",
        "REST API"
    ],

    "Full Stack Developer": [
        "Angular",
        "JavaScript",
        "TypeScript",
        "Node.js",
        "SQL"
    ],

    "Cloud Engineer": [
        "AWS",
        "Docker",
        "Kubernetes",
        "Terraform"
    ],

    "AI Engineer": [
        "Python",
        "Prompt Engineering",
        "LLM",
        "LangChain",
        "RAG"
    ],

    "Agentic AI Engineer": [
        "Agentic AI",
        "LangChain",
        "LangGraph",
        "CrewAI",
        "AI Automation"
    ]
}


def recommend_jobs(skills):

    recommendations = []

    for job, required_skills in JOB_DATABASE.items():

        matched_skills = 0

        for skill in required_skills:

            if skill in skills:
                matched_skills += 1

        match_percentage = (
            matched_skills / len(required_skills)
        ) * 100

        recommendations.append(
            (job, round(match_percentage, 2))
        )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations