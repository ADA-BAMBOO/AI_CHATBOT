from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer("all-MiniLM-L6-v2")
def Semantic_Similarity(question,bot_answer,real_answer):
    emb1 = model.encode(real_answer, convert_to_tensor=True)
    emb2 = model.encode(bot_answer, convert_to_tensor=True)

    similarity = util.pytorch_cos_sim(emb1, emb2).item()
    return float(similarity)