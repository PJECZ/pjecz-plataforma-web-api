"""
FastAPI App
"""
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from plataforma_web.v1.abogados.paths import router as abogados
from plataforma_web.v1.audiencias.paths import router as audiencias
from plataforma_web.v1.autoridades.paths import router as autoridades
from plataforma_web.v1.distritos.paths import router as distritos
from plataforma_web.v1.edictos.paths import router as edictos
from plataforma_web.v1.epocas.paths import router as epocas
from plataforma_web.v1.glosas.paths import router as glosas
from plataforma_web.v1.listas_de_acuerdos.paths import router as listas_de_acuerdos
from plataforma_web.v1.listas_de_acuerdos_acuerdos.paths import router as listas_de_acuerdos_acuerdos
from plataforma_web.v1.materias.paths import router as materias
from plataforma_web.v1.materias_tipos_juicios.paths import router as materias_tipos_juicios
from plataforma_web.v1.materias_tipos_juzgados.paths import router as materias_tipos_juzgados
from plataforma_web.v1.peritos.paths import router as peritos
from plataforma_web.v1.peritos_tipos.paths import router as peritos_tipos
from plataforma_web.v1.repsvm_agresores.paths import router as repsvm_agresores
from plataforma_web.v1.repsvm_delitos_especificos.paths import router as repsvm_delitos_especificos
from plataforma_web.v1.repsvm_delitos_genericos.paths import router as repsvm_delitos_genericos
from plataforma_web.v1.repsvm_tipos_sentencias.paths import router as repsvm_tipos_sentencias
from plataforma_web.v1.sentencias.paths import router as sentencias
from plataforma_web.v1.tesis_jurisprudencias.paths import router as tesis_jurisprudencias
from plataforma_web.v1.ubicaciones_expedientes.paths import router as ubicaciones_expedientes

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
app.include_router(epocas, prefix="/epocas")
app.include_router(glosas, prefix="/glosas")
app.include_router(listas_de_acuerdos, prefix="/listas_de_acuerdos")
app.include_router(listas_de_acuerdos_acuerdos, prefix="/listas_de_acuerdos_acuerdos")
app.include_router(materias, prefix="/materias")
app.include_router(materias_tipos_juicios, prefix="/materias_tipos_juicios")
app.include_router(materias_tipos_juzgados, prefix="/materias_tipos_juzgados")
app.include_router(peritos, prefix="/peritos")
app.include_router(peritos_tipos, prefix="/peritos_tipos")
app.include_router(repsvm_agresores, prefix="/repsvm_agresores")
app.include_router(repsvm_delitos_especificos, prefix="/repsvm_delitos_especificos")
app.include_router(repsvm_delitos_genericos, prefix="/repsvm_delitos_genericos")
app.include_router(repsvm_tipos_sentencias, prefix="/repsvm_tipos_sentencias")
app.include_router(sentencias, prefix="/sentencias")
app.include_router(tesis_jurisprudencias, prefix="/tesis_jurisprudencias")
app.include_router(ubicaciones_expedientes, prefix="/ubicaciones_expedientes")


@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "Hola. Soy 'Plataforma Web API' del Poder Judicial del Estado de Coahuila de Zaragoza."}
