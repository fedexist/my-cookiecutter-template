#!/usr/bin/env python
import os
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

__is_windows = os.name == 'nt'
__is_posix = os.name == 'posix'

PYTHON_COMMAND = '{{cookiecutter.python_version}}'
VENV_PYTHON_COMMAND = PYTHON_COMMAND
PIP_COMMAND = 'pip'

if __is_windows:
    PYTHON_COMMAND += '.exe'
    PIP_COMMAND += '.exe'

if __is_posix:
    ACTIVATE_VENV = 'source venv/bin/activate'
elif __is_windows:
    ACTIVATE_VENV = './venv/bin/activate'
else:
    raise OSError(f"Unsupported {os.name} OS, cannot activate any virtual environment")


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_folder(folder_path):
    shutil.rmtree(folder_path, ignore_errors=True)


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if '{{ cookiecutter.use_docker }}' != 'y':
        remove_file("Dockerfile")

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('src', '{{ cookiecutter.package_name }}', 'cli.py')
        remove_file(cli_file)

    if '{{ cookiecutter.use_gcf }}' != 'y':
        remove_folder('gcf')

    if '{{ cookiecutter.use_sql }}' != 'y':
        remove_folder('src/{{ cookiecutter.package_name }}/sql')

    if '{{ cookiecutter.init_venv }}' == 'y':
        print("Now initializing Python virtual environment...")
        os.system(f'{PYTHON_COMMAND} -m venv venv')

        print("Now installing development dependencies...")
        os.system(f'{ACTIVATE_VENV} && '
                  f'{PIP_COMMAND} install -r requirements_dev.txt')

        if '{{ cookiecutter.use_jupyter }}' == 'y':
            print("Now creating an IPyKernel based on the current Virtual "
                  "Environment named {{ cookiecutter.project_slug }}-venv...")
            os.system(f'{ACTIVATE_VENV} && '
                      f'{PIP_COMMAND} install --upgrade pip setuptools ipykernel && '
                      f'{VENV_PYTHON_COMMAND} -m ipykernel install --name={{ cookiecutter.project_slug }}-venv')
        else:
            remove_folder('ipynb')

    if '{{cookiecutter.init_git}}' == 'y':
        print("Now committing to git and creating git-hooks...")
        os.system('git init')
        os.system('mv git-hooks/* .git/hooks')
        remove_folder('git-hooks')
        os.system('git add .')
        os.system('git commit -am "Initial commit" --no-verify')
        print("Installing pre-commit hooks using .pre-commit-config.yaml")
        os.system(f'{ACTIVATE_VENV} && pre-commit install')
    else:
        remove_folder('git-hooks')
