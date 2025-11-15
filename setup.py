from setuptools import find_packages, setup
from typing import List
hypen_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        this function will return list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace("\n"," ") for req in requirements]
        if hypen_dot in requirements:
            requirements.remove(hypen_dot)
setup(
    name='Mlproject',
    version='0.0.1',
    author='Zain',
    author_email='zainulabdeenrizvi@gmail.com',
    install_requires= get_requirements('requirement.txt')
)