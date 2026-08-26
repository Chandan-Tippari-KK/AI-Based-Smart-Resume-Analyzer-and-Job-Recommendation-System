from resume_parser import extract_text_from_pdf
from nlp_skill_extractor import extract_skills_nlp

# Resume file name
pdf_file = "sample_resume.pdf"

# Extract text from the resume
resume_text = extract_text_from_pdf(pdf_file)

print("\n===== RESUME TEXT =====\n")
print(resume_text)

# Extract skills using the NLP-based extractor
skills = extract_skills_nlp(resume_text)

print("\n===== NLP DETECTED SKILLS =====\n")

for skill in skills:
    print(skill)