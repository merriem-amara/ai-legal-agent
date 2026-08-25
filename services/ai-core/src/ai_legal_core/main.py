from fastapi import FastAPI

from ai_legal_core.api.router import api_router
from ai_legal_core.config.settings import settings


app = FastAPI(
    title=settings.app_name,
    version="0.1.0"
)


app.include_router(
    api_router
)
