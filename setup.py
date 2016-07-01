
from setuptools import setup, find_packages

setup(
    name='pycli',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click>=5.1',
    ],
    entry_points='''
        [console_scripts]
        pycli=mycli.cli:main
    ''',
)
