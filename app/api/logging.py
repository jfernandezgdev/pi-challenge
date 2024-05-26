import logging
import sys

def init_logging():
    """
    Configura el sistema de registro (logging) para el proyecto.

    Se configura el nivel de registro como INFO.
    El formato del registro incluye la marca de tiempo, el nivel de registro y el mensaje.
    Se agregan dos manejadores (handlers) de registro:
    1. logging.FileHandler para registrar mensajes en un archivo "logger.log".
    2. logging.StreamHandler para enviar mensajes al flujo de salida estándar (stdout).
    """   
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("logger.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )
