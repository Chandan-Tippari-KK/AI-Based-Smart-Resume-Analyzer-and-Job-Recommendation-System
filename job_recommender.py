
JOB_DATABASE = {
    "Backend Developer": [
        "C#", "ASP.NET Core", "SQL", "SQL Server", "REST API"
    ],
    "Full Stack Developer": [
        "Angular", "JavaScript", "TypeScript", "Node.js", "SQL"
    ],
    "Cloud Engineer": [
        "AWS", "Docker", "Kubernetes", "Terraform"
    ],
    "AI Engineer": [
        "Python", "Prompt Engineering", "LLM", "LangChain", "RAG"
    ],
    "Agentic AI Engineer": [
        "Agentic AI", "LangChain", "LangGraph",
        "CrewAI", "AI Automation"
    ]
}


def normalize_skill(skill):
    """Normalize whitespace and case for skill comparisons."""
    return " ".join(str(skill).strip().lower().split())


def recommend_jobs(skills):
    """
    Return job matches with matched skills, missing skills,
    and transparent rule-based match percentages.
    """
    detected_skills = {
        normalize_skill(skill)
        for skill in skills
        if str(skill).strip()
    }

    recommendations = []

    for job, required_skills in JOB_DATABASE.items():
        matched_skills = [
            skill for skill in required_skills
            if normalize_skill(skill) in detected_skills
        ]

        missing_skills = [
            skill for skill in required_skills
            if normalize_skill(skill) not in detected_skills
        ]

        match_percentage = (
            len(matched_skills) / len(required_skills) * 100
            if required_skills else 0.0
        )

        recommendations.append({
            "job": job,
            "match_percentage": round(match_percentage, 2),
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
        })

    recommendations.sort(
        key=lambda item: item["match_percentage"],
        reverse=True
    )

    return recommendations
