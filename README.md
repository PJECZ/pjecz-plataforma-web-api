# pjecz-plataforma-web-api

API de la Plataforma Web del PJECZ.

## Configurar VSCode

Cree .vscode/settings.json

    {
        "editor.formatOnSave": true,
        "python.linting.pylintArgs": ["--max-line-length", "256"],
        "python.formatting.provider": "black",
        "python.formatting.blackArgs": ["--line-length", "256"]
    }

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

Y luego instale los paquetes que requiere Plataforma Web

    pip install -r requirements.txt

Verifique con

    pip list

## FastAPI

Arrancar

    uvicorn --host=0.0.0.0 api.app:app --reload

Arrancar con gunicorn

    gunicorn -w 4 -k uvicorn.workers.UvicornWorker api.app:app
