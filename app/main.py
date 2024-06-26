from fastapi import FastAPI
from app.api.logging import init_logging
from app.api.routers.routes import router
from app.db.sql.sqlalchemy.init import init_database

# Inicializar el sistema de logs
init_logging()

# Crear una instancia de la aplicación FastAPI
app = FastAPI(title="Challenge Python | Pi Data Strategy & Consulting")

# Incluir las rutas de la API
app.include_router(router)

# Inicializar la base de datos
init_database()

# Eston es una pruebas testing
