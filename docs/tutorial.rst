Tutorial
========

.. note:: Did you find any of these instructions confusing? `Edit this file`_
          and submit a pull request with your improvements!

.. _`Edit this file`: https://gitlab.advancedanalytics.generali.com/aa-generali-italia/aa-pypackage/blob/master/docs/tutorial.rst

To start with, you will need a `Gitlab account`_. Create these before you get started on this tutorial. If you are new to Git and Gitlab, you should probably spend a few minutes on some of the tutorials at the top of the page at `Gitlab Help`_.

.. _`Gitlab account`: https://gitlab.advancedanalytics.generali.com
.. _`Gitlab Help`: https://gitlab.advancedanalytics.generali.com/help


Step 1: Install Cookiecutter
----------------------------

Alternative A: Use your python system distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install cookiecutter:

.. code-block:: bash

    pip install cookiecutter
    # It can be
    # python3.7 -m pip install cookiecutter
    # python3.8 -m pip install cookiecutter
    # Whatever suits your need, we only need the command cookiecutter to be installed on your system


Alternative B: Use a virtual environment for cookiecutter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, you need to create and activate a virtualenv for the package project. Use your favorite method, or create a virtualenv for your new package like this:

.. code-block:: bash

    virtualenv ~/.virtualenvs/mypackage

Here, ``mypackage`` is the name of the package that you'll create.

Activate your environment:

.. code-block:: bash

    source bin/activate

On Windows, activate it like this. You may find that using a Command Prompt window works better than gitbash.

.. code-block:: powershell

    > \path\to\env\Scripts\activate


Install cookiecutter:

.. code-block:: bash

    pip install cookiecutter


Step 2: Generate Your Package
-----------------------------

Now it's time to generate your Python package.

Use cookiecutter, pointing it at the cookiecutter-pypackage repo:

.. code-block:: bash

    cookiecutter https://gitlab.advancedanalytics.generali.com/aa-generali-italia/aa-pypackage.git

You'll be asked to enter a bunch of values to set the package up.
If you don't know what to enter, stick with the defaults.


Step 3: Create a Gitlab Repo
----------------------------

Go to your Gitlab account and create a new repo named ``mypackage``, where ``mypackage`` matches the ``[project_slug]`` from your answers to running cookiecutter. This is so that Travis CI and pyup.io can find it when we get to Step 5.

``If your virtualenv folder is within your project folder, be sure to add the virtualenv folder name to your .gitignore file.``

You will find one folder named after the ``[project_slug]``. Move into this folder, and then setup git to use your Gitlab repo and upload the code:

.. note:: The initialization and first commit shown here are not needed
          if you choose the option ``init_git`` while setting up your project

.. code-block:: bash

    cd mypackage
    git init .
    git add .
    git commit -m "Initial skeleton."
    git remote add origin git@gitlab.advancedanalytics.generali.com:aa-generali-italia/mypackage.git
    git push -u origin master

Where ``myusername`` and ``mypackage`` are adjusted for your username and package name.

You'll need a ssh key to push the repo. You can `Generate`_ a key or `Add`_ an existing one.

.. _`Generate`: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
.. _`Add`: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/


Step 4: Install Dev Requirements
--------------------------------

You should still be in the folder containing the ``requirements_dev.txt`` file.

Your virtualenv should still be activated. If it isn't, activate it now. Install the new project's local development requirements:

.. code-block:: bash

    pip install -r requirements_dev.txt

Step 5: Add your dependencies
-----------------------------

Add your dependencies in the ``setup.cfg`` file, in the section named ``install_requires``.


Step 6: Set Up Jenkins (Ask your DE!)
-------------------------------------

`Jenkins`_ is a continuous integration tool used to prevent integration problems. Every commit to the master branch will trigger automated builds of the application.

Follow the guide `provided in the Advanced Analytics wiki`_ to setup your Jenkins Pipeline.

.. _`Jenkins`: https://jenkins.advancedanalytics.generali.com
.. _`provided in the Advanced Analytics wiki`: https://aa-generali-italia.atlassian.net/wiki/spaces/DE/pages/1105592326/CI+CD+Gitlab+and+Jenkins?search_id=22711e42-46e3-4f8a-a2fd-aba090f21e3f#Jenkins-Setup


Step 7: Set Up Your Confluence Documentation Page
-------------------------------------------------

You can host your documentation on the Advanced Analytics wiki. Think of it as Continuous Documentation.

In order to do it, create a page within the DE space and use that name during the creation of your project
(``confluence_parent_page``).

Now, each time you'll push a commit, Jenkins will upload your documentation on Confluence.


Step 8: Release on PyPI
-----------------------

You may know Python Package Index or `PyPI`_ , the official third-party software repository for the Python programming language. Python developers intend it to be a comprehensive catalog of all open source Python packages.

Advanced Analytics has its own private PyPI, where we distribute our own packages, which you can find `here`_.

When you are ready, release your package the standard Python way.

See `PyPI Help`_ for more information about submitting a package.

You can refer to this documentation's page pypi_release_checklist to find out how to manage properly a Python package release.

.. _`PyPI`: https://pypi.python.org/pypi
.. _`PyPI Help`: http://peterdowns.com/posts/first-time-with-pypi.html
.. _`here`: http://pypi.advancedanalytics.generali.com/

Having problems?
----------------

Visit our :ref:`troubleshooting` page for help. If that doesn't help, go to our `Issues`_ page and create a new Issue. Be sure to give as much information as possible.

Alternatively, you can find me on Slack or Microsoft Teams (Federico D'Ambrosio)

.. _`Issues`: https://gitlab.advancedanalytics.generali.com/aa-generali-italia/aa-pypackage/issues
