import runpy

from pathlib import Path
from setuptools import find_packages
from setuptools import setup


this_dir = Path(__file__).parent.resolve()
version_file_path = this_dir / "src/version.py"
__version__ = runpy.run_path(str(version_file_path))["version"]

requirements = []

setup(
    author="Maximilian Langknecht",
    name="Pantry Supply Tracker",
    install_requires=requirements,
    packages=find_packages(),
    version=__version__,
)
