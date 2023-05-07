from setuptools import setup, find_packages

setup(
    name='mysharedlib',
    version='0.1.0',
    description='Shared library for my Cloud Functions',
    packages=find_packages(),
    install_requires=[
        'google-cloud-secret-manager',
        'requests',
    ],
)
