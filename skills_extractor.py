skills_list = [
    "python",
    "machine learning",
    "deep learning",
    "sql",
    "tensorflow",
    "pandas",
    "numpy",
    "data analysis"
]

def extract_skills(text):
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills
