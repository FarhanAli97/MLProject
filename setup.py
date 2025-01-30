from setuptools import find_packages, setup
from typing import List

# HYPEN_E_DOT='-e .'

def get_requirements(file_path:str) -> List[str]:

    """Read requirements file and return list of requirements"""
    
    requirements = []

    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace('\n', '') for req in requirements]

        # if HYPEN_E_DOT in requirements:
        #     requirements.remove(HYPEN_E_DOT)

        return requirements
    


setup(
    
    name='MLProject',
    version='0.0.1',
    author='Farhan',
    author_email='farhan.pro.pk@gmail.com',
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'scikit-learn', 'matplotlib', 'seaborn'],

)