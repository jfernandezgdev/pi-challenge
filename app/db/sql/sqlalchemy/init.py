import logging
from app.db.sql.sqlalchemy.database import Database

def init_database():
    """
    Inicializa la base de datos.

    Crea una instancia de la clase Database y llama al método init_db() 
    para realizar la inicialización de la base de datos. 
    Además, registra en el log que la base de datos ha sido inicializada correctamente.
    """
    db = Database()  # Crear una instancia de la clase Database
    db.init_db()  # Inicializar la base de datos
    logging.info("Base de datos inicializada correctamente")