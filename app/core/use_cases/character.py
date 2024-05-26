import logging
from app.api.schemas.character import CharacterCreate
from app.core.interfaces.character import CharacterInterface

class CharacterUseCase:
    def __init__(self):
        """
        Inicializar el caso de uso de personajes con una interface.
        """
        # self.interface = interface  # Inyección de dependencia de la interface
        self.interface = CharacterInterface()  # Inyección de dependencia de la interface

    # Función para obtener todos los personajes
    def get_characters(self):
        """
        Retorna todos los personajes usando la interface.

        Returns:
            List[CharacterModel]: Lista de todos los personajes.
        """
        return self.interface.get()

    # Función para obtener un personaje por su ID
    def get_character(self, character_id: int):
        """
        Retorna un personaje por su ID usando la interface.

        Args:
            character_id (int): ID del personaje.

        Returns:
            CharacterModel: El personaje correspondiente al ID proporcionado.
        """
        return self.interface.get_by_id(character_id)

    # Función para obtener un personaje por su nombre
    def get_character_by_name(self, character_name: str):
        """
        Retorna un personaje por su nombre usando la interface.

        Args:
            character_name (str): Nombre del personaje.

        Returns:
            CharacterModel: El personaje correspondiente al nombre proporcionado.
        """
        return self.interface.get_by_name(character_name)

    # Función para crear un nuevo personaje
    def create(self, data: CharacterCreate):
        """
        Crea un nuevo personaje usando la interface.

        Args:
            data (CharacterCreate): Datos del personaje a crear.

        Returns:
            CharacterModel: El personaje creado.
        """
        logging.info(f"create: {data}")
        return self.interface.create(data)  # Guardar el personaje usando la interface
    
    # Función para eliminar un personaje por su ID
    def delete(self, character_id: int):
        """
        Elimina un personaje por su ID usando la interface.

        Args:
            character_id (int): ID del personaje a eliminar.

        Returns:
            bool: True si el personaje fue eliminado, False si no se encontró.
        """
        return self.interface.delete(character_id)  # Eliminar el personaje usando la interface

