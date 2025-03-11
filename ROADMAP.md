# 📍 Roadmap Técnico – LLM Context Service

Este roadmap apresenta as etapas de evolução técnica do projeto `llm-context-service`, com foco em organização, qualidade, testes e escalabilidade.

---

## 🔹 Fase 1 — Qualidade de Código e Arquitetura
✅ Já iniciado com sucesso, foco em:
- [x] Separação de responsabilidades por serviço e modelo.
- [x] Organização modular e escalável (config, services, models, utils).
- [x] Estrutura de resposta padronizada com `system`, `user` e `assistant`.

### Ações pendentes:
- [ ] Adicionar docstrings detalhadas nos endpoints da FastAPI.
- [ ] Substituir `print()` por `logging` estruturado com níveis (`INFO`, `WARNING`, `ERROR`).
- [ ] Melhorar tratamento de exceções nos serviços de modelo.

---

## 🔹 Fase 2 — Melhorias Funcionais
- [ ] Permitir upload de arquivos `.txt` diretamente para análise (além do corpo JSON).
- [ ] Adicionar suporte a múltiplas respostas paralelas (batch inference).
- [ ] Modularização de prompts por tipo de análise (resumo, classificação, etc.).

---

## 🔹 Fase 3 — Testes Automatizados
- [ ] Estrutura de testes com `pytest`.
- [ ] Testar diferentes cenários com `TestClient` da FastAPI.
- [ ] Testar falhas comuns: modelo inválido, input vazio, erro de autenticação.

---

## 🔹 Fase 4 — Produção e Performance
- [ ] Endpoint `/healthcheck` para monitoramento.
- [ ] Otimizar `max_new_tokens` dinamicamente com base no tamanho do texto.
- [ ] Adicionar cache local dos modelos baixados.

---

## 🔹 Fase 5 — Docker & Deploy
- [x] Dockerfile com imagem leve baseada em `python:3.12-slim`.
- [x] Docker Compose com suporte a `.env`.
- [ ] Criar versão com suporte a GPU para modelos maiores.
- [ ] Documentar deploy com Docker em ambientes reais (cloud/VPS).

---

## 🔹 Fase 6 — Documentação e Contribuição
- [x] Criar `README.md` completo.
- [ ] Criar `CONTRIBUTING.md` com diretrizes.
- [ ] Incluir `CHANGELOG.md` com histórico das versões.
- [ ] Adicionar versão traduzida do `README` em inglês (`README.en.md`).

---

## 📌 Prioridades recomendadas (curto prazo)
✅ Estrutura modular e reutilizável  
✅ Suporte a múltiplos modelos  
✅ Logging estruturado e docstrings  
✅ Testes automatizados com FastAPI TestClient