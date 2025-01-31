from api_v1.routes import chat, completions, engines, health, embeddings
from fastapi import APIRouter

router = APIRouter()

router.include_router(chat.router)
router.include_router(completions.router)
router.include_router(engines.router)
router.include_router(health.router)
router.include_router(embeddings.router)
