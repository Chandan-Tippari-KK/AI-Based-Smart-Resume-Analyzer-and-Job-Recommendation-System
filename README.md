# AI-Based Smart Resume Analyzer and Job Recommendation System

An AI-assisted resume analysis and career guidance web application that extracts skills from resumes, evaluates resume quality, calculates ATS-oriented scores, matches resumes against job roles using TF-IDF and cosine similarity, and generates personalized career insights.

## Overview

The **AI-Based Smart Resume Analyzer and Job Recommendation System** is a Python and Flask-based mini project designed to automate several parts of the resume screening and career guidance process.

The application accepts a resume in **PDF or DOCX** format and produces a consolidated analysis including:

- Resume text extraction
- NLP-based technical skill detection
- Skill categorization
- Machine-learning-based job matching
- Resume quality scoring
- ATS-oriented scoring
- Resume improvement suggestions
- Resume strengths and weaknesses
- Resume ranking
- Career recommendation
- Skill-gap analysis
- Personalized learning path
- Career roadmap
- Skill-based interview questions
- Resume rewriting suggestions
- Downloadable PDF analysis report

> **Project Type:** Academic Mini Project  
> **Domain:** Artificial Intelligence, Natural Language Processing, Machine Learning  
> **Academic Year:** 2026

---

## Key Features

### 1. Resume Parsing

Supports:

- PDF resumes
- DOCX resumes

The application extracts textual content using:

- `pdfplumber`
- `python-docx`

### 2. NLP-Based Skill Extraction

The application uses **spaCy** and the `en_core_web_sm` English model to tokenize resume text and detect technical skills from a predefined skill vocabulary.

Examples include:

- Python
- C#
- JavaScript
- TypeScript
- SQL
- ASP.NET Core
- Angular
- AWS
- Docker
- Kubernetes
- Terraform
- LangChain
- LangGraph
- CrewAI
- Agentic AI
- LLM
- RAG
- Machine Learning

### 3. Skill Categorization

Detected skills are grouped into categories such as:

- Programming Languages
- Frontend
- Backend
- Database
- Cloud
- DevOps
- Artificial Intelligence

### 4. Machine Learning Job Matching

The project uses:

- **TF-IDF vectorization**
- **Cosine similarity**
- **scikit-learn**

The extracted resume text is compared against predefined job descriptions for roles including:

- Backend Developer
- Full Stack Developer
- Cloud Engineer
- AI Engineer
- Agentic AI Engineer

The system produces a percentage-based similarity score for each role.

### 5. Resume Score

The application calculates a resume quality score based on detected:

- Technical skills
- Experience
- Education
- Projects
- Certifications

### 6. ATS-Oriented Score

The ATS scoring module checks for resume elements such as:

- Email address
- LinkedIn profile
- GitHub profile
- Technical skills
- Work experience
- Education
- Projects
- Certifications
- Quantified achievements

It also reports missing areas that could improve the resume.

> The current ATS score is a project-specific heuristic score; it is not an official score produced by a commercial ATS platform.

### 7. Resume Improvement Suggestions

The system can identify areas such as:

- Missing GitHub profile
- Missing LinkedIn profile
- Missing projects
- Missing certifications
- Missing AI-related skills
- Lack of measurable achievements

### 8. Career Recommendation

Based on detected skills, the system recommends a career direction and provides:

- Missing skills
- Suggested certifications
- Learning platforms
- Indicative salary information

### 9. Skill-Gap Analysis

The system compares the candidate's detected skills against predefined requirements for selected career paths and calculates a completion percentage.

### 10. Learning Path

The application generates an eight-week learning path based on the recommended career direction.

### 11. Interview Question Generator

Interview questions are generated according to detected technologies and skills, including areas such as:

- Python
- ASP.NET Core
- SQL
- Angular
- Docker
- AWS
- Agentic AI

### 12. Resume Strength Analysis

The application identifies:

- Resume strengths
- Resume weaknesses
- Technical skill coverage
- AI skill coverage
- Cloud skill coverage
- ATS-related improvement areas

### 13. Resume Ranking

A project-specific ranking is calculated from the resume score and ATS score, producing categories such as:

- Gold
- Silver
- Bronze
- Beginner

### 14. Career Roadmap

The system generates a career roadmap containing:

- Target career
- Missing skills
- Suggested certifications
- Learning platforms
- Indicative salary range
- Estimated learning duration

### 15. PDF Report

