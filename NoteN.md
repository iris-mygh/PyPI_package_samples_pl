# This is my simple Project
This is just a simple project to show the use of a package

# How to create python package and upload to PyPI

?? How to publish a python package to PyPI (pip)
### Create account:
- https://pypi.org/ 

### Create python package name “Simple_drawing”

PackagePyPI_sample/ Simple_drawing
```
PackagePyPI_sample/
        - Simple_drawing/
            - __init__.py
            - draw_circle.py
                draw_circle_with_symbol()
            
       - LICENSE.txt
       - setup.py
       - README.md
       - requirements.txt
       - test.py
       
```

### LICENSE.txt
- Open [link](https://choosealicense.com)  (Choose an open source license)

### setup.py
```
from setuptools import setup, find_packages
from os import path
working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Simple_drawing', # name of package
    version='0.0.1',
    url='https://github.com/yourname/yourproject',
    author='Iris',
    author_email='your_email@gmail.com',
    description='Simple test package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(), 
    auto_discover packages,
    install_requires=[],
)
```

- Run:
```
cd ./First_sample/
pip install –upgrade pip
pip install twine wheel setuptools
```
- Twine: Đăng tải gói của bạn lên PyPI một cách an toàn.
- Wheel: Xây dựng gói thành tệp .whl.
- Setuptools: Quản lý quá trình xây dựng và các phụ thuộc.

```
python setup.py sdist bdist_wheel
```
--> folders: build, dist, Simple_drawing.egg-info

- local test
```
cd ./PyPi_samples
pip install dist/Simple_drawing-0.0.1-py3-none-any.whl
python test.py
pip uninstall dist/Simple_drawing-0.0.1-py3-none-any.whl
```

- edit and rebuild: Simple_drawing==0.0.2:
```
1- .\PyPi_samples\Simple_drawing\__init__.py
    from .draw_circle import draw_circle_with_symbol

2- .\PyPi_samples\setup.py
setup(
    name='Simple_drawing',
    version='0.0.2',
    ...
    entry_points = {
        "console_script" : [
            "Simple_drawing = Simple_drawing : draw_circle_with_symbol",
        ],

    },
)

```
```
cd ./PyPi_samples
python setup.py sdist bdist_wheel
```

- upload to PyPI
```
cd ./PyPi_samples
twine upload dist/*
```
### Note: 
- Create Token: [link](https://pypi.org/manage/account/token/)
- Username: __token__
- Enter your API token: pypi-AgEIcHlwaS5vcmcCJDkzNmYxZDNhLTc2ODEtNDUyNS05ZmM2LTMyYjk1Y2Q5NmI4YwACKlszLCJhZWY3MTNhMC03ZjlmLTRhZmQtYjA3Ny00MjgyMzBlMTljZWIiXQAABiCK3NXHxpF_NZIsWHXCBoAsMCa36R6vFJhJHl53YJVDZQ

# References:
- Packaging Python Projects [link](https://packaging.python.org/en/latest/tutorials/packaging-projects/)