from models import (
    llama_3_2_1b_instruct,
    llama_3_2_1b,
    llama_3_2_3b,
    llama_3_2_3b_instruct
)

def analyze_text(text: str, model: str) -> str:
    if model == "llama-3.2-1b":
        return llama_3_2_1b.run(text)
    elif model == "llama-3.2-1b-instruct":
        return llama_3_2_1b_instruct.run(text)
    elif model == "llama-3.2-3b":
        return llama_3_2_3b.run(text)
    elif model == "llama-3.2-3b-instruct":
        return llama_3_2_3b_instruct.run(text)
    else:
        return f"Modelo '{model}' não suportado."
