import runpy

from pathlib import Path
from setuptools import setup


this_dir = Path(__file__).parent.resolve()
version_file_path = this_dir / "pantry_supply_tracker/version.py"
version = runpy.run_path(str(version_file_path))["version"]

requirements = [
    "fastapi~=0.78.0",
    "pydantic~=1.9.1",
    "python-dotenv~=0.20.0",
    "uvicorn~=0.18.1",
]

setup(
    author="Maximilian Langknecht",
    name="Pantry Supply Tracker",
    install_requires=requirements,
    packages=["pantry_supply_tracker"],
    version=version,
)
