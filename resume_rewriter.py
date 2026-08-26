def rewrite_resume(resume_text):

    rewritten = resume_text

    replacements = {

        "worked on": "Developed and maintained",

        "made": "Designed and implemented",

        "used": "Utilized",

        "good knowledge": "Strong understanding",

        "responsible for": "Successfully managed",

        "helped": "Contributed to",

        "created": "Engineered",

        "project": "software solution"
    }

    rewritten_lower = rewritten.lower()

    for old, new in replacements.items():
        rewritten_lower = rewritten_lower.replace(old, new)

    return rewritten_lower