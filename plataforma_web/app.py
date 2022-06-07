"""
FastAPI App
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

# V1 Catalogos
from .v1.autoridades.paths import autoridades as autoridades_v1
from .v1.distritos.paths import distritos as distritos_v1
from .v1.materias.paths import materias as materias_v1
from .v1.materias_tipos_juicios.paths import materias_tipos_juicios as materias_tipos_juicios_v1
from .v1.materias_tipos_juzgados.paths import materias_tipos_juzgados as materias_tipos_juzgados_v1

# V2 Catalogos
from .v2.autoridades.paths import autoridades as autoridades_v2
from .v2.distritos.paths import distritos as distritos_v2
from .v2.materias.paths import materias as materias_v2
from .v2.materias_tipos_juicios.paths import materias_tipos_juicios as materias_tipos_juicios_v2
from .v2.materias_tipos_juzgados.paths import materias_tipos_juzgados as materias_tipos_juzgados_v2

# Abogados registrados
from .v1.abogados.paths import abogados as abogados_v1
from .v2.abogados.paths import abogados as abogados_v2

# Audiencias
from .v1.audiencias.paths import audiencias as audiencias_v1
from .v2.audiencias.paths import audiencias as audiencias_v2

# Edictos
from .v1.edictos.paths import edictos as edictos_v1
from .v2.edictos.paths import edictos as edictos_v2

# Glosas
from .v1.glosas.paths import glosas as glosas_v1
from .v2.glosas.paths import glosas as glosas_v2

# Listas de Acuerdos
from .v1.listas_de_acuerdos.paths import listas_de_acuerdos as listas_de_acuerdos_v1
from .v2.listas_de_acuerdos.paths import listas_de_acuerdos as listas_de_acuerdos_v2
from .v1.listas_de_acuerdos_acuerdos.paths import listas_de_acuerdos_acuerdos as listas_de_acuerdos_acuerdos_v1
from .v2.listas_de_acuerdos_acuerdos.paths import listas_de_acuerdos_acuerdos as listas_de_acuerdos_acuerdos_v2

# Peritos
from .v1.peritos.paths import peritos as peritos_v1
from .v2.peritos.paths import peritos as peritos_v2
from .v1.peritos_tipos.paths import peritos_tipos as peritos_tipos_v1
from .v2.peritos_tipos.paths import peritos_tipos as peritos_tipos_v2

# REDAM
from .v2.redams.paths import redams as redams_v2

# REPSVM
from .v1.repsvm_agresores.paths import repsvm_agresores as repsvm_agresores_v1
from .v2.repsvm_agresores.paths import repsvm_agresores as repsvm_agresores_v2
from .v1.repsvm_delitos_especificos.paths import repsvm_delitos_especificos as repsvm_delitos_especificos_v1
from .v2.repsvm_delitos_especificos.paths import repsvm_delitos_especificos as repsvm_delitos_especificos_v2
from .v1.repsvm_delitos_genericos.paths import repsvm_delitos_genericos as repsvm_delitos_genericos_v1
from .v2.repsvm_delitos_genericos.paths import repsvm_delitos_genericos as repsvm_delitos_genericos_v2
from .v1.repsvm_tipos_sentencias.paths import repsvm_tipos_sentencias as repsvm_tipos_sentencias_v1
from .v2.repsvm_tipos_sentencias.paths import repsvm_tipos_sentencias as repsvm_tipos_sentencias_v2

# Sentencias
from .v1.sentencias.paths import sentencias as sentencias_v1
from .v2.sentencias.paths import sentencias as sentencias_v2

# Tesis y Jurisprudencias
from .v1.epocas.paths import epocas as epocas_v1
from .v2.epocas.paths import epocas as epocas_v2
from .v1.tesis_jurisprudencias.paths import tesis_jurisprudencias as tesis_jurisprudencias_v1
from .v2.tesis_jurisprudencias.paths import tesis_jurisprudencias as tesis_jurisprudencias_v2

# Ubicaciones de Expedientes
from .v1.ubicaciones_expedientes.paths import ubicaciones_expedientes as ubicaciones_expedientes_v1
from .v2.ubicaciones_expedientes.paths import ubicaciones_expedientes as ubicaciones_expedientes_v2

# Load configuration
try:
    from instance.settings import ORIGINS
except ImportError:
    from config.settings import ORIGINS

# FastAPI
app = FastAPI()

# CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Catalogos v1
app.include_router(autoridades_v1, prefix="/autoridades", tags=["catalogos"])
app.include_router(distritos_v1, prefix="/distritos", tags=["catalogos"])
app.include_router(epocas_v1, prefix="/epocas", tags=["catalogos"])
app.include_router(materias_v1, prefix="/materias", tags=["catalogos"])
app.include_router(materias_tipos_juicios_v1, prefix="/materias_tipos_juicios", tags=["catalogos"])
app.include_router(materias_tipos_juzgados_v1, prefix="/materias_tipos_juzgados", tags=["catalogos"])

# Catalogos v2
app.include_router(autoridades_v2, prefix="/v2/autoridades", tags=["catalogos"])
app.include_router(distritos_v2, prefix="/v2/distritos", tags=["catalogos"])
app.include_router(epocas_v2, prefix="/v2/epocas", tags=["catalogos"])
app.include_router(materias_v2, prefix="/v2/materias", tags=["catalogos"])
app.include_router(materias_tipos_juicios_v2, prefix="/v2/materias_tipos_juicios", tags=["catalogos"])
app.include_router(materias_tipos_juzgados_v2, prefix="/v2/materias_tipos_juzgados", tags=["catalogos"])

# Abogados registrados
app.include_router(abogados_v1, prefix="/abogados", tags=["abogados registrados"])
app.include_router(abogados_v2, prefix="/v2/abogados", tags=["abogados registrados"])

# Audiencias
app.include_router(audiencias_v1, prefix="/audiencias", tags=["agenda de audiencias"])
app.include_router(audiencias_v2, prefix="/v2/audiencias", tags=["agenda de audiencias"])

# Edictos
app.include_router(edictos_v1, prefix="/edictos", tags=["edictos"])
app.include_router(edictos_v2, prefix="/v2/edictos", tags=["edictos"])

# Glosas
app.include_router(glosas_v1, prefix="/glosas", tags=["glosas"])
app.include_router(glosas_v2, prefix="/v2/glosas", tags=["glosas"])

# Listas de Acuerdos
app.include_router(listas_de_acuerdos_v1, prefix="/listas_de_acuerdos", tags=["listas de acuerdos"])
app.include_router(listas_de_acuerdos_v2, prefix="/v2/listas_de_acuerdos", tags=["listas de acuerdos"])
app.include_router(listas_de_acuerdos_acuerdos_v1, prefix="/listas_de_acuerdos_acuerdos", tags=["listas de acuerdos"])
app.include_router(listas_de_acuerdos_acuerdos_v2, prefix="/v2/listas_de_acuerdos_acuerdos", tags=["listas de acuerdos"])

# Peritos
app.include_router(peritos_v1, prefix="/peritos", tags=["peritos"])
app.include_router(peritos_v2, prefix="/v2/peritos", tags=["peritos"])
app.include_router(peritos_tipos_v1, prefix="/peritos_tipos", tags=["peritos"])
app.include_router(peritos_tipos_v2, prefix="/v2/peritos_tipos", tags=["peritos"])

# REDAM
app.include_router(redams_v2, prefix="/redam", tags=["redam"])

# REPSVM
app.include_router(repsvm_agresores_v1, prefix="/repsvm_agresores", tags=["repsvm"])
app.include_router(repsvm_agresores_v2, prefix="/v2/repsvm_agresores", tags=["repsvm"])
app.include_router(repsvm_delitos_especificos_v1, prefix="/repsvm_delitos_especificos", tags=["repsvm"])
app.include_router(repsvm_delitos_especificos_v2, prefix="/v2/repsvm_delitos_especificos", tags=["repsvm"])
app.include_router(repsvm_delitos_genericos_v1, prefix="/repsvm_delitos_genericos", tags=["repsvm"])
app.include_router(repsvm_delitos_genericos_v2, prefix="/v2/repsvm_delitos_genericos", tags=["repsvm"])
app.include_router(repsvm_tipos_sentencias_v1, prefix="/repsvm_tipos_sentencias", tags=["repsvm"])
app.include_router(repsvm_tipos_sentencias_v2, prefix="/v2/repsvm_tipos_sentencias", tags=["repsvm"])

# Sentencias
app.include_router(sentencias_v1, prefix="/sentencias", tags=["sentencias"])
app.include_router(sentencias_v2, prefix="/v2/sentencias", tags=["sentencias"])

# Tesis y Jurisprudencias
app.include_router(epocas_v1, prefix="/epocas", tags=["tesis y jurisprudencias"])
app.include_router(epocas_v2, prefix="/v2/epocas", tags=["tesis y jurisprudencias"])
app.include_router(tesis_jurisprudencias_v1, prefix="/tesis_jurisprudencias", tags=["tesis y jurisprudencias"])
app.include_router(tesis_jurisprudencias_v2, prefix="/v2/tesis_jurisprudencias", tags=["tesis y jurisprudencias"])

# Ubicaciones de Expedientes
app.include_router(ubicaciones_expedientes_v1, prefix="/ubicaciones_expedientes", tags=["ubicaciones de expedientes"])
app.include_router(ubicaciones_expedientes_v2, prefix="/v2/ubicaciones_expedientes", tags=["ubicaciones de expedientes"])

# Add pagination
add_pagination(app)


@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "Hola. Soy 'Plataforma Web API' del Poder Judicial del Estado de Coahuila de Zaragoza."}
