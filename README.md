# RESUME SORTER

A simple NLP-based web application that automatically ranks candidate resumes based on a given job description.

The system reads PDF resumes, extracts text, compares them with the job role using semantic similarity, and produces a match score for each candidate.

---

## Features

* Upload job description
* Automatic PDF resume parsing
* Skill detection
* Semantic similarity matching (BERT embeddings)
* Candidate ranking with match percentage
* Clean web interface using Streamlit

---

## Tech Stack

* Python
* Streamlit
* Sentence Transformers (MiniLM)
* Scikit-learn (Cosine Similarity)
* PyMuPDF (PDF text extraction)

---

## How It Works

1. Extract text from resumes
2. Clean and preprocess text
3. Convert text to embeddings
4. Compare with job description
5. Calculate similarity + skill match score
6. Rank candidates

---
