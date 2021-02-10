"""
Configuración para desarrollo
"""
import os


# PostgreSQL en Minos
DB_USER = os.environ.get("DB_USER", "nouser")
DB_PASS = os.environ.get("DB_PASS", "wrongpassword")
DB_NAME = os.environ.get("DB_NAME", "nodbname")
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

# CORS or "Cross-Origin Resource Sharing" refers to the situations when a frontend
# running in a browser has JavaScript code that communicates with a backend,
# and the backend is in a different "origin" than the frontend.
# https://fastapi.tiangolo.com/tutorial/cors/
ORIGINS = [
    "http://127.0.0.1",
    "http://localhost",
]
