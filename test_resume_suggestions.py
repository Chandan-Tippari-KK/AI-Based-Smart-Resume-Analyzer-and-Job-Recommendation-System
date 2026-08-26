from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from resume_suggestions import generate_resume_suggestions

# Resume PDF file
pdf_file = "sample_resume.pdf"

# Extract resume text
resume_text = extract_text_from_pdf(pdf_file)

# Extract detected skills
detected_skills = extract_skills(resume_text)

# Generate suggestions
suggestions = generate_resume_suggestions(
    resume_text,
    detected_skills
)

print("\n========== RESUME IMPROVEMENT SUGGESTIONS ==========\n")

for index, suggestion in enumerate(suggestions, start=1):
    print(f"{index}. {suggestion}")

print("\n===================================================\n")