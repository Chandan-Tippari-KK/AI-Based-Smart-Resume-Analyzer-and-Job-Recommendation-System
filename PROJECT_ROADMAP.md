# AI-Based Smart Resume Analyzer and Job Recommendation System

## Project Information

### Project Title
AI-Based Smart Resume Analyzer and Job Recommendation System

### Project Type
Mini Project

### Domain
Artificial Intelligence (AI)
Natural Language Processing (NLP)
Machine Learning

### Developed By
Chandan Tippari K K

### Academic Year
2026

---

# Project Objective

The objective of this project is to develop an intelligent system that can:

- Analyze resumes automatically
- Extract candidate skills
- Identify important keywords
- Match skills with job roles
- Recommend suitable jobs
- Calculate resume-job matching scores
- Reduce manual resume screening effort

---

# Problem Statement

Recruiters often spend significant time manually reviewing resumes to identify suitable candidates.

The traditional resume screening process:

- Is time-consuming
- Is prone to human errors
- May overlook qualified candidates
- Becomes difficult when handling large numbers of resumes

This project aims to automate resume analysis and provide intelligent job recommendations using AI and NLP techniques.

---

# Existing System

Current Process:

1. Candidate submits resume
2. Recruiter manually reviews resume
3. Skills are identified manually
4. Job suitability is determined manually

### Limitations

- Time-consuming
- Human bias
- Not scalable
- Error-prone

---

# Proposed System

The proposed system automatically:

1. Reads resumes
2. Extracts text
3. Identifies skills
4. Performs NLP processing
5. Matches skills with jobs
6. Generates recommendations
7. Calculates match percentage

---

# Software Requirements

## Operating System

- Windows 10 / Windows 11

## Programming Language

- Python 3.11+

## IDE

- Visual Studio Code

## Libraries

- Flask
- spaCy
- NLTK
- Scikit-learn
- PDFPlumber
- Python-docx

---

# Installation Commands

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

```bash
venv\Scripts\activate
```

## Install Required Packages

```bash
pip install flask spacy nltk scikit-learn pdfplumber python-docx
```

## Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

## Verify spaCy

```python
import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Resume Analyzer")

for token in doc:
    print(token.text)
```

---

# Project Folder Structure

```text
resume-analyzer-project
│
├── venv
│
├── sample_resume.pdf
│
├── resume_parser.py
│
├── skill_extractor.py
│
├── test_skill_extractor.py
│
├── job_recommender.py
│
├── test_job_recommender.py
│
└── PROJECT_ROADMAP.md
```

---

# Phase 1 - Environment Setup

Status: COMPLETED

### Tasks Completed

- Python Installed
- VS Code Installed
- Virtual Environment Created
- Required Packages Installed
- spaCy Installed
- NLP Model Installed

---

# Phase 2 - Resume Parsing Module

Status: COMPLETED

File:

```text
resume_parser.py
```

### Responsibilities

- Read PDF files
- Read DOCX files
- Extract resume text

### Functions

```python
extract_text_from_pdf()
```

```python
extract_text_from_docx()
```

### Testing Result

SUCCESS

Resume text extracted successfully.

---

# Phase 3 - Skill Extraction Module

Status: COMPLETED

File:

```text
skill_extractor.py
```

### Responsibilities

- Detect skills from resume
- Compare resume text against skill database

### Function

```python
extract_skills()
```

### Skills Currently Supported

- Python
- C#
- SQL
- AWS
- Docker
- Kubernetes
- Angular
- ASP.NET Core
- LangChain
- CrewAI
- Agentic AI
- etc.

### Testing Result

SUCCESS

Skills detected successfully.

---

# Phase 4 - Job Recommendation Module

Status: COMPLETED

File:

```text
job_recommender.py
```

### Responsibilities

- Compare skills against job profiles
- Generate matching scores
- Recommend jobs

### Function

```python
recommend_jobs()
```

### Current Jobs Supported

- Backend Developer
- Full Stack Developer
- Cloud Engineer
- AI Engineer
- Agentic AI Engineer

### Testing Result

SUCCESS

Job recommendations generated successfully.

---

# Current Output

Detected Skills:

- Python
- C#
- SQL
- Angular
- ASP.NET Core
- AWS
- Docker
- Kubernetes
- Terraform
- LangChain
- LangGraph
- CrewAI
- Agentic AI
- LLM
- etc.

Recommended Jobs:

- Backend Developer
- Full Stack Developer
- Cloud Engineer
- AI Engineer
- Agentic AI Engineer

---

# Phase 5 - NLP Enhancement

Status: IN PROGRESS

### Goal

Improve skill extraction accuracy.

### Tasks

- Remove false positives
- Use Named Entity Recognition
- Use NLP tokenization
- Improve keyword matching

### Example

Current Issue:

Java detected from JavaScript.

Future Solution:

Exact NLP-based skill detection.

---

# Phase 6 - Machine Learning Based Matching

Status: COMPLETED

### Goal

Use Machine Learning to compare resumes and job descriptions.

### Technologies

- TF-IDF
- Cosine Similarity
- Scikit-learn

### Output Example

Agentic AI Engineer → 95%

AI Engineer → 88%

Backend Developer → 82%

Cloud Engineer → 76%

---

# Phase 7 - Resume Score Generator

Status: COMPLETED

### Goal

Generate overall resume quality score.

### Example

Resume Score:

```text
87 / 100
```

Evaluation Areas:

- Skills
- Experience
- Education
- Certifications
- Projects

---

# Phase 8 - Resume Improvement Suggestions

Status: COMPLETED

### Goal

Suggest improvements.

Example:

```text
Add more AI projects

Add GitHub links

Add certifications

Add measurable achievements
```

---

# Phase 9 - Flask Web Application

Status: PENDING

### Goal

Create a web interface.

Features:

- Upload Resume
- View Skills
- View Match Score
- View Job Recommendations

Files To Create:

```text
app.py

templates/
    index.html

static/
    style.css
```

---

# Phase 10 - Final Project Completion

Status: PENDING

### Deliverables

- Source Code
- Documentation
- Synopsis
- PPT
- Project Report
- Demonstration

---

# Mini Project Synopsis Sections

The synopsis should contain:

1. Title
2. Introduction
3. Problem Statement
4. Objectives
5. Existing System
6. Proposed System
7. Methodology
8. Technologies Used
9. Modules
10. Expected Outcomes
11. Future Scope
12. References

---

# Testing Log

## Test 1

File:

```text
resume_parser.py
```

Result:

PASS

---

## Test 2

File:

```text
test_skill_extractor.py
```

Result:

PASS

---

## Test 3

File:

```text
test_job_recommender.py
```

Result:

PASS

Output:

All job recommendations generated successfully.

---

# Future Enhancements

- Deep Learning Models
- Resume Ranking System
- ATS Compatibility Analysis
- Interview Question Generator
- AI Career Guidance
- Job Portal Integration
- LinkedIn Integration
- Multi-language Resume Analysis

---

# Project Status

Overall Progress:

```text
40% Completed
```

Completed:

- Environment Setup
- Resume Parsing
- Skill Extraction
- Job Recommendation

Pending:

- NLP Enhancement
- Machine Learning Matching
- Resume Scoring
- Resume Suggestions
- Flask Web Application
- Final Deployment

---

# Last Updated

Date: June 2026

Project Owner:
Chandan Tippari K K

Project:
AI-Based Smart Resume Analyzer and Job Recommendation System