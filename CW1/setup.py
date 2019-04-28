from setuptools import setup, find_packages

setup(
    name="The Alchemists Laboratory",
    version="0.1.0",
    author="Dáithí",
    packages=find_packages(exclude=['*tests']),
    install_requires=['argparse', 'pyyaml'],
    entry_points={
        'console_scripts': [
            'abracadabra = alchemist.command:process'
        ]})
