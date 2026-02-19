import streamlit as st
import os
from parser import extract_text_from_pdf
from utils import clean_text
from ranking import calculate_final_score

st.title("AI Resume Screening System")

jd_input = st.text_area("Paste Job Description Here")

if st.button("Rank Candidates"):

    if jd_input.strip() == "":
        st.warning("Please enter a job description.")
    else:
        jd_text = clean_text(jd_input)

        results = []

        resume_folder = "resumes"

        for file in os.listdir(resume_folder):
            if file.endswith(".pdf"):
                file_path = os.path.join(resume_folder, file)

                resume_text = extract_text_from_pdf(file_path)
                resume_text = clean_text(resume_text)

                score = calculate_final_score(resume_text, jd_text)

                results.append((file, score))

        results.sort(key=lambda x: x[1], reverse=True)

        st.subheader("Ranking Results")

        for name, score in results:
            st.write(f"{name} → {score}% match")
