def analyze_resume_strength(skills, resume_score, ats_score):

    strengths = []
    weaknesses = []

    # Skills

    if len(skills) >= 20:
        strengths.append("Strong technical skill set.")
    else:
        weaknesses.append("Add more technical skills.")

    # Resume Score

    if resume_score["Overall Score"] >= 80:
        strengths.append("Excellent resume quality.")
    else:
        weaknesses.append("Improve resume quality.")

    # ATS Score

    if ats_score["ATS Score"] >= 80:
        strengths.append("ATS-friendly resume.")
    else:
        weaknesses.append("Improve ATS compatibility.")

    # AI Skills

    ai_skills = [
        "Python",
        "LLM",
        "LangChain",
        "Agentic AI",
        "Prompt Engineering"
    ]

    count = 0

    for skill in ai_skills:
        if skill in skills:
            count += 1

    if count >= 3:
        strengths.append("Good AI skillset.")
    else:
        weaknesses.append("Improve AI-related skills.")

    # Cloud

    if "AWS" in skills:
        strengths.append("Cloud knowledge detected.")
    else:
        weaknesses.append("Cloud certification recommended.")

    return {
        "Strengths": strengths,
        "Weaknesses": weaknesses
    }