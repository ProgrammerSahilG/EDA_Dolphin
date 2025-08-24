from setuptools import find_packages , setup
from typing import List



def ger_requirements(file_path: str) -> list[str]:
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



  
setup(
    name='EDolphinA',
    version='0.1',
    author='Sahil Kumar',
    author_email='sahilkumar1851320@gmail.com',
    packages=find_packages(),
    install_requires= ger_requirements('requirements.txt')

)