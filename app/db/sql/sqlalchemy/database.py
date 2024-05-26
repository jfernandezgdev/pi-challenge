from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Declarar una clase Base que será la clase base para todas las clases de modelo
Base = declarative_base()

class Database:
    def __init__(self):
        """
        Constructor de la clase Database.
        """
        URL_BD_SQLALCHEMY = "sqlite:///./pi.db"
        # Crear el motor de base de datos con la URL especificada
        self.engine = create_engine(URL_BD_SQLALCHEMY, connect_args={"check_same_thread": False})
        # Crear una clase SessionLocal que se utilizará para interactuar con la base de datos
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
   
    def init_db(self):
        """
        Inicializa la base de datos creando todas las tablas según los modelos definidos.
        """
        # Crear todas las tablas en la base de datos según los modelos definidos
        Base.metadata.create_all(bind=self.engine)

    def get_db(self):
        """
        Obtener una sesión de base de datos.

        Returns:
        - Generator: Sesión de la base de datos.
        """
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()