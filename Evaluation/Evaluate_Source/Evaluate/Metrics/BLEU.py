import nltk
nltk.download('punkt_tab')
from nltk.translate.bleu_score import sentence_bleu,SmoothingFunction
from nltk.tokenize import word_tokenize
def BLEU(question, bot_answer, real_answer):
    smoothie = SmoothingFunction().method1

    # Token hóa đúng chuẩn
    reference_tokens = [word_tokenize(real_answer)]  # chú ý: phải là list lồng list
    hypothesis_tokens = word_tokenize(bot_answer)

    return float(sentence_bleu(reference_tokens, hypothesis_tokens, smoothing_function=smoothie))