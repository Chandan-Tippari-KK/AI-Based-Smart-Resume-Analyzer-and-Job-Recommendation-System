from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from resume_score import calculate_resume_score

# Resume PDF file
pdf_file = "sample_resume.pdf"

# Extract resume text
resume_text = extract_text_from_pdf(pdf_file)

# Extract skills
detected_skills = extract_skills(resume_text)

# Calculate resume score
result = calculate_resume_score(resume_text, detected_skills)

print("\n========== RESUME SCORE REPORT ==========\n")

for key, value in result.items():
    print(f"{key}: {value}")

print("\n=========================================\n")