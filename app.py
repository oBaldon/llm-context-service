from fastapi import FastAPI
from pydantic import BaseModel
from services.model_service import analyze_text
from utils import save_output
from services.execution_time import ExecutionTimeMiddleware

app = FastAPI(title="LLM Context Analyzer")
app.middleware("http")(ExecutionTimeMiddleware(app))

class AnalyzeRequest(BaseModel):
    text: str
    model: str  # ex: "llama-3.2-1b-instruct" ou "llama-3.2-3b"

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    result = analyze_text(text=request.text, model=request.model)
    save_output.save_as_json(result, filename="resumo_contexto")
    save_output.save_as_txt(result, filename="resumo_contexto")
    return {"result": result}

