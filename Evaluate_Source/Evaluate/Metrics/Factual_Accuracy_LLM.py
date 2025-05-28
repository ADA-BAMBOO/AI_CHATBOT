from sentence_transformers import util,SentenceTransformer
import re
import google.generativeai as genai
from google.generativeai import GenerativeModel
model = GenerativeModel("gemini-2.0-flash")
genai.configure(api_key='AIzaSyB3UsRhTacEumwAKLH6jWn1LYLf8dP_BLU')
def Factual_Accuracy_LLM(question, bot_answer, real_answer):
    prompt = f"""
You are a fact-checking assistant.

Given:
- Question: {question}
- Chatbot Answer: {bot_answer}
- Ground Truth Answer: {real_answer}

Your task:
Evaluate how factually accurate the chatbot's answer is **compared to the ground truth**.
Return a factual accuracy **score as a floating-point number between 0.0 and 1.0**:
- 1.0 means completely factually accurate and aligned with the ground truth.
- 0.0 means entirely inaccurate or hallucinated.
Use your best judgment based on the factual content overlap and correctness.

Instructions:
Only respond with the score (e.g., 0.87). Do not explain your reasoning.
"""

    response = model.generate_content(prompt)
    return float(response.text.strip())