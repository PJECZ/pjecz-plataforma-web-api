# Plataforma Web API V2 - Pruebas de funcionalidad

Como un sencillo ejemplo, se levanta un servidor web con Flask, el cual entrega tablas vacias que por medio de DataTables se llenan con datos.

## Instalar Flask

    pip install flask

## Arrancar Flask

    export FLASK_APP=tests/app.py
    export FLASK_ENV=development
    flask run
