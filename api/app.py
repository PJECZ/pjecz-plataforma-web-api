"""
FastAPI App
"""
from pathlib import Path
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from api.abogados.views import router as abogados
from api.autoridades.views import router as autoridades
from api.distritos.views import router as distritos

if Path("instance/settings.py").exists():
    from instance.settings import SQLALCHEMY_DATABASE_URI
else:
    from config.settings import SQLALCHEMY_DATABASE_URI

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=SQLALCHEMY_DATABASE_URI)
app.include_router(abogados, prefix="/abogados")
app.include_router(autoridades, prefix="/autoridades")
app.include_router(distritos, prefix="/distritos")


@app.get("/")
async def root():
    """ Mensaje de Bienvenida """
    return {"message": "Bienvenido. Soy la API de Plataforma Web."}
