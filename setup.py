from setuptools import setup, find_packages

setup(
    name='calculator_package',
    version='0.1.0',
    author='Ivan',
    author_email='ibaeza40@gmail.com',
    description='A simple calculator package for basic arithmetic operations.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/irbaeza/desafio-criando-um-pacote-de-calculadora',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
