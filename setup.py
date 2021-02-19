"""
Setup
"""
from setuptools import setup, find_packages


setup(
    name="api",
    version="0.1",
    include_package_data=True,
    install_requires=[
        "fastapi==0.63.0",
        "gunicorn==20.0.4",
        "httptools==0.1.1",
        "PyMySQL==1.0.2",
        "psycopg2-binary==2.8.6",
        "pydantic==1.7.3",
        "SQLAlchemy==1.3.23",
        "uvicorn==0.13.3",
        "uvloop==0.14.0",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
)
