from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import logger
from app.api.v1.endpoints import task

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(task.router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint accessed")
    return {"status": "ok"}
