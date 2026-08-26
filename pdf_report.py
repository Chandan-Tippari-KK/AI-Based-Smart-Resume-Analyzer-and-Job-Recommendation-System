from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_pdf_report(
        filename,
        skills,
        categorized_skills,
        ml_jobs,
        resume_score,
        ats_score,
        suggestions,
        interview_questions,
        rewritten_resume,
        career_recommendation,
        career_roadmap,
        resume_rank,
        skill_gap,
        learning_path,
        strength_analysis,
        output_path):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(output_path)

    story = []

    story.append(
        Paragraph("<b>AI-Based Smart Resume Analyzer Report</b>",
                  styles["Title"])
    )

    story.append(
        Paragraph(f"<b>Resume:</b> {filename}",
                  styles["Normal"])
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Resume Score</b>",
                  styles["Heading2"])
    )

    for key, value in resume_score.items():

        story.append(
            Paragraph(f"{key}: {value}",
                      styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>ATS Score</b>",
                  styles["Heading2"])
    )

    story.append(
        Paragraph(
            f"{ats_score['ATS Score']}/100",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Detected Skills</b>",
                  styles["Heading2"])
    )

    for skill in skills:

        story.append(
            Paragraph(f"• {skill}",
                      styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Recommended Jobs</b>",
                  styles["Heading2"])
    )

    for job, score in ml_jobs.items():

        story.append(
            Paragraph(
                f"{job} : {score:.2f}%",
                styles["Normal"]
            )
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Suggestions</b>",
                  styles["Heading2"])
    )

    for suggestion in suggestions:

        story.append(
            Paragraph(f"• {suggestion}",
                      styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    # Resume Rank
    story.append(
        Paragraph("<b>Resume Rank</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            f"Rank : {resume_rank['Rank']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            resume_rank["Message"],
            styles["Normal"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    # Skill Categories

    story.append(
        Paragraph("<b>Skill Categories</b>", styles["Heading2"])
    )

    for category, skill_list in categorized_skills.items():

        # Print category name
        story.append(
            Paragraph(f"<b>{category}</b>", styles["Heading3"])
        )

        # Print every skill inside that category
        for skill in skill_list:

            story.append(
                Paragraph(f"• {skill}", styles["Normal"])
            )

        story.append(
            Paragraph("<br/>", styles["Normal"])
        )

    # Interview Questions

    story.append(
        Paragraph("<b>Interview Questions</b>", styles["Heading2"])
    )

    for question in interview_questions:

        story.append(
            Paragraph(f"• {question}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    # AI Resume Rewriter

    story.append(
        Paragraph("<b>AI Resume Rewriter</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            rewritten_resume.replace("\n", "<br/>"),
            styles["Normal"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    # Career Recommendation

    story.append(
        Paragraph("<b>Career Recommendation</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            f"<b>Recommended Career:</b> {career_recommendation['Career']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Missing Skills</b>", styles["Heading3"])
    )

    for skill in career_recommendation["Missing Skills"]:

        story.append(
            Paragraph(f"• {skill}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Recommended Certifications</b>", styles["Heading3"])
    )

    for cert in career_recommendation["Certifications"]:

        story.append(
            Paragraph(f"• {cert}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Learning Platforms</b>", styles["Heading3"])
    )

    for platform in career_recommendation["Learning Platforms"]:

        story.append(
            Paragraph(f"• {platform}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph(
            f"<b>Expected Salary:</b> {career_recommendation['Salary']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )


    # Career Roadmap

    story.append(
        Paragraph("<b>Career Roadmap</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            f"<b>Target Career:</b> {career_roadmap['Career']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Skills to Learn</b>", styles["Heading3"])
    )

    for skill in career_roadmap["Missing Skills"]:

        story.append(
            Paragraph(f"• {skill}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Recommended Certifications</b>", styles["Heading3"])
    )

    for cert in career_roadmap["Certifications"]:

        story.append(
            Paragraph(f"• {cert}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Learning Platforms</b>", styles["Heading3"])
    )

    for platform in career_roadmap["Learning Platforms"]:

        story.append(
            Paragraph(f"• {platform}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph(
            f"<b>Expected Salary:</b> {career_roadmap['Salary']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Estimated Learning Duration:</b> {career_roadmap['Duration']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    # Skill Gap Analysis

    story.append(
        Paragraph("<b>Skill Gap Analysis</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            f"<b>Skill Completion:</b> {skill_gap['Completion']}%",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Existing Skills</b>", styles["Heading3"])
    )

    for skill in skill_gap["Existing"]:

        story.append(
            Paragraph(f"• {skill}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Missing Skills</b>", styles["Heading3"])
    )

    for skill in skill_gap["Missing"]:

        story.append(
            Paragraph(f"• {skill}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    # Learning Path

    story.append(
        Paragraph("<b>Learning Path</b>", styles["Heading2"])
    )

    for step in learning_path:

        story.append(
            Paragraph(f"• {step}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    # Resume Strength & Weakness Analysis

    story.append(
        Paragraph("<b>Resume Strength & Weakness Analysis</b>", styles["Heading2"])
    )

    story.append(
        Paragraph("<b>Strengths</b>", styles["Heading3"])
    )

    for strength in strength_analysis["Strengths"]:

        story.append(
            Paragraph(f"• {strength}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Weaknesses</b>", styles["Heading3"])
    )

    for weakness in strength_analysis["Weaknesses"]:

        story.append(
            Paragraph(f"• {weakness}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph(
            "Generated On : "
            + datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            styles["Italic"]
        )
    )

    doc.build(story)

    return output_path