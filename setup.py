from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'     # -e is the indication that requirements.txt is mapped to setup.py

def get_requirements(file_path:str)->List[str]:

    '''this funtion will return the list of requirements'''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
name = "ML version",
version = "0.0.1",
author="Siddarth",
author_email="siddarthnayak299@gmail.com",
packages=find_packages(),              # It will search for __init__ and try to build it 
install_requires=get_requirements('requirements.txt')
)
