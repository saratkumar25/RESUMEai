from similarity import calculate_similarity
from skills_extractor import extract_skills

def calculate_final_score(resume_text, jd_text):

    # Semantic similarity (70%)
    similarity_score = calculate_similarity(resume_text, jd_text)

    # Skills matching (30%)
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched = len(set(resume_skills) & set(jd_skills))
    total = len(jd_skills) if len(jd_skills) > 0 else 1

    skills_score = matched / total

    final_score = (0.7 * similarity_score) + (0.3 * skills_score)

    return round(final_score * 100, 2)
