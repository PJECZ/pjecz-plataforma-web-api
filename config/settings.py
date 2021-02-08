"""
Configuración para producción
"""
import os


# MySQL en Google Cloud
DB_USER = os.environ.get("DB_USER", "nouser")
DB_PASS = os.environ.get("DB_PASS", "wrongpassword")
DB_NAME = os.environ.get("DB_NAME", "nodbname")
DB_SOCKET_DIR = os.environ.get("DB_SOCKET_DIR", "/cloudsql")
CLOUD_SQL_CONNECTION_NAME = os.environ.get("CLOUD_SQL_CONNECTION_NAME", "")
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@/{DB_NAME}?unix_socket={DB_SOCKET_DIR}/{CLOUD_SQL_CONNECTION_NAME}"
