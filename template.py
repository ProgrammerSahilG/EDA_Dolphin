import os
from pathlib import Path
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Project name
project_name = 'eda_dolphin'

# List of files to create
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_loader.py",
    f"src/{project_name}/components/stats.py",
    f"src/{project_name}/components/visualizer.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/helpers.py"
]

# Create folders and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            pass  # Create empty file
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

print("\n✅ EDA Dolphin project structure ready!")
