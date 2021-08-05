"""
FastAPI App
"""
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from plataforma_web.abogados.views import router as abogados
from plataforma_web.audiencias.views import router as audiencias
from plataforma_web.autoridades.views import router as autoridades
from plataforma_web.distritos.views import router as distritos
from plataforma_web.edictos.views import router as edictos
from plataforma_web.glosas.views import router as glosas
from plataforma_web.listas_de_acuerdos.views import router as listas_de_acuerdos
from plataforma_web.listas_de_acuerdos_acuerdos.views import router as listas_de_acuerdos_acuerdos
from plataforma_web.materias.views import router as materias
from plataforma_web.peritos.views import router as peritos
from plataforma_web.sentencias.views import router as sentencias
from plataforma_web.ubicaciones_expedientes.views import router as ubicaciones_expedientes

try:
    from instance.settings import ORIGINS
except ImportError:
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
app.include_router(audiencias, prefix="/audiencias")
app.include_router(autoridades, prefix="/autoridades")
app.include_router(distritos, prefix="/distritos")
app.include_router(edictos, prefix="/edictos")
app.include_router(glosas, prefix="/glosas")
app.include_router(listas_de_acuerdos, prefix="/listas_de_acuerdos")
app.include_router(listas_de_acuerdos_acuerdos, prefix="/listas_de_acuerdos_acuerdos")
app.include_router(materias, prefix="/materias")
app.include_router(peritos, prefix="/peritos")
app.include_router(sentencias, prefix="/sentencias")
app.include_router(ubicaciones_expedientes, prefix="/ubicaciones_expedientes")


@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "Hola. Soy 'Plataforma Web API' del Poder Judicial del Estado de Coahuila de Zaragoza."}
