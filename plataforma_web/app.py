"""
FastAPI App
"""
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from plataforma_web.routers.abogados.paths import router as abogados
from plataforma_web.routers.audiencias.paths import router as audiencias
from plataforma_web.routers.autoridades.paths import router as autoridades
from plataforma_web.routers.distritos.paths import router as distritos
from plataforma_web.routers.edictos.paths import router as edictos
from plataforma_web.routers.glosas.paths import router as glosas
from plataforma_web.routers.listas_de_acuerdos.paths import router as listas_de_acuerdos
from plataforma_web.routers.listas_de_acuerdos_acuerdos.paths import router as listas_de_acuerdos_acuerdos
from plataforma_web.routers.materias.paths import router as materias
from plataforma_web.routers.materias_tipos_juicios.paths import router as materias_tipos_juicios
from plataforma_web.routers.peritos.paths import router as peritos
from plataforma_web.routers.sentencias.paths import router as sentencias
from plataforma_web.routers.ubicaciones_expedientes.paths import router as ubicaciones_expedientes

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
app.include_router(materias_tipos_juicios, prefix="/materias_tipos_juicios")
app.include_router(peritos, prefix="/peritos")
app.include_router(sentencias, prefix="/sentencias")
app.include_router(ubicaciones_expedientes, prefix="/ubicaciones_expedientes")


@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "Hola. Soy 'Plataforma Web API' del Poder Judicial del Estado de Coahuila de Zaragoza."}
