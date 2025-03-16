import torch
from transformers import pipeline

model_id = "meta-llama/Llama-3.3-70B-Instruct"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

def run(text: str) -> str:
    messages = [
        {"role": "system", "content": "Você é um assistente útil e especialista em linguagem natural."},
        {"role": "user", "content": f"Explique sobre o que se trata este texto:\n\n{text}\n\nResumo e contexto:"}
    ]
    result = pipe(messages, max_new_tokens=512)
    return result[0]["generated_text"]
