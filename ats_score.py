def calculate_ats_score(resume_text, detected_skills):
    """
    Calculates ATS Score based on resume quality.
    """

    score = 0
    missing = []

    resume_lower = resume_text.lower()

    # -----------------------------
    # Contact Information
    # -----------------------------
    if "@" in resume_text:
        score += 5
    else:
        missing.append("Email Address")

    # -----------------------------
    # LinkedIn
    # -----------------------------
    if "linkedin" in resume_lower:
        score += 5
    else:
        missing.append("LinkedIn Profile")

    # -----------------------------
    # GitHub
    # -----------------------------
    if "github" in resume_lower:
        score += 5
    else:
        missing.append("GitHub Profile")

    # -----------------------------
    # Skills
    # -----------------------------
    skill_score = min(len(detected_skills), 20)

    score += skill_score

    if skill_score < 15:
        missing.append("More Technical Skills")

    # -----------------------------
    # Experience
    # -----------------------------
    if "experience" in resume_lower:
        score += 15
    else:
        missing.append("Work Experience")

    # -----------------------------
    # Education
    # -----------------------------
    if "education" in resume_lower:
        score += 10
    else:
        missing.append("Education")

    # -----------------------------
    # Projects
    # -----------------------------
    if "project" in resume_lower:
        score += 10
    else:
        missing.append("Projects")

    # -----------------------------
    # Certifications
    # -----------------------------
    if "certification" in resume_lower:
        score += 10
    else:
        missing.append("Certifications")

    # -----------------------------
    # Achievements
    # -----------------------------
    achievement_words = [
        "%",
        "improved",
        "reduced",
        "increased",
        "optimized",
        "saved"
    ]

    if any(word in resume_lower for word in achievement_words):
        score += 10
    else:
        missing.append("Quantified Achievements")

    # -----------------------------
    # Limit score to 100
    # -----------------------------
    score = min(score, 100)

    return {
        "ATS Score": score,
        "Missing": missing
    }