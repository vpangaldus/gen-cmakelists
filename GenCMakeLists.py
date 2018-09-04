'''
A simple python script to generate simple CMakeLists.txt.
'''

import click
from jinja2 import Environment, FileSystemLoader

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('project_name')
@click.argument('cmakelists_file', type=click.File('w'),
                default='CMakeLists.txt',
                required=False)
@click.option('-l', '--libs', help='library to link with.')

def cli(project_name, cmakelists_file, libs):

    """
    Generate simple CMakeLists.txt\n
    example:
    \n\t * GenCMakeLists HelloWorld --libs Threads,Boost

    """

    # Jinja setup
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    t = env.get_template('cmakelists_base.txt')
    data = {}
    data['project_name'] = project_name

    if libs:
        data['libs'] = [c.strip() for c in libs.split(',')]

    # generate the CMakeLists.txt file
    click.echo(t.render(data=data), file=cmakelists_file)


