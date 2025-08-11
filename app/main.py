from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import logger

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint accessed")
    return {"status": "ok"}
