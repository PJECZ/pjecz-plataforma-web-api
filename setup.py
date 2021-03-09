"""
Setup
"""
from setuptools import setup


setup(
    name="cli",
    version="0.1",
    py_modules=[
        "cli.distritos",
        "cli.autoridades",
    ],
    entry_points="""
        [console_scripts]
        distritos=cli.distritos:cli
        autoridades=cli.autoridades:cli
    """,
)
