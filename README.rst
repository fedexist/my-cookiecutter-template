=================================
Advanced Analytics Python Package
=================================

Cookiecutter_ template for a standard Python package, with optional FrEEdAA enabled, ready to be used
by our Generali Italia Advanced Analytics team, easy to use fot both Data Engineer and Data Scientist.

* Gitlab repo: https://gitlab.advancedanalytics.generali.com/aa-generali-italia/aa-pypackage
* Original GitHub repo: https://github.com/audreyr/cookiecutter-pypackage/
* Documentation: https://cookiecutter-pypackage.readthedocs.io/

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest``
* Jenkins-CI_: Ready for Jenkins Continuous Integration testing, including the deployment of the Google Cloud Function
  for FrEEdAA inference
* Tox_ testing: Setup to easily test for Python 3.5, 3.6, 3.7, 3.8
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_
* bump2version_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

.. _Cookiecutter: https://github.com/audreyr/cookiecutter


Quickstart
----------

.. note::
   Before you start using ``aa-pypackage``, make sure you have the commands python3.7 and python3.8 available in your PATH.

   In order to make sure of this, execute ``python3.7 --version`` and ``python3.8 --version``.

   If you don't have them installed, please install the required python distributions (by using ``brew``, ``pyenv`` or whatever it is
   your preferred method of installation) and/or set the appropriate aliases, if needed.


Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://gitlab.advancedanalytics.generali.com/aa-generali-italia/aa-pypackage
    # Or
    cookiecutter git@gitlab.advancedanalytics.generali.com:aa-generali-italia/aa-pypackage.git

Then:

* Create a repo and put it there.
* Create a Jenkins-CI_ pipeline on https://jenkins.advancedanalytics.generali.com.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Release your package by pushing a new tag to master.
* Update according to your needs the `setup.cfg` file, adding your project dependencies to its `install_requires` configuration

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives


If you already have your own `cookiecutter.json` file, then

1. Clone this repo
2. Replace or update with your values the provided cookiecutter.json file
3. Run ``cookiecutter aa-pypackage/ --no-input``

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _Jenkins-CI: https://www.jenkins.io/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _Read the Docs: https://readthedocs.io/
.. _bump2version: https://github.com/c4urself/bump2version
.. _Punch: https://github.com/lgiordani/punch
.. _Pipenv: https://pipenv.readthedocs.io/en/latest/
.. _PyPi: https://pypi.python.org/pypi
