def generate_interview_questions(skills):

    questions = []

    if "Python" in skills:
        questions.extend([
            "Explain Python decorators.",
            "What is the difference between List and Tuple?",
            "Explain generators in Python."
        ])

    if ".NET Core" in skills or "ASP.NET Core" in skills:
        questions.extend([
            "Explain Dependency Injection in ASP.NET Core.",
            "What is Middleware?",
            "Difference between .NET Framework and .NET Core."
        ])

    if "SQL" in skills or "SQL Server" in skills:
        questions.extend([
            "What is normalization?",
            "Difference between DELETE, TRUNCATE and DROP.",
            "Explain Indexes in SQL."
        ])

    if "Angular" in skills:
        questions.extend([
            "What are Angular Components?",
            "Explain Dependency Injection in Angular.",
            "Difference between ngIf and ngFor."
        ])

    if "Docker" in skills:
        questions.extend([
            "What is Docker?",
            "Difference between Docker Image and Container.",
            "Explain Docker Compose."
        ])

    if "AWS" in skills:
        questions.extend([
            "What is EC2?",
            "Difference between EC2 and Lambda.",
            "Explain S3."
        ])

    if "Agentic AI" in skills:
        questions.extend([
            "What is Agentic AI?",
            "Difference between AI Agent and Chatbot.",
            "Explain CrewAI."
        ])

    return questions