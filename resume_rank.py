def calculate_resume_rank(resume_score, ats_score):

    overall = resume_score["Overall Score"]
    ats = ats_score["ATS Score"]

    average = (overall + ats) / 2

    if average >= 90:
        return {
            "Rank": "🥇 Gold",
            "Color": "gold",
            "Message": "Excellent Resume! Ready for top companies."
        }

    elif average >= 75:
        return {
            "Rank": "🥈 Silver",
            "Color": "silver",
            "Message": "Very Good Resume. A few improvements can make it outstanding."
        }

    elif average >= 60:
        return {
            "Rank": "🥉 Bronze",
            "Color": "#CD7F32",
            "Message": "Good Resume. Needs more improvements."
        }

    else:
        return {
            "Rank": "⭐ Beginner",
            "Color": "#808080",
            "Message": "Start improving your resume by adding projects, skills and certifications."
        }