from resume_parser import extract_text_from_pdf
from ml_job_matcher import recommend_jobs_ml

# Resume PDF file
pdf_file = "sample_resume.pdf"

# Extract resume text
resume_text = extract_text_from_pdf(pdf_file)

print("\n===== RESUME TEXT =====\n")
print(resume_text)

# Get ML-based job recommendations
recommendations = recommend_jobs_ml(resume_text)

print("\n===== MACHINE LEARNING JOB MATCHING =====\n")

# Display the recommendations in descending order
for job, score in sorted(recommendations.items(), key=lambda item: item[1], reverse=True):
    print(f"{job} --> {score}%")