# 🧠 LLM Context Service

Este é um microserviço para **análise de contexto e significado de textos transcritos**, utilizando modelos LLM da família **LLaMA (Meta)**.  
Ele recebe via API REST um texto e retorna uma resposta estruturada com **contexto, tópicos principais e resumo**, baseado no modelo selecionado.

---

## 🚀 Funcionalidades

- Recebe texto bruto (como transcrição de áudio) via endpoint HTTP.
- Analisa contexto e significado com LLMs.
- Suporte a múltiplos modelos:
  - `meta-llama/Llama-3.2-1B`
  - `meta-llama/Llama-3.2-1B-Instruct`
  - `meta-llama/Llama-3.2-3B`
  - `meta-llama/Llama-3.2-3B-Instruct`
- Estrutura de resposta padronizada no formato:
  - `"system"`, `"user"` e `"assistant"`
- Salvamento automático do resultado como `.json` e `.txt`.

---

## ✅ Requisitos

- **Python 3.12+**
- **Token HuggingFace** (necessário para modelos *Instruct*)
- Dependências definidas em `requirements.txt`

---

## ⚙️ Instalação e Execução

### 1. Clonar o repositório
```bash
git clone https://github.com/seu_usuario/llm-context-service.git
cd llm-context-service
```

### 2. Criar e ativar o ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configuração do `.env`

> ℹ️ **Importante:** Certifique-se de criar um arquivo `.env` na raiz do projeto antes de iniciar o microserviço.  
> Esse arquivo deve conter a variável de ambiente necessária para autenticar no HuggingFace.

```env
HF_TOKEN=seu_token_huggingface_aqui
```

> ❗ Modelos *Instruct* exigem login/autenticação. Mesmo com o token no `.env`, pode ser necessário executar:
```bash
huggingface-cli login
```

---

### 5. Iniciar o microserviço
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

---

## 📡 Uso da API

### **Endpoint:** `/analyze`
- **Método:** `POST`
- **Descrição:** Recebe um texto e retorna o contexto, significado e resumo do conteúdo.
- **Parâmetros do corpo da requisição:**
  - `text`: string com o conteúdo a ser analisado
  - `model`: string com o nome do modelo (ex: `llama-3.2-1b-instruct`)

### **Exemplo de requisição com `curl`:**
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "text": "'"$(cat ./tests/sample_text.txt | sed 's/"/\"/g')"'", 
    "model": "llama-3.2-1b-instruct"
  }'
```

### **Exemplo de resposta JSON:**
```json
{
  "result": [
    {
      "role": "system",
      "content": "Você é um assistente útil e especialista em linguagem natural."
    },
    {
      "role": "user",
      "content": "Texto completo enviado no prompt"
    },
    {
      "role": "assistant",
      "content": "Resposta do modelo com resumo e tópicos estruturados"
    }
  ]
}
```

---

## 📦 Execução com Docker

### 1. Construir a imagem Docker
```bash
docker build -t llm-context-service .
```

### 2. Executar o contêiner
```bash
docker run -p 8000:8000 llm-context-service
```

### 3. Ou executar com Docker Compose
```bash
docker-compose up --build
```

---

## 📁 Estrutura do Projeto

```
llm-context-service/
│
├── app.py                  # Aplicação principal FastAPI
├── config/                 # Configuração e variáveis de ambiente
├── models/                 # Diferentes implementações de modelos LLaMA
├── services/               # Orquestração dos modelos
├── utils/                  # Salvamento do resultado em arquivos
├── tests/                 # Textos de entrada para testes da API
├── temp/                   # Saída automática gerada (.json/.txt)
├── Dockerfile              # Definição da imagem Docker
├── docker-compose.yml      # Orquestração com Docker Compose
├── requirements.txt        # Dependências Python
└── README.md               # Documentação do projeto
```

---

## 🛠 Tecnologias Utilizadas

- **Python 3.12**
- **FastAPI**
- **Hugging Face Transformers**
- **Modelos Meta-LLaMA**
- **Docker & Docker Compose**

---

## 👤 Autor

Desenvolvido por [@oBaldon](https://github.com/oBaldon)

Contribuições e melhorias são bem-vindas!

---

### 📍 Roadmap Técnico

Para conhecer os próximos passos planejados para a evolução do `llm-context-service`, melhorias técnicas, testes e escalabilidade, consulte o [📍 Roadmap Técnico](./ROADMAP.md).  
Esse documento detalha as fases de desenvolvimento e prioridades recomendadas para o projeto.