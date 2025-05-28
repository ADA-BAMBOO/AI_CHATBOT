# from .BLEU import *
# from .Factual_Accuracy_LLM import *
# from .Factual_Accuracy import *
# from .Relevance_Score import *
# from .ROUGE import *
# from .Semantic_Similarity import *
import os
import importlib

# Lấy tên file .py trừ __init__.py
metric_modules = [
    f[:-3] for f in os.listdir(os.path.dirname(__file__))
    if f.endswith(".py") and f != "__init__.py"
]

# Tạo dictionary chứa các hàm compute
metric_functions = {}

for module_name in metric_modules:
    try:
        module = importlib.import_module(f"{__name__}.{module_name}")
        if hasattr(module, module_name):
            metric_func = getattr(module, module_name)
            metric_functions[module_name] = metric_func
        else:
            print(f"⚠️ Module '{module_name}' không có hàm compute()")
    except Exception as e:
        print(f"❌ Lỗi khi import module '{module_name}': {e}")
