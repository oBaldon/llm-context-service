# Dockerfile
FROM python:3.12-slim

# Diretório da aplicação
WORKDIR /app

# Copia os arquivos
COPY . .

# Instala dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expondo porta
EXPOSE 8000

# Comando padrão para iniciar a API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
