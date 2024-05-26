from fastapi import  HTTPException, status
from app.core.use_cases.character import CharacterUseCase
from app.api.schemas.character import CharacterCreate
from pydantic import ValidationError
import logging

# Función para obtener todos los personajes
def get_all_characters():
    """
    Retorna todos los personajes disponibles.

    Returns:
        List[Character]: Lista de todos los personajes.
    """   
    function_name = get_all_characters.__name__
    logging.info('[#] Inicio controllers - {}()'.format(function_name))
    
    try:
        # Inicializar el caso de uso
        use_case = CharacterUseCase()
        # Retornar todos los personajes
        characters = use_case.get_characters()
        logging.info(f'[#] Fin controllers - {function_name}()')
        return characters
    except HTTPException as http_exception:
        # Capturamos excepción HTTPException y devolvemos el detalle
        logging.error(http_exception.detail)
        raise http_exception      
    except Exception as e:
        # Capturamos excepciónes diferentes a HTTPException y devolvemos el detalle
        error_message = f'Error al obtener los personajes: {e}'
        logging.error(error_message)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_message)
    
# Función para obtener un personaje específico por ID
def get_character(character_id: int):
    """
    Retorna un personaje por su ID.

    Args:
        character_id (int): ID del personaje.

    Returns:
        Character: El personaje correspondiente al ID proporcionado.
    """    
    function_name = get_character.__name__
    logging.info(f'[#] Inicio controllers - {function_name}()')
    
    try:
        # Inicializar el caso de uso
        use_case = CharacterUseCase()
        # Retornar el personaje por ID
        character = use_case.get_character(character_id)
        if character is None:
            error_message = f'Personaje con ID {character_id} no encontrado'
            logging.warning(error_message)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_message)
        logging.info(f'[#] Fin controllers - {function_name}()')
        return character
    except HTTPException as http_exception:
        # Capturamos excepción HTTPException y devolvemos el detalle
        logging.error(http_exception.detail)
        raise http_exception     
    except Exception as e:
        # Capturamos excepciónes diferentes a HTTPException y devolvemos el detalle
        error_message = f'Error al obtener el personaje: {e}'
        logging.error(error_message)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_message)
    
# Función para crear un nuevo personaje
def create_character(character: CharacterCreate):
    """
    Crea un nuevo personaje.

    Args:
        character (CharacterCreate): Datos del personaje a crear.

    Returns:
        Character: El nuevo personaje creado.
    """   
    function_name = create_character.__name__
    logging.info(f'[#] Inicio controllers - {function_name}()')
    
    try:
        # Inicializar el caso de uso
        use_case = CharacterUseCase()
        # Verificar si el personaje ya existe en la base de datos por nombre
        db_character = use_case.get_character_by_name(character.name)
        if db_character:
            error_message = f'Personaje con nombre {character.name} ya existe'
            logging.warning(error_message)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_message)
        # Crear el personaje si no existe
        new_character = use_case.create(character)
        logging.info(f'[#] Fin controllers - {function_name}()')
        return new_character
    except HTTPException as http_exception:
        # Capturamos excepción HTTPException y devolvemos el detalle
        logging.error(http_exception.detail)
        raise http_exception   
    except Exception as e:
        # Capturamos excepciónes diferentes a HTTPException y devolvemos el detalle
        error_message = f'Error al crear el personaje: {e}'
        logging.error(error_message)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_message)

# Función para eliminar un personaje por su ID
def delete_character(character_id: int):
    """
    Elimina un personaje por su ID.

    Args:
        character_id (int): ID del personaje a eliminar.

    Returns:
        dict: Detalle del resultado de la eliminación.
    """    
    function_name = delete_character.__name__
    logging.info(f'[#] Inicio controllers - {function_name}()')
    
    try:
        # Inicializar el caso de uso
        use_case = CharacterUseCase()
        # Eliminar el personaje
        success = use_case.delete(character_id)
        if not success:
            error_message = f'Personaje con ID {character_id} no encontrado para eliminar'
            logging.warning(error_message)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_message)   
        success_message = f'Personaje con ID {character_id} eliminado exitosamente'
        logging.info(success_message)
        logging.info(f'[#] Fin controllers - {function_name}()')
        return {"detail": success_message}
    except HTTPException as http_exception:
        # Capturamos excepción HTTPException y devolvemos el detalle
        logging.error(http_exception.detail)
        raise http_exception       
    except Exception as e:
        # Capturamos excepciónes diferentes a HTTPException y devolvemos el detalle
        error_message = f'Error al eliminar el personaje: {e}'
        logging.error(error_message)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_message)
