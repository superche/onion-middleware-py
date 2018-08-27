# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='onion-middleware-py',
    version='0.1.0',
    description='Onion middleware for Python (2.7)',
    long_description=readme,
    author='Shaw Che',
    author_email='shawche@outlook.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
