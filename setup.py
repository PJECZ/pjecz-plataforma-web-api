"""
Setup
"""
from setuptools import setup


setup(
    name="plataforma_web_api",
    version="0.1",
    entry_points="""
        [console_scripts]
        plataforma_web_api=cli.cli:cli
    """,
)
