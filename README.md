# Proyecto Challenge Python - Pi Data Strategy & Consulting

Este proyecto utiliza FASTAPI para crear un CRUD de personajes. El proyecto ha sido estructurado siguiendo los principios de Clean Architecture.

Este proyecto fue desarrollado por Jorge Fernández [https://www.linkedin.com/in/jfernandezgonzales/]

## Contenido

1. [Estructura del Proyecto](#estructura-del-proyecto)
2. [Tecnologias](#tecnologias)
3. [Configuración del Entorno Local](#configuración-del-entorno-local)
    1. [Clonar el repositorio](#clonar-el-repositorio)
    2. [Crear entorno virtual](#crear-entorno-virtual)
    3. [Instalar Dependencias](#instalar-dependencias)
    4. [Inicializar Aplicación](#inicializar-aplicación)
4. [Documentación de la API](#documentación-de-la-api)
5. [Implementación con Docker(Opcional)](#implementación-con-docker(opcional))

## Estructura del Proyecto

```
pi_challenge/
│
├── app/
│   ├── api/                 # Contiene controladores/routers/schemas/logging
│   │   ├── controllers/
│   │   │   └── character.py
│   │   ├── routers/
│   │   │   ├── character.py
│   │   │   ├── root.py
│   │   │   └── routes.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── character.py
│   │   └── logging.py
│   ├── core/                # Contiene lógica de negocio 
│   │   ├── interfaces/
│   │   │   └── character.py
│   │   └── use_cases/
│   │       └── character.py
│   ├── db/                  # Contendrá la interacción con la base de datos
│   │   ├── sql/
│   │   │   ├── sqlalchemy/
│   │   │   │   ├── models/
│   │   │   │   │   └── character.py
│   │   │   │   ├── database.py
│   │   │   │   └── init.py
│   ├── test/                # Pruebas de las APIs 
│   │   └── test_character.py
│   └── main.py              # Punto de entrada de la aplicación   
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

## Tecnologias

- **Python version**: 3.9 o superior
- **Framework**: FastAPI
- **Database**: SQLite

## Configuración del Entorno Local

### Clonar el repositorio

```bash
git clone <repository_url>
cd pi_challenge
```

### Crear entorno virtual

```bash
# Crear un entorno virtual
python -m venv nombre_entorno_virtual

# Activar entorno virtual (Windows)
.\nombre_entorno_virtual\Scripts\activate

# Activar entorno virtual (macOS/Linux)
source nombre_entorno_virtual/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Inicializar aplicación

```bash
uvicorn app.main:app --reload
```
La aplicación debería estar corriendo en http://127.0.0.1:8000.

## Documentación de la API
Esta ruta te lleva a Swagger UI, donde puedes interactuar con tu API de forma dinámica y explorar sus endpoints y parámetros :

- `/docs` para Swagger UI

La url para el Swagger UI es http://127.0.0.1:8000/docs

## Implementación con Docker(Opcional)

### Construir imagen de Docker

```bash
docker build -t pi_challenge .
```

### Inicializar contenedor Docker 

```bash
docker run -p 80:80 pi_challenge
```
