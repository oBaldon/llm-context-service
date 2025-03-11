import torch
from transformers import pipeline

model_id = "meta-llama/Llama-3.2-1B"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

def run(text: str) -> str:
    prompt = (
        "A seguir, um texto será apresentado. Sua tarefa é analisá-lo e explicar de forma clara e estruturada "
        "sobre o que se trata, quais os principais tópicos abordados e qual o objetivo do texto.\n\n"
        "Texto:\n"
        f"{text}\n\n"
        "Agora, forneça um resumo detalhado com tópicos estruturados:"
    )
    result = pipe(prompt, max_new_tokens=512)
    generated_text = result[0]["generated_text"]
    clean_response = generated_text.replace(prompt, "").strip()
    return [
        {"role": "system", "content": "Você é um assistente útil e especialista em linguagem natural."},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": clean_response}
    ]
