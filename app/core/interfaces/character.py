from sqlalchemy.orm import Session
from app.db.sql.sqlalchemy.models.character import CharacterModel
from app.api.schemas.character import CharacterCreate
from app.db.sql.sqlalchemy.database import Database

class CharacterInterface:
    def __init__(self):
        """
        Inicializar la interface de personajes con una sesión de base de datos.
        """
        self.db_session = Database().SessionLocal()  # Inyección de dependencia de la sesión de la base de datos

    # Función para obtener todos los personajes
    def get(self):
        """
        Retorna todos los personajes de la base de datos.

        Returns:
            List[CharacterModel]: Lista de todos los personajes.
        """
        return self.db_session.query(CharacterModel).all()

    # Función para obtener un personaje por su ID
    def get_by_id(self, character_id: int):
        """
        Retorna un personaje por su ID de la base de datos.

        Args:
            character_id (int): ID del personaje.

        Returns:
            CharacterModel: El personaje correspondiente al ID proporcionado.
        """
        return self.db_session.query(CharacterModel).filter(CharacterModel.id == character_id).first()

    # Función para obtener un personaje por su nombre
    def get_by_name(self, character_name: str):
        """
        Retorna un personaje por su nombre de la base de datos.

        Args:
            character_name (str): Nombre del personaje.

        Returns:
            CharacterModel: El personaje correspondiente al nombre proporcionado.
        """
        return self.db_session.query(CharacterModel).filter(CharacterModel.name == character_name).first()

    # Función para crear un nuevo personaje
    def create(self, character: CharacterCreate):
        """
        Crea un nuevo personaje en la base de datos.

        Args:
            character (CharacterCreate): Datos del personaje a crear.

        Returns:
            CharacterModel: El personaje creado.
        """
        db_character = CharacterModel(**character.__dict__)  # Convertir la entidad de personaje en un modelo ORM
        self.db_session.add(db_character)  # Agregar el personaje a la sesión
        self.db_session.commit()  # Confirmar la transacción
        self.db_session.refresh(db_character)  # Actualizar la sesión para obtener los datos actualizados
        return db_character

    # Función para eliminar un personaje por su ID
    def delete(self, character_id: int):
        """
        Elimina un personaje por su ID en la base de datos.

        Args:
            character_id (int): ID del personaje a eliminar.

        Returns:
            bool: True si el personaje fue eliminado, False si no se encontró.
        """
        # Buscar el personaje por su ID
        db_character = self.db_session.query(CharacterModel).filter(CharacterModel.id == character_id).first()
        if db_character:  # Si se encuentra el personaje
            self.db_session.delete(db_character)  # Eliminar el personaje de la sesión
            self.db_session.commit()  # Confirmar los cambios en la base de datos
            return True  # Indicar que el personaje fue eliminado correctamente
        return False  # Indicar que el personaje no fue encontrado y no se eliminó
