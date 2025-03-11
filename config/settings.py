from dotenv import load_dotenv
import os
from huggingface_hub import login

load_dotenv()

# Configurações globais do modelo (se necessário no futuro)
N_CTX = int(os.getenv("N_CTX", 2048))
N_THREADS = int(os.getenv("N_THREADS", 6))
N_GPU_LAYERS = int(os.getenv("N_GPU_LAYERS", 40))

# Token de autenticação Hugging Face (para modelos gated)
HF_TOKEN = os.getenv("HF_TOKEN", None)

if HF_TOKEN:
    login(HF_TOKEN)
    print("[✅] Login no Hugging Face realizado com sucesso via código.")
else:
    print("[⚠️] Nenhum HF_TOKEN encontrado. Modelos gated podem não funcionar sem login.")
