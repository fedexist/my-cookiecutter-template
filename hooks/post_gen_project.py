#!/usr/bin/env python
import os
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

__is_windows = os.name == 'nt'
__is_posix = os.name == 'posix'

PYTHON_COMMAND = 'python{{cookiecutter.python_version}}'
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

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")
        remove_file("docs/authors.rst")

    if "{{ cookiecutter.use_docker }}" != "y":
        remove_file("Dockerfile")

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('src', '{{ cookiecutter.package_name }}', 'cli.py')
        remove_file(cli_file)

    print("Now initializing Python virtual environment...")
    os.system(f"{PYTHON_COMMAND} -m venv venv")

    print("Now installing development dependencies...")
    os.system(f"{ACTIVATE_VENV} && "
              f"{PIP_COMMAND} install -r requirements_dev.txt")

    print("Now committing to git and creating git-hooks...")
    os.system("git init")
    os.system("git add .")
    os.system("git commit -am \"Initial commit\" --no-verify")
    print("Installing pre-commit hooks using .pre-commit-config.yaml")
    os.system(f"{ACTIVATE_VENV} && pre-commit install")
