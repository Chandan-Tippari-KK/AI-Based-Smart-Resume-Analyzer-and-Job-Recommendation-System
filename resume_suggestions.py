def generate_resume_suggestions(resume_text, detected_skills):
    """
    Generates improvement suggestions based on the resume content.
    """

    suggestions = []

    # Check for GitHub
    if "github" not in resume_text.lower():
        suggestions.append("Add your GitHub profile link.")

    # Check for LinkedIn
    if "linkedin" not in resume_text.lower():
        suggestions.append("Add your LinkedIn profile link.")

    # Check for Projects
    if "project" not in resume_text.lower():
        suggestions.append("Include at least one project.")

    # Check for Certifications
    if "certification" not in resume_text.lower():
        suggestions.append("Add relevant certifications.")

    # Check for AI Skills
    ai_skills = [
        "Python",
        "Machine Learning",
        "NLP",
        "LLM",
        "LangChain",
        "Agentic AI"
    ]

    missing_ai_skills = []

    for skill in ai_skills:
        if skill not in detected_skills:
            missing_ai_skills.append(skill)

    if len(missing_ai_skills) > 0:
        suggestions.append(
            "Consider learning: " +
            ", ".join(missing_ai_skills)
        )

    # Check for measurable achievements
    if "%" not in resume_text and "improved" not in resume_text.lower():
        suggestions.append(
            "Add measurable achievements (e.g., Improved performance by 30%)."
        )

    # If everything looks good
    if len(suggestions) == 0:
        suggestions.append("Excellent resume! No major suggestions.")

    return suggestions