def flee_score(risk_aversion, predation_level):
    score = max(0, min(((1+(risk_aversion/200)) * predation_level), 100))
    return score

add toxicity
