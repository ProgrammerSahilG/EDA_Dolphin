from setuptools import find_packages , setup
from typing import List



def get_requirements(file_path: str) -> list[str]:
    """
    This function reads a requirements file and returns a list of packages.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements



with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="eda_dolphin",          # PyPI package name
    version="0.1.0",
    author="Sahil Kumar",
    author_email="sahilkumar1851320@gmail.com",
    description="Comprehensive Exploratory Data Analysis Toolkit",
    long_description_content_type="text/markdown",
    url="https://github.com/ProgrammerSahilG/EDA_Dolphin.git",  # repo link
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements('requirements.txt')
    ,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires='>=3.9',
)

