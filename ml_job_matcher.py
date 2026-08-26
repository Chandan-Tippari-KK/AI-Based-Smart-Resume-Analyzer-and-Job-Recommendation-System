from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample job descriptions
JOB_DESCRIPTIONS = {
    "Backend Developer":
    """
    Python C# ASP.NET Core SQL Server REST API
    Entity Framework Core Git Azure DevOps Docker
    """,

    "Full Stack Developer":
    """
    Angular JavaScript TypeScript Node.js ASP.NET Core
    REST API SQL Git Docker
    """,

    "Cloud Engineer":
    """
    AWS Docker Kubernetes Terraform Jenkins
    Ansible Git Linux CI/CD
    """,

    "AI Engineer":
    """
    Python Machine Learning NLP Prompt Engineering
    LangChain RAG LLM AI Automation
    """,

    "Agentic AI Engineer":
    """
    Python Agentic AI CrewAI LangGraph LangChain
    RAG LLM Prompt Engineering AI Automation
    """
}


def recommend_jobs_ml(resume_text):
    """
    Recommends jobs using TF-IDF and Cosine Similarity.
    """

    documents = [resume_text]

    job_names = list(JOB_DESCRIPTIONS.keys())

    documents.extend(JOB_DESCRIPTIONS.values())

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_scores = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    )

    recommendations = {}

    for i, score in enumerate(similarity_scores[0]):
        recommendations[job_names[i]] = round(score * 100, 2)

    return recommendations