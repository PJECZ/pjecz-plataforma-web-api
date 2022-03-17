"""
FastAPI App
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from plataforma_web.v1.abogados.paths import abogados as abogados_v1
from plataforma_web.v1.audiencias.paths import audiencias as audiencias_v1
from plataforma_web.v1.autoridades.paths import autoridades as autoridades_v1
from plataforma_web.v1.distritos.paths import distritos as distritos_v1
from plataforma_web.v1.edictos.paths import edictos as edictos_v1
from plataforma_web.v1.epocas.paths import epocas as epocas_v1
from plataforma_web.v1.glosas.paths import glosas as glosas_v1
from plataforma_web.v1.listas_de_acuerdos.paths import listas_de_acuerdos as listas_de_acuerdos_v1
from plataforma_web.v1.listas_de_acuerdos_acuerdos.paths import listas_de_acuerdos_acuerdos as listas_de_acuerdos_acuerdos_v1
from plataforma_web.v1.materias.paths import materias as materias_v1
from plataforma_web.v1.materias_tipos_juicios.paths import materias_tipos_juicios as materias_tipos_juicios_v1
from plataforma_web.v1.materias_tipos_juzgados.paths import materias_tipos_juzgados as materias_tipos_juzgados_v1
from plataforma_web.v1.peritos.paths import peritos as peritos_v1
from plataforma_web.v1.peritos_tipos.paths import peritos_tipos as peritos_tipos_v1
from plataforma_web.v1.repsvm_agresores.paths import repsvm_agresores as repsvm_agresores_v1
from plataforma_web.v1.repsvm_delitos_especificos.paths import repsvm_delitos_especificos as repsvm_delitos_especificos_v1
from plataforma_web.v1.repsvm_delitos_genericos.paths import repsvm_delitos_genericos as repsvm_delitos_genericos_v1
from plataforma_web.v1.repsvm_tipos_sentencias.paths import repsvm_tipos_sentencias as repsvm_tipos_sentencias_v1
from plataforma_web.v1.sentencias.paths import sentencias as sentencias_v1
from plataforma_web.v1.tesis_jurisprudencias.paths import tesis_jurisprudencias as tesis_jurisprudencias_v1
from plataforma_web.v1.ubicaciones_expedientes.paths import ubicaciones_expedientes as ubicaciones_expedientes_v1

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

# Catalogos
app.include_router(autoridades_v1, prefix="/autoridades", tags=["catalogos"])
app.include_router(distritos_v1, prefix="/distritos", tags=["catalogos"])
app.include_router(materias_v1, prefix="/materias", tags=["catalogos"])
app.include_router(materias_tipos_juicios_v1, prefix="/materias_tipos_juicios", tags=["catalogos"])
app.include_router(materias_tipos_juzgados_v1, prefix="/materias_tipos_juzgados", tags=["catalogos"])

# Abogados registrados
app.include_router(abogados_v1, prefix="/abogados", tags=["abogados"])

# Agenda de Audiencias
app.include_router(audiencias_v1, prefix="/audiencias", tags=["audiencias"])

# Edictos
app.include_router(edictos_v1, prefix="/edictos", tags=["edictos"])

# Glosas
app.include_router(glosas_v1, prefix="/glosas", tags=["glosas"])

# Listas de Acuerdos
app.include_router(listas_de_acuerdos_v1, prefix="/listas_de_acuerdos", tags=["listas de acuerdos"])
app.include_router(listas_de_acuerdos_acuerdos_v1, prefix="/listas_de_acuerdos_acuerdos", tags=["listas de acuerdos"])

# Peritos
app.include_router(peritos_v1, prefix="/peritos", tags=["peritos"])
app.include_router(peritos_tipos_v1, prefix="/peritos_tipos", tags=["peritos"])

# REPSVM
app.include_router(repsvm_agresores_v1, prefix="/repsvm_agresores", tags=["repsvm"])
app.include_router(repsvm_delitos_especificos_v1, prefix="/repsvm_delitos_especificos", tags=["repsvm"])
app.include_router(repsvm_delitos_genericos_v1, prefix="/repsvm_delitos_genericos", tags=["repsvm"])
app.include_router(repsvm_tipos_sentencias_v1, prefix="/repsvm_tipos_sentencias", tags=["repsvm"])

# Sentencias
app.include_router(sentencias_v1, prefix="/sentencias", tags=["sentencias"])

# Tesis y Jurisprudencias
app.include_router(epocas_v1, prefix="/epocas")
app.include_router(tesis_jurisprudencias_v1, prefix="/tesis_jurisprudencias")

# Ubicaciones de Expedientes
app.include_router(ubicaciones_expedientes_v1, prefix="/ubicaciones_expedientes")

# Add pagination
add_pagination(app)

@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "Hola. Soy 'Plataforma Web API' del Poder Judicial del Estado de Coahuila de Zaragoza."}
