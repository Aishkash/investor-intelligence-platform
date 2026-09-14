from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

app = FastAPI(
    title="AI-Powered Investor Intelligence Platform",
    version="0.1.0",
)

app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static",
)


@app.get("/health")
def health():
    return {"status": "ok", "service": "investor-intelligence-platform"}


@app.get("/")
def home():
    return FileResponse(FRONTEND_DIR / "index.html")
