from setuptools import setup
from setuptools import find_packages

def parse_requirements():
    import os
    lib_folder = os.path.dirname(os.path.realpath(__file__))
    requirement_path = lib_folder + '/requirements.txt'
    if not os.path.exists(requirement_path):
        return []
    install_requires = []
    if os.path.isfile(requirement_path):
        with open(requirement_path) as f:
            install_requires = f.read().splitlines()
    return install_requires


setup(
    name='jorm',
    version='0.0.6',
    description='jarvis orm',
    packages=find_packages(
        exclude=['tests']
    ),
    install_requires=parse_requirements()
)