The project can generate a downloadable PDF analysis report containing the major resume-analysis results.

---

## System Workflow

```text
                    ┌──────────────────────┐
                    │   User Uploads       │
                    │   PDF / DOCX Resume  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Resume Parser      │
                    │ PDFPlumber / DOCX    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ NLP Skill Extraction │
                    │       spaCy          │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
     ┌───────────────┐ ┌───────────────┐ ┌────────────────┐
     │ Skill         │ │ Resume / ATS  │ │ ML Job         │
     │ Categorization│ │ Scoring       │ │ Matching       │
     └───────┬───────┘ └───────┬───────┘ │ TF-IDF +       │
             │                 │         │ Cosine         │
             │                 │         └───────┬────────┘
             └─────────────────┼─────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Career Intelligence  │
                    │                      │
                    │ • Recommendations    │
                    │ • Skill Gap          │
                    │ • Learning Path      │
                    │ • Career Roadmap     │
                    │ • Interview Questions│
                    │ • Suggestions        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Flask Web Dashboard  │
                    │ + PDF Report         │
                    └──────────────────────┘
```

---

## Technology Stack

| Area | Technology |
|---|---|
| Language | Python |
| Web Framework | Flask |
| NLP | spaCy |
| NLP Model | `en_core_web_sm` |
| Machine Learning | scikit-learn |
| Text Similarity | TF-IDF + Cosine Similarity |
| PDF Parsing | pdfplumber |
| DOCX Parsing | python-docx |
| PDF Report Generation | ReportLab |
| Frontend | HTML, CSS, Jinja2 |
| Development IDE | Visual Studio Code |
| Version Control | Git |
| Repository | GitHub |

---

## Project Structure

```text
resume-analyzer-project/
│
├── app.py
│
├── ats_score.py
├── career_recommendation.py
├── career_roadmap.py
├── interview_questions.py
├── job_recommender.py
├── learning_path.py
├── ml_job_matcher.py
├── nlp_skill_extractor.py
├── pdf_report.py
├── resume_parser.py
├── resume_rank.py
├── resume_rewriter.py
├── resume_score.py
├── resume_strength.py
├── resume_suggestions.py
├── skill_categorizer.py
├── skill_extractor.py
├── skill_gap_analysis.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── test_ats_score.py
├── test_job_recommender.py
├── test_ml_job_matcher.py
├── test_nlp_skill_extractor.py
├── test_resume_score.py
├── test_resume_suggestions.py
├── test_skill_extractor.py
│
├── PROJECT_ROADMAP.md
├── .gitignore
└── README.md
```

> `venv/`, generated Python cache files, uploaded resumes, and the local sample resume are intentionally excluded from version control.

---

## Installation

### Prerequisites

Make sure the following are installed:

- Python 3.11+
- Git
- Visual Studio Code

### 1. Clone the repository

```bash
git clone https://github.com/Chandan-Tippari-KK/AI-Based-Smart-Resume-Analyzer-and-Job-Recommendation-System.git
cd AI-Based-Smart-Resume-Analyzer-and-Job-Recommendation-System
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```powershell
pip install flask spacy scikit-learn pdfplumber python-docx reportlab
```

### 5. Download the spaCy English model

```powershell
python -m spacy download en_core_web_sm
```

### 6. Verify spaCy

```python
import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Resume Analyzer")

for token in doc:
    print(token.text)
```

---

## Running the Application

From the project root:

```powershell
python app.py
```

Flask starts the local development server.

Open the URL displayed in the terminal, typically:

```text
http://127.0.0.1:5000/
```

### Application Flow

1. Open the web application.
2. Select a PDF or DOCX resume.
3. Click **Analyze Resume**.
4. Review the generated analysis.
5. Explore skills, scores, job matches, recommendations, skill gaps, learning paths, and interview questions.
6. Download the generated PDF report when available.
7. Use **Clear Results** to reset the session.

---

## Testing

The project contains separate test scripts for major modules:

```text
test_ats_score.py
test_job_recommender.py
test_ml_job_matcher.py
test_nlp_skill_extractor.py
test_resume_score.py
test_resume_suggestions.py
test_skill_extractor.py
```

Example:

```powershell
python test_skill_extractor.py
```

ML job matching:

```powershell
python test_ml_job_matcher.py
```

ATS scoring:

```powershell
python test_ats_score.py
```

Resume scoring:

```powershell
python test_resume_score.py
```

Resume suggestions:

```powershell
python test_resume_suggestions.py
```

---

## AI, NLP and Machine Learning Approach

The project follows a hybrid approach rather than relying on a single AI model.

### NLP Layer

spaCy is used to process resume text and tokenize the content. The project then checks tokens and multi-word phrases against a predefined technical-skill vocabulary.

### Skill Matching Layer

A predefined skill database is used to identify technical skills and organize them into broader categories.

### Machine Learning Layer

The ML job matcher represents the resume and predefined job descriptions using **TF-IDF** vectors and calculates **cosine similarity** between them.

Conceptually:

```text
Resume Text
     │
     ▼
