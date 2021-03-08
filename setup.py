"""
Setup
"""
from setuptools import setup, find_packages


setup(
    name="api",
    version="0.1",
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=3.8",
)
