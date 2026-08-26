from resume_parser import extract_text_from_pdf
from nlp_skill_extractor import extract_skills_nlp
from ats_score import calculate_ats_score

resume = extract_text_from_pdf("resume.pdf")

skills = extract_skills_nlp(resume)

ats = calculate_ats_score(resume, skills)

print()

print("========== ATS REPORT ==========")

print()

print("ATS Score :", ats["ATS Score"])

print()

print("Missing Sections")

for item in ats["Missing"]:
    print("-", item)

print()

print("===============================")