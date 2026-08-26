from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills


# Change this to your resume file name
pdf_file = "sample_resume.pdf"


# Extract text from resume
resume_text = extract_text_from_pdf(pdf_file)

print("\n===== RESUME TEXT =====\n")
print(resume_text)


# Extract skills
skills = extract_skills(resume_text)

print("\n===== DETECTED SKILLS =====\n")

for skill in skills:
    print(skill)