from setuptools import setup

setup(
    name='fridump',
    version='1.0',
    description='Memory dumping tool for frida',
    packages=['fridump'],
    install_requires=[
        'frida'
        ],
    entry_points={
        'console_scripts': [
            'fridump=fridump.fridump:main',
        ],
    },
)