#!/usr/bin/env python
import os
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_folder(folder_path):
    shutil.rmtree(folder_path, ignore_errors=True)


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.package_name }}', 'cli.py')
        remove_file(cli_file)

    if '{{ cookiecutter.use_freedaa }}' == 'n':
        remove_folder('gcf')

    if '{{ cookiecutter.use_sql }}' == 'n':
        remove_folder('sql')

    if '{{cookiecutter.init_git}}' == 'y':
        os.system('git init')
        os.system('git add .')
        os.system('git commit -am "Initial commit"')