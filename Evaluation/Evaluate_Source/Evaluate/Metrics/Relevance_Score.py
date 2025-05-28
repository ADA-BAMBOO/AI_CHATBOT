from sentence_transformers import util,SentenceTransformer
embedder=SentenceTransformer("BAAI/bge-large-en-v1.5")
# ✅ Hàm tính Relevance Score
def Relevance_Score(question,bot_answer,real_answer):
    """Tính mức độ liên quan giữa câu hỏi và câu trả lời"""
    # ✅ Kiểm tra nếu question hoặc answer bị lỗi (None, NaN, float)
    if question is None or bot_answer is None or isinstance(question, float) or isinstance(bot_answer, float):
        print(f"❌ Câu tham chiếu lỗi tại câu hỏi '{question}': {bot_answer}")
        raise ValueError("Giá trị bot_answer không hợp lệ (rỗng hoặc không phải chuỗi).")

    # ✅ Nếu là float, chuyển thành str
    if isinstance(question, float):
        question = str(question)
    if isinstance(bot_answer, float):
        bot_answer = str(bot_answer)

    # ✅ Encode câu hỏi và câu trả lời
    embedding_question = embedder.encode(question, convert_to_tensor=True)
    embedding_answer = embedder.encode(bot_answer, convert_to_tensor=True)

    score = util.pytorch_cos_sim(embedding_question, embedding_answer).item()
    return float(score)