.. _troubleshooting:

===============
Troubleshooting
===============

.. note:: Can you help improve this file? `Edit this file`_
          and submit a pull request with your improvements!

.. _`Edit this file`: https://gitlab.advancedanalytics.generali.com/aa-generali-italia/aa-pypackage/blob/master/docs/troubleshooting.rst


Windows Issues
--------------

* Some people have reported issues using git bash; try using the Command Terminal instead.

* Virtual environments can sometimes be tricky on Windows. If you have Python 3.5 or above installed (recommended), this should get you a virtualenv named ``myenv`` created inside the current folder:

.. code-block:: powershell

    > c:\Python35\python -m venv myenv

Or:

.. code-block:: powershell

    > c:\Python35\python c:\Python35\Tools\Scripts\pyvenv.py myenv

* Some people have reported that they have to re-activate their virtualenv whenever they change directory, so you should remember the path to the virtualenv in case you need it.


I don't understand how any of this works
----------------------------------------

Here I'll put some useful reference as to how all of this works:

* Take a look at the documentation of `PyScaffold`_
* Take a look at how Pythons's `Setuptools`_ handles ``setup.cfg``
* Take a look at how you can use `bump2version`_ to manage versioned releases

.. _`PyScaffold`: https://pyscaffold.org/en/stable/
.. _`Setuptools`: https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html
.. _`bump2version`: https://pypi.org/project/bump2version/
