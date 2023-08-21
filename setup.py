from setuptools import find_packages, setup
from typing import List

with open("README.md", "r") as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'emotion-detection'
AUTHOR_NAME = 'natek-1'
SRC_REPO = 'Emotion_Detection'
AUTHOR_EMAIL = 'nategabrielk@icloud.com'

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str='./requirements.txt')->List[str]:
    '''
    this funciton will return the list of requirements for this project
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements =file_obj.readlines()
        requirements = [req.replace("\n", '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small package that can read emotions from human images',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    packages=find_packages(),
    install_requires=get_requirements()
)