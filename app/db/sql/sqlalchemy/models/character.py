from sqlalchemy import Column, Integer, String
from app.db.sql.sqlalchemy.database import Base 

# Definición del modelo Character
class CharacterModel(Base):
    """
    Modelo Character que representa a un personaje en la base de datos.
    """    
    # Nombre de la tabla en la base de datos
    __tablename__ = "characters"
    
    # Columnas de la tabla
    id = Column(Integer, primary_key=True, index=True)  # Identificador único
    name = Column(String, index=True)  # Nombre del personaje
    height = Column(Integer)  # Altura
    mass = Column(Integer)  # Peso
    hair_color = Column(String)  # Color de cabello
    skin_color = Column(String)  # Color de piel
    eye_color = Column(String)  # Color de ojos
    birth_year = Column(Integer)  # Año de nacimiento
