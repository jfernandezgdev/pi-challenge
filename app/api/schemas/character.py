from pydantic import BaseModel

# Clase base para la validación y serialización de datos de personajes
class CharacterBase(BaseModel):
    name: str          # Nombre
    height: int        # Altura
    mass: int          # Masa
    hair_color: str    # Color de cabello
    skin_color: str    # Color de piel
    eye_color: str     # Color de ojos
    birth_year: int    # Año de nacimiento

# Clase para la creación de un nuevo personaje, hereda de CharacterBase
class CharacterCreate(CharacterBase):
    pass  # No se agregan campos adicionales, pero permite la extensión futura

# Clase para representar un personaje con su ID, hereda de CharacterBase
class Character(CharacterBase):
    id: int  # Identificador único del personaje

    # Configuración adicional para habilitar que Pydantic funcione con SQLAlchemy
    class Config:
        from_attributes = True  # Habilita el modo ORM para la conversión entre modelos de Pydantic y SQLAlchemy