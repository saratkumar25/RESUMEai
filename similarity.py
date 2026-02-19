from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    return model.encode(text)

def calculate_similarity(text1, text2):
    vec1 = get_embedding(text1)
    vec2 = get_embedding(text2)

    score = cosine_similarity([vec1], [vec2])[0][0]
    return score
