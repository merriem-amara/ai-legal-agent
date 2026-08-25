from fastapi import APIRouter

from ai_legal_core.api.health import router as health_router
from ai_legal_core.api.documents import router as documents_router


api_router = APIRouter()

api_router.include_router(
    health_router
)

api_router.include_router(
    documents_router
)
