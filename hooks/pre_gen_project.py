import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.package_name}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)

    #Exit to cancel project
    sys.exit(1)


if '{{ cookiecutter.use_gcf }}' == 'y' and '{{ cookiecutter.gcf_python_runtime }}' not in {'python38', 'python37'}:
    print("ERROR: The chosen Google Cloud Function runtime (%s) is not valid. "
          "Please use one between 'python38' and 'python37'.".format('{{ cookiecutter.gcf_python_runtime }}'))
    sys.exit(1)