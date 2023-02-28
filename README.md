# pjecz-plataforma-web-api

API de la Plataforma Web del PJECZ.

## Configurar

Cree un archivo para las variables de entorno `.env`

    # Base de datos
    DB_USER=pjeczadmin
    DB_PASS=****************
    DB_NAME=pjecz_plataforma_web
    DB_HOST=127.0.0.1
    DB_PORT=5432

Para Bash Shell cree un archivo `.bashrc` con este contenido

    if [ -f ~/.bashrc ]; then
        source ~/.bashrc
    fi

    source venv/bin/activate
    if [ -f .env ]; then
        export $(grep -v '^#' .env | xargs)
    fi

    figlet Plataforma Web API
    echo

    echo "-- Database"
    echo "   DB_HOST: ${DB_HOST}"
    echo "   DB_PORT: ${DB_PORT}"
    echo "   DB_NAME: ${DB_NAME}"
    echo "   DB_PASS: ${DB_PASS}"
    echo "   DB_USER: ${DB_USER}"
    echo

    export PGDATABASE=${DB_NAME}
    export PGPASSWORD=${DB_PASS}
    export PGUSER=${DB_USER}
    echo "-- PostgreSQL"
    echo "   PGDATABASE: ${PGDATABASE}"
    echo "   PGPASSWORD: ${PGPASSWORD}"
    echo "   PGUSER:     ${PGUSER}"
    echo

    alias arrancar="uvicorn --port=8001 --reload plataforma_web.app:app"
    echo "-- Aliases"
    echo "   arrancar"
    echo

Cree el archivo `instance/settings.py` que cargue las variables de entorno

    """
    Configuración para desarrollo
    """
    import os


    DB_USER = os.environ.get("DB_USER", "wronguser")
    DB_PASS = os.environ.get("DB_PASS", "badpassword")
    DB_NAME = os.environ.get("DB_NAME", "pjecz_plataforma_web")
    DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
    DB_PORT = os.environ.get("DB_PORT", "5432")

    # PostgreSQL
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # CORS or "Cross-Origin Resource Sharing" refers to the situations when a frontend
    # running in a browser has JavaScript code that communicates with a backend,
    # and the backend is in a different "origin" than the frontend.
    # https://fastapi.tiangolo.com/tutorial/cors/
    ORIGINS = [
        "http://localhost:5000",
        "http://localhost:8001",
        "http://127.0.0.1:5000",
        "http://127.0.0.1:8001",
    ]

## Crear Entorno Virtual

Crear el enorno virtual dentro de la copia local del repositorio, con

    python -m venv venv

O con virtualenv

    virtualenv -p python3 venv

Active el entorno virtual, en Linux con...

    source venv/bin/activate

O en windows con

    venv/Scripts/activate

Verifique que haya el mínimo de paquetes con

    pip list

Actualice el pip de ser necesario

    pip install --upgrade pip

Y luego instale los paquetes requeridos

    pip install -r requirements.txt

Verifique con

    pip list

## FastAPI

Arrancar con uvicorn

    uvicorn --host=0.0.0.0 --port 8001 --reload plataforma_web.app:app

O arrancar con gunicorn

    gunicorn -w 4 -k uvicorn.workers.UvicornWorker plataforma_web.app:app