TF-IDF Vectorization
     │
     ├──────────────► Backend Developer
     ├──────────────► Full Stack Developer
     ├──────────────► Cloud Engineer
     ├──────────────► AI Engineer
     └──────────────► Agentic AI Engineer
                         │
                         ▼
                 Cosine Similarity
                         │
                         ▼
                  Match Percentage
```

### Rule-Based Intelligence

Several other modules use deterministic rules and predefined knowledge bases to produce:

- ATS scores
- Resume scores
- Skill gaps
- Career recommendations
- Learning paths
- Career roadmaps
- Interview questions
- Resume suggestions
- Resume strength analysis
- Resume ranking

This combination makes the project a **hybrid NLP + machine-learning + rule-based career analysis system**.

---

## Current Job Profiles

The current ML matching module contains predefined descriptions for:

- Backend Developer
- Full Stack Developer
- Cloud Engineer
- AI Engineer
- Agentic AI Engineer

The rule-based recommendation module also uses skill requirements for these roles.

---

## Current Limitations

The current implementation is an academic prototype and has several areas that can be improved:

- Job descriptions are currently predefined rather than retrieved from live job portals.
- Skill extraction uses a predefined vocabulary.
- Multi-word skill detection includes phrase-based matching.
- ATS scoring is a project-specific heuristic and does not reproduce commercial ATS systems.
- Career and salary recommendations are based on predefined rules rather than live market data.
- The application currently uses a Flask development server.
- The application should use a secure production secret key before deployment.
- Resume uploads should receive stronger validation and security controls before public deployment.
- Automated test coverage can be expanded and converted to a unified test framework such as `pytest`.

---

## Future Enhancements

Potential future improvements include:

- Advanced NLP and transformer-based skill extraction
- Named Entity Recognition for better resume understanding
- Semantic resume-job matching using embeddings
- Larger and dynamically updated job-description datasets
- Live job portal/API integration
- Resume ranking across multiple candidates
- Improved ATS compatibility analysis
- LLM-powered resume rewriting
- Personalized interview preparation
- Multi-language resume analysis
- Authentication and user profiles
- Database-backed resume history
- Production deployment using a WSGI server
- Containerization with Docker
- CI/CD integration
- Cloud deployment
- More comprehensive automated testing

---

## Academic Project Information

**Project Title:** AI-Based Smart Resume Analyzer and Job Recommendation System

**Project Type:** Mini Project

**Domain:**
- Artificial Intelligence
- Natural Language Processing
- Machine Learning

**Academic Year:** 2026

**Developed By:** Chandan Tippari K K

---

## Project Roadmap

The repository also contains [`PROJECT_ROADMAP.md`](PROJECT_ROADMAP.md), which documents the project's development plan, modules, testing notes, and planned enhancements.

The README describes the **current implementation**, while the roadmap is retained as the project's development documentation.

---

## Screenshots

Add screenshots of the application here after capturing the current UI.

Recommended screenshots:

```text
docs/
├── dashboard.png
├── resume-analysis.png
├── job-recommendations.png
└── pdf-report.png
```

Example Markdown:

```markdown
![Resume Analyzer Dashboard](docs/dashboard.png)
```

---

## Disclaimer

This project is an academic software prototype developed for educational purposes.

The generated resume scores, ATS-oriented scores, job matches, career recommendations, salary ranges, learning paths, and other outputs should be treated as **assistive recommendations**, not professional recruitment, employment, financial, or career guarantees.

---

## Author

**Chandan Tippari K K**

AI-Based Smart Resume Analyzer and Job Recommendation System  
Academic Mini Project — 2026

---

## License

This project does not currently specify an open-source license.

If you intend to allow others to reuse, modify, and distribute the code, consider adding an appropriate license such as the MIT License.
