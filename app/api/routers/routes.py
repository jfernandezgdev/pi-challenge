from fastapi import APIRouter
from app.api.routers.root import router as root_router
from app.api.routers.character import router as character_router

# Crear una nueva instancia de APIRouter
router = APIRouter()

# Ruta Raíz
router.include_router(router=root_router, tags=["Raíz"])
# Ruta Character
router.include_router(router=character_router, prefix="/character", tags=["Personaje"])