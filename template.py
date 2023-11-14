import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s):')

projectname = "TextSummerization"

list_files= [
    # created temporary files for main.yaml files
    ".github/workflow/.gitkeep",
    # logger code will be added to
    f"src/{projectname}/__init__.py",
    # Each stage code will be added in components {DataIntigrity}
    f"src/{projectname}/components/__init__.py",
    f"src/{projectname}/utils/__init__.py",
    # common code will be added to
    f"src/{projectname}/utils/common.py",
    f"src/{projectname}/config/__init__.py",
    # configuration for each stage code will be added
    f"src/{projectname}/config/configuration.py",
    # pipeline for the each stage code will be added
    f"src/{projectname}/pipeline/__init__.py",
    f"src/{projectname}/entity/__init__.py",
    # confiring the entities for each stage
    f"src/{projectname}/entity/config_entity.py",
    # Yaml files will be retrieved here
    f"src/{projectname}/constants/__init__.py",
    # All Stage Configuration will be added here
    "config/config.yaml",
    # parameters will be added here
    "params.yaml",
    # Data Schema will be added here
    "schema.yaml",
    # Runs All main stage pipeline here
    "main.py",
    # Application starts running from here by also calling main.py
    "app.py",
    "Dockerfile",
    # All the required libraries will be added here
    "requirements.txt",
    # Steup is added here to support components local
    "setup.py",
    # Notebook for each stage is tested here
    "research/trials.ipynb",
    # Frontend whole code is here
    "templates/index.html"
]

for filepath in list_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")

