from fastapi import FastAPI

from routes.dashboard import router as dashboard_router
from routes.health import router as health_router
from routes.chat import router as chat_router
from routes.ingestion import router as ingestion_router
# from routes.aish import router as aish_router

app = FastAPI(
    title="Investor Intelligence API",
    version="1.0.0"
)
# app.include_router(
#     aish_router,
#     prefix="/api",
#     tags=["AI Search"]
# )

app.include_router(
    health_router,
    tags=["Health"]
)

app.include_router(
    dashboard_router,
    prefix="/api",
    tags=["Dashboard"]
)
# Chat API
app.include_router(
    chat_router,
    prefix="/api",
    tags=["Chat"]
)
# Ingestion API
app.include_router(
    ingestion_router,
    prefix="/api",
    tags=["Ingestion"]

)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)