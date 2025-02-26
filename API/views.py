from django.shortcuts import render
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
import requests

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import time
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_directory = "API/model_bbo"
tokenizer = AutoTokenizer.from_pretrained(model_directory)
model = AutoModelForCausalLM.from_pretrained(
    model_directory,
    device_map="auto",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32  # Dùng FP16 nếu GPU hỗ trợ
).to(device)

class GetJsonAPI(APIView):
    model=model
    tokenizer=tokenizer
    def post(self,request):
        quest_packet=request.data
        try:
            for i in quest_packet:
                if i == None:
                    return Response({"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)
            res,time=self.chat_with_AI(quest_packet['message'])
            return Response({"answer":res,"time":time}) 
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def chat_with_AI(self, prompt, max_length=50):
        start_time = time.time()
        # Tokenize input và đưa vào GPU
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
        inputs = {key: value.to(self.model.device) for key, value in inputs.items()}

        # Sinh văn bản với mô hình trên GPU
        with torch.no_grad():  # Tắt gradient để tiết kiệm bộ nhớ
            output = self.model.generate(**inputs, max_length=max_length)

        # Giải mã kết quả
        res = self.tokenizer.decode(output[0], skip_special_tokens=True)

        # Loại bỏ câu hỏi khỏi kết quả, chỉ giữ câu trả lời
        answer = res[len(prompt):].strip()
        end_time = time.time()
        duration = end_time - self.start_time
        return answer,duration