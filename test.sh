#!/bin/bash

# Timestamp atual
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

# Diretórios de saída
HEADER_DIR="logs/headers"
BODY_DIR="logs/bodies"

# Cria os diretórios, se ainda não existirem
mkdir -p "$HEADER_DIR"
mkdir -p "$BODY_DIR"

# Caminhos dos arquivos
HEADER_FILE="$HEADER_DIR/headers_$TIMESTAMP.txt"
BODY_FILE="$BODY_DIR/body_$TIMESTAMP.json"

# Requisição curl
curl -s -D "$HEADER_FILE" -o "$BODY_FILE" -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "text": "'"$(cat ./tests/sample_text.txt | sed 's/"/\\"/g')"'", 
    "model": "llama-3.1-8b-instruct"
  }'

# Exibe o caminho dos arquivos salvos
echo "🗂 Headers salvos em: $HEADER_FILE"
echo "📦 Corpo da resposta salvo em: $BODY_FILE"

