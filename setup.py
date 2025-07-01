# with the help of setup.py I'll be able to build my machine learning project as a package and even deploy in pypI from there anybody can do the installation and can use it"
from typing import List
from setuptools import find_packages,setup


HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # When this will try to read the requirements file a "/n" will also be readed to remove this with a blank we'll write a list comprehension 
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name="mlproject",
    version='0.0.1',
    author= 'Shivam',
    author_email="thisisshivam18@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('./requirements.txt')    
    )   