from fastapi import APIRouter
from app.api.controllers import character as controller
from app.api.schemas.character import CharacterCreate, Character

# Crear una nueva instancia de APIRouter
router = APIRouter()

# Ruta para obtener todos los personajes
@router.get("/getAll", response_model=list[Character])
def get_all():
    """
    Retorna la lista de todos los personajes existentes de la base de datos.
    """
    return controller.get_all_characters()

# Ruta para obtener un personaje específico por ID
@router.get("/get/{id}", response_model=Character)
def get(id: int):
    """
    Retorna un personaje por su ID.
    
    Args:
        id (int): ID del personaje a buscar.
    """
    return controller.get_character(id)

# Ruta para crear un nuevo personaje
@router.post("/add", response_model=Character)
def create(character: CharacterCreate):
    """
    Crea un nuevo personaje

    Args:
        character (CharacterCreate): Datos del personaje a crear.
    """
    return controller.create_character(character)

# Ruta para eliminar un personaje por ID
@router.delete("/delete/{id}")
def delete(id: int):
    """
    Elimina un personaje por su ID.

    Args:
        id (int): ID del personaje a eliminar.
    """
    return controller.delete_character(id)
