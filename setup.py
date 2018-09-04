from setuptools import setup, find_packages

setup(
    name='GenCMakeLists',
    version="0.0.1",
    packages=find_packages(),
    package_data={'': ['templates/*.txt']},
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
