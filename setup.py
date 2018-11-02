from setuptools import setup, find_packages

setup(
    name='GenCMakeLists',
    version="0.0.1",
    py_modules=['GenCMakeLists'],
    data_files=[('templates', ['templates/cmakelists_base.txt'])],
    install_requires=[
        'Click',
        'Jinja2',
        'pytest',
    ],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        GenCMakeLists=GenCMakeLists:cli
    '''
)
