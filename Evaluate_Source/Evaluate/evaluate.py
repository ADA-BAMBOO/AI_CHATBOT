from sentence_transformers import SentenceTransformer, util
import os
import pandas as pd
import torch
import gc
import wikipedia
import re
# from Metrics import *
# from Training import *
from Evaluate.Metrics import metric_functions

def evaluate(question,bot_answer,real_answer):
    scores={}
    for name,fun in metric_functions.items():
        scores[name]=round(fun(question,bot_answer,real_answer),3)
    return scores
