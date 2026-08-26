from flask import Flask, render_template, request, redirect, url_for, session, send_file
import os

from resume_parser import extract_text_from_pdf, extract_text_from_docx
from nlp_skill_extractor import extract_skills_nlp
from ml_job_matcher import recommend_jobs_ml
from resume_score import calculate_resume_score
from resume_suggestions import generate_resume_suggestions
from ats_score import calculate_ats_score
from skill_categorizer import categorize_skills
from pdf_report import generate_pdf_report
from interview_questions import generate_interview_questions
from resume_rewriter import rewrite_resume
from career_recommendation import generate_career_recommendation
from career_roadmap import generate_career_roadmap
from resume_strength import analyze_resume_strength
from resume_rank import calculate_resume_rank
from skill_gap_analysis import analyze_skill_gap
from learning_path import generate_learning_path

app = Flask(__name__)

app.secret_key = "resume_analyzer_secret_key"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        uploaded_file = request.files["resume"]

        filename = uploaded_file.filename

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        uploaded_file.save(file_path)

        if filename.lower().endswith(".pdf"):
            resume_text = extract_text_from_pdf(file_path)

        elif filename.lower().endswith(".docx"):
            resume_text = extract_text_from_docx(file_path)

        else:
            return "Unsupported file format."

        skills = extract_skills_nlp(resume_text)

        categorized_skills = categorize_skills(skills)

        ml_jobs = recommend_jobs_ml(resume_text)

        print("\n===== ML JOBS =====")
        print(ml_jobs)
        print(type(ml_jobs))

        resume_score = calculate_resume_score(resume_text, skills)

        ats_score = calculate_ats_score(resume_text, skills)

        suggestions = generate_resume_suggestions(
            resume_text,
            skills
        )

        interview_questions = generate_interview_questions(skills)

        rewritten_resume = rewrite_resume(resume_text)

        career_recommendation = generate_career_recommendation(skills)

        learning_path = generate_learning_path(career_recommendation["Career"])

        skill_gap = analyze_skill_gap(skills, career_recommendation["Career"])

        strength_analysis = analyze_resume_strength(skills, resume_score, ats_score)

        resume_rank = calculate_resume_rank(resume_score, ats_score)

        career_roadmap = generate_career_roadmap(skills)

        session["skills"] = skills

        session["categorized_skills"] = categorized_skills

        session["ml_jobs"] = {
        job: float(score)
        for job, score in ml_jobs.items()
        }

        session["resume_score"] = resume_score

        session["ats_score"] = ats_score

        session["suggestions"] = suggestions

        session["interview_questions"] = interview_questions

        session["rewritten_resume"] = rewritten_resume

        session["career_recommendation"] = career_recommendation

        session["learning_path"] = learning_path

        session["skill_gap"] = skill_gap

        session["strength_analysis"] = strength_analysis

        session["resume_rank"] = resume_rank

        session["career_roadmap"] = career_roadmap

        session["uploaded_file_name"] = filename

        return redirect(url_for("home"))

    return render_template(
    "index.html",
    skills=session.get("skills"),
    categorized_skills=session.get("categorized_skills"),
    ml_jobs=session.get("ml_jobs"),
    resume_score=session.get("resume_score"),
    ats_score=session.get("ats_score"),
    suggestions=session.get("suggestions"),
    interview_questions=session.get("interview_questions"),
    rewritten_resume=session.get("rewritten_resume"),
    career_recommendation=session.get("career_recommendation"),
    learning_path=session.get("learning_path"),
    skill_gap=session.get("skill_gap"),
    strength_analysis=session.get("strength_analysis"),
    resume_rank=session.get("resume_rank"),
    career_roadmap=session.get("career_roadmap"),
    uploaded_file_name=session.get("uploaded_file_name")
    )

@app.route("/clear")
def clear():

    session.clear()

    return redirect(url_for("home"))


@app.route("/download_report")
def download_report():

    if session.get("resume_score") is None:
        return redirect(url_for("home"))

    pdf_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        "Resume_Analysis_Report.pdf"
    )

    generate_pdf_report(
    filename=session.get("uploaded_file_name"),
    skills=session.get("skills"),
    categorized_skills=session.get("categorized_skills"),
    ml_jobs=session.get("ml_jobs"),
    resume_score=session.get("resume_score"),
    ats_score=session.get("ats_score"),
    suggestions=session.get("suggestions"),
    interview_questions=session.get("interview_questions"),
    rewritten_resume=session.get("rewritten_resume"),
    career_recommendation=session.get("career_recommendation"),
    career_roadmap=session.get("career_roadmap"),
    resume_rank=session.get("resume_rank"),
    skill_gap=session.get("skill_gap"),
    learning_path=session.get("learning_path"),
    strength_analysis=session.get("strength_analysis"),
    output_path=pdf_path)

    return send_file(
        pdf_path,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)