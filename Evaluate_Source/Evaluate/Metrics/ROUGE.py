from rouge_score import rouge_scorer
def ROUGE(question,bot_answer,real_answer):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = scorer.score(real_answer, bot_answer)
    return scores['rouge1'].fmeasure