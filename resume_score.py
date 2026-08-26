def calculate_resume_score(resume_text, detected_skills):
    """
    Calculates a simple resume score based on
    different resume sections.
    """

    score = 0

    # ---------- Skills ----------
    skill_score = min(len(detected_skills), 15) * 2
    score += skill_score

    # ---------- Experience ----------
    if "experience" in resume_text.lower():
        experience_score = 20
    else:
        experience_score = 0

    score += experience_score

    # ---------- Education ----------
    if "education" in resume_text.lower():
        education_score = 15
    else:
        education_score = 0

    score += education_score

    # ---------- Projects ----------
    if "project" in resume_text.lower():
        project_score = 15
    else:
        project_score = 0

    score += project_score

    # ---------- Certifications ----------
    if "certification" in resume_text.lower():
        certification_score = 10
    else:
        certification_score = 0

    score += certification_score

    # Maximum score is 90
    if score > 90:
        score = 90

    return {
        "Overall Score": score,
        "Skill Score": skill_score,
        "Experience Score": experience_score,
        "Education Score": education_score,
        "Project Score": project_score,
        "Certification Score": certification_score
    }