from app.api.controllers import character as controller

def get_characters():
    """
    Llama a la función en el controlador para obtener todos los personajes.

    Returns:
        list: Lista de personajes.
    """
    result = controller.get_all_characters()
    return result

def get_character():
    """
    Llama a la función en el controlador para obtener un personaje por su ID.

    Returns:
        dict: Detalles del personaje.
    """
    id = 2
    result = controller.get_character(id)
    return result
    
def create_character():
    """
    Llama a la función en el controlador para crear un nuevo personaje.

    Returns:
        dict: Detalles del personaje creado.
    """
    data = {
        "name": "Ironman",
        "height": 180,
        "mass": 80,
        "hair_color": "black",
        "skin_color": "with",
        "eye_color": "blue",
        "birth_year": 1980
    }
    result = controller.create_character(data)
    return result

def delete_character():
    """
    Llama a la función en el controlador para eliminar un personaje por su ID.

    Returns:
        str: Mensaje indicando el resultado de la eliminación.
    """
    id = 2
    result = controller.delete_character(id)
    return result  

def __main__():
    """
    Función principal para ejecutar las operaciones relacionadas con los personajes.
    """
    get_characters()
    get_character()
    create_character()
    delete_character()