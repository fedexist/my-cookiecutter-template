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
        cli_file = os.path.join('src', '{{ cookiecutter.package_name }}', 'cli.py')
        remove_file(cli_file)

    if '{{ cookiecutter.use_gcf }}' != 'y':
        remove_folder('gcf')

    if '{{ cookiecutter.use_sql }}' != 'y':
        remove_folder('src/{{ cookiecutter.package_name }}/sql')

    if '{{ cookiecutter.use_pycharm }}' != 'y':
        remove_folder('.idea')

    if '{{ cookiecutter.init_venv }}' == 'y':
        print("Now initializing Python virtual environment...")
        os.system('{{cookiecutter.python_version}} -m venv venv')

        print("Now installing development dependencies...")
        os.system('source venv/bin/activate && '
                  'pip install -r requirements_dev.txt')

        if '{{ cookiecutter.use_jupyter }}' == 'y':
            print("Now creating an IPyKernel based on the current Virtual Environment...")
            os.system('source venv/bin/activate && '
                      'pip install --upgrade pip setuptools ipykernel && '
                      'python -m ipykernel install --name={{ cookiecutter.project_slug }}-venv')
        else:
            remove_folder('ipynb')

    if '{{cookiecutter.init_git}}' == 'y':
        print("Now committing to git and creating git-hooks...")
        os.system('git init')
        os.system('mv git-hooks/* .git/hooks')
        remove_folder('git-hooks')
        os.system('git add .')
        os.system('git commit -am "Initial commit"')
    else:
        remove_folder('git-hooks')