import click
from GenCMakeLists import cli
from click.testing import CliRunner
import os

cmakelist_simple_app = """
cmake_minimum_required(VERSION 3.11)
project(simple_app LANGUAGES CXX)
add_executable(simple_app main.cpp)
set_target_properties(simple_app PROPERTIES
    CXX_STANDARD 14
    CXX_STANDARD_REQUIRED YES
    CXX_EXTENSIONS NO
)
"""

cmakelist_app_with_threads = r"""
cmake_minimum_required(VERSION 3.11)

project(app LANGUAGES CXX)

find_package(Threads REQUIRED)

add_executable(app main.cpp)
set_target_properties(app PROPERTIES
    CXX_STANDARD 14
    CXX_STANDARD_REQUIRED YES
    CXX_EXTENSIONS NO
)

# Note:
# Please adjust the link dependencies, it is PUBLIC by default
target_link_libraries(app
  PUBLIC
    ${CMAKE_THREAD_LIBS_INIT}
)
"""

def test_help():
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0

def test_generate_simple_app():
    runner = CliRunner()
    result = runner.invoke(cli, ['simple_app'])
    with open('CMakeLists.txt','r') as f:
        read_data = f.read()
    f.close()
    os.remove('CMakeLists.txt')
    assert result.exit_code == 0
    assert read_data.split() == cmakelist_simple_app.split()

def test_generate_app_with_threads_libs():
    runner = CliRunner()
    result = runner.invoke(cli, ['app', '--libs', 'Threads'])
    with open('CMakeLists.txt','r') as f:
        read_data = f.read()
    f.close()
    os.remove('CMakeLists.txt')
    assert result.exit_code == 0
    #print(read_data)
    assert read_data.split() == cmakelist_app_with_threads.split()


	
