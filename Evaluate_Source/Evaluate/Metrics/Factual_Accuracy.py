from sentence_transformers import util,SentenceTransformer
import re
embedder=SentenceTransformer("BAAI/bge-large-en-v1.5")

def Factual_Accuracy(question,bot_answer,real_answer):
    """Tính factual accuracy dựa trên độ tương đồng giữa câu trả lời mô hình và câu tham chiếu"""

    if not isinstance(real_answer, str) or len(real_answer.strip()) == 0:
        print(f"❌ Câu tham chiếu lỗi tại câu hỏi '{question}': {real_answer}")
        raise ValueError("Giá trị real_answer không hợp lệ (rỗng hoặc không phải chuỗi).")
    # Gọi mô hình để dự đoán câu trả lời

    answers = re.findall(r'A: (.*?)(?=Q:|\Z)', bot_answer, re.DOTALL)
    answer = answers[0].strip() if answers else bot_answer.strip()

    if not isinstance(answer, str) or len(answer.strip()) == 0:
        print(f"❌ Câu tham chiếu lỗi tại câu hỏi '{question}': {bot_answer}")
        raise ValueError("Giá trị bot_answer không hợp lệ (rỗng hoặc không phải chuỗi).")

    # Mã hóa câu trả lời mô hình và câu tham chiếu để tính độ tương đồng
    embedding_bot_answer = embedder.encode(answer, convert_to_tensor=True)
    embedding_real_answer = embedder.encode(real_answer, convert_to_tensor=True)

    score = util.pytorch_cos_sim(embedding_bot_answer, embedding_real_answer).item()
    return float(score)