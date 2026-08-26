def generate_career_roadmap(skills):

    skills = [s.lower() for s in skills]

    roadmap = {}

    if "python" in skills:

        roadmap = {

            "Career": "AI Engineer",

            "Missing Skills": [
                "Machine Learning",
                "Deep Learning",
                "TensorFlow",
                "PyTorch"
            ],

            "Certifications": [
                "Google AI Professional",
                "AWS Machine Learning Specialty",
                "Microsoft Azure AI Engineer"
            ],

            "Learning Platforms": [
                "Coursera",
                "Udemy",
                "DeepLearning.AI",
                "Kaggle"
            ],

            "Salary": "₹12 LPA - ₹28 LPA",

            "Duration": "4-6 Months"
        }

    elif ".net core" in skills or "asp.net core" in skills:

        roadmap = {

            "Career": "Senior Backend Developer",

            "Missing Skills": [
                "Microservices",
                "Docker",
                "Kubernetes",
                "Azure"
            ],

            "Certifications": [
                "Azure Developer Associate",
                "Docker Certified Associate"
            ],

            "Learning Platforms": [
                "Microsoft Learn",
                "Udemy",
                "Coursera"
            ],

            "Salary": "₹10 LPA - ₹22 LPA",

            "Duration": "3-5 Months"
        }

    else:

        roadmap = {

            "Career": "Software Engineer",

            "Missing Skills": [
                "DSA",
                "System Design"
            ],

            "Certifications": [],

            "Learning Platforms": [
                "Coursera"
            ],

            "Salary": "₹6 LPA - ₹12 LPA",

            "Duration": "2-3 Months"
        }

    return roadmap