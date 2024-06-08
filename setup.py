from setuptools import setup, find_packages
from os import path

working_directory = path.abspath(path.dirname(__file__))
cwd = path.dirname(path.abspath(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requirements = open(path.join(cwd, "requirements.txt"), "r").readlines()

setup(
    name='Simple_drawing',
    version='0.0.1',
    url='https://github.com/path/project',
    author='LNKN',
    author_email='your_email@gmail.com',
    description='Simple_drawing test package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=requirements,
    entry_points = {
        "console_script" : [
            "Simple_drawing = Simple_drawing:draw_circle_with_symbol",
        ],

    },
)