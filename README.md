# AI-Powered Investor Intelligence Platform

A starting implementation of the Investor Intelligence Platform described in the BRD.

## Current milestone

- FastAPI backend
- Simple HTML/CSS dashboard
- Health-check endpoint
- Environment-variable configuration
- Ready for Git/GitHub
- Docker-ready structure for the next milestone

## Planned milestones

1. Local development setup
2. Git/GitHub workflow
3. PDF upload and document storage
4. PDF -> Markdown/text extraction
5. Semantic chunking + embeddings
6. Azure AI Search vector index
7. KPI extraction
8. Risk factors / growth drivers / executive summary
9. RAG chat assistant
10. PostgreSQL persistence
11. Docker + Azure Container Registry
12. AKS deployment
13. CI/CD and production hardening

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000
