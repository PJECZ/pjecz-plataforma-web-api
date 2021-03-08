"""
FastAPI App
"""
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from api.abogados.views import router as abogados
from api.autoridades.views import router as autoridades
from api.distritos.views import router as distritos
from api.listas_de_acuerdos.views import router as listas_de_acuerdos
from api.peritos.views import router as peritos
from api.ubicaciones_expedientes.views import router as ubicaciones_expedientes

try:
    from instance.settings import ORIGINS
except:
    from config.settings import ORIGINS

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(abogados, prefix="/abogados")
app.include_router(autoridades, prefix="/autoridades")
app.include_router(distritos, prefix="/distritos")
app.include_router(listas_de_acuerdos, prefix="/listas_de_acuerdos")
app.include_router(peritos, prefix="/peritos")
app.include_router(ubicaciones_expedientes, prefix="/ubicaciones_expedientes")


@app.get("/")
async def root():
    """ Mensaje de Bienvenida """
    return {"message": "Bienvenido. Soy la API de Plataforma Web."}
