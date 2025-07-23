from setuptools import setup,find_packages
setup(
    name='smartformatter',
    version='0.1',
    package=find_packages(),
    install_requires=['inflect'],
    author='Sanjana',
    description='Utility functions for smart formatting of names,phones,numbers.',
)