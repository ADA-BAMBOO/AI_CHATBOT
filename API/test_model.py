import os
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Đường dẫn tới thư mục chứa mô hình đã lưu
model_directory = "API/model_bbo"

# # Tải tokenizer và mô hình từ thư mục địa phương
tokenizer = AutoTokenizer.from_pretrained(model_directory)
model = AutoModelForCausalLM.from_pretrained(
    model_directory,
    device_map='auto',
    torch_dtype='auto'  
)

print()


def chat_with_AI(prompt, model, tokenizer, max_length=50):
    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)

    # Đảm bảo dữ liệu đầu vào được đặt trên đúng thiết bị mà mô hình đang sử dụng
    inputs = {key: value.to(model.device) for key, value in inputs.items()}

    # Sinh văn bản (không truyền bất kỳ tham số sampling nào)
    with torch.no_grad():  # Tắt gradient để tối ưu bộ nhớ
        output = model.generate(**inputs, max_length=max_length)

    # Giải mã kết quả
    res = tokenizer.decode(output[0], skip_special_tokens=True)

    # Chỉ trả về câu trả lời, không có câu hỏi
    answer = res[len(prompt):].strip()  # Loại bỏ câu hỏi khỏi kết quả
    return answer

Answer = chat_with_AI("What is cardano", model, tokenizer)
print(Answer)
