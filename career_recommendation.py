def generate_career_recommendation(skills):

    skills_set = set(skills)

    if {"Python", "LLM", "LangChain"}.issubset(skills_set):

        return {
            "Career": "AI Engineer",

            "Missing Skills": [
                "TensorFlow",
                "PyTorch",
                "Vector Databases",
                "MLOps"
            ],

            "Certifications": [
                "AWS Certified AI Practitioner",
                "Microsoft Azure AI Engineer"
            ],

            "Learning Platforms": [
                "Coursera",
                "Udemy",
                "Microsoft Learn"
            ],

            "Salary": "₹8 LPA - ₹35+ LPA"
        }

    elif {".NET Core", "ASP.NET Core", "SQL Server"}.issubset(skills_set):

        return {
            "Career": "Backend Developer",

            "Missing Skills": [
                "Microservices",
                "Redis",
                "RabbitMQ",
                "Azure"
            ],

            "Certifications": [
                "Microsoft Azure Developer Associate"
            ],

            "Learning Platforms": [
                "Microsoft Learn",
                "Udemy"
            ],

            "Salary": "₹6 LPA - ₹25+ LPA"
        }

    elif {"Angular", "JavaScript"}.issubset(skills_set):

        return {
            "Career": "Frontend Developer",

            "Missing Skills": [
                "React",
                "Next.js",
                "Testing"
            ],

            "Certifications": [
                "Meta Front-End Developer"
            ],

            "Learning Platforms": [
                "Coursera",
                "Udemy"
            ],

            "Salary": "₹5 LPA - ₹22+ LPA"
        }

    else:

        return {
            "Career": "Software Engineer",

            "Missing Skills": [
                "DSA",
                "System Design"
            ],

            "Certifications": [
                "AWS Cloud Practitioner"
            ],

            "Learning Platforms": [
                "Coursera"
            ],

            "Salary": "₹5 LPA - ₹20+ LPA"
        }