# gen-cmakelists [![Build Status](https://travis-ci.com/vpangaldus/gen-cmakelists.svg?branch=master)](https://travis-ci.com/vpangaldus/gen-cmakelists)
GenCMakeLists.py is a python script to generate simple CMakeLists.txt for C++ project.

## Getting Started
### Prerequisites
Setup python virtualenv if you prefer to do so.

### Installing
```
python setup.py install
```
## Usage
The script will generate CMakeLists.txt for C++ project. It, by default, uses CMake 3.11 and C++14 standard.
Currently, it only targets linux. User is still expected to modify and adjust all the neccessary information such as library name, path to library and so on. The script will help only on the repetitive stuffs.

To get help:
```
GenCMakeLists --help
```

To generate a simple app:
```
GenCMakeLists simple_app
```


## License
This project is licensed under the GPL License - see the [LICENSE](LICENSE) file for details

## Acknowledgements
* Click
* Jinja
* pytest
