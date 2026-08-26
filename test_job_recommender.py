from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from job_recommender import recommend_jobs


# Resume file
pdf_file = "sample_resume.pdf"


# Extract resume text
resume_text = extract_text_from_pdf(pdf_file)


# Extract skills
skills = extract_skills(resume_text)

print("\n===== DETECTED SKILLS =====\n")

for skill in skills:
    print(skill)


# Recommend jobs
recommendations = recommend_jobs(skills)

print("\n===== JOB RECOMMENDATIONS =====\n")

for job, score in recommendations:
    print(f"{job} --> {score}% Match")