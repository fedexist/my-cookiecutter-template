PyPI Release Checklist
======================

Before Your First Release
-------------------------

#. Register the package on PyPI:

    .. code-block:: bash

        # Make sure your .pypirc is updated
        cat ~/.pypirc
        [distutils]
        index-servers =
            aapi-staging
            aapi-stable

        [aapi-staging]
        repository: pypi.advancedanalytics.generali.com/
        username: <username>
        password: <password>

        [aapi-stable]
        repository: pypi.advancedanalytics.generali.com/
        username: <username>
        password: <password>

        python setup.py register -r aapi-staging
        python setup.py register -r aapi-stable

#. Visit PyPI to make sure it registered.

For Every Release
-------------------

#. Update HISTORY.rst

#. Commit the changes:

    .. code-block:: bash

        git add HISTORY.rst
        git commit -m "Changelog for upcoming release 0.1.1."

#. Update version number (can also be patch or major)

    .. code-block:: bash

        bump2version minor

#. Install the package again for local development, but with the new version number:

    .. code-block:: bash

        python setup.py develop

#. Run the tests:

    .. code-block:: bash

        tox

#. Push the commit:

    .. code-block:: bash

        git push

#. Push the tags, creating the new release on both Gitlab and PyPI:

    .. code-block:: bash

        git push --tags

#. Check the PyPI listing page to make sure that the README, release notes, and roadmap display properly. If not, try one of these:

    #. Copy and paste the RestructuredText into http://rst.ninjs.org/ to find out what broke the formatting.

    #. Check your long_description locally:

        .. code-block:: bash

            pip install readme_renderer
            python setup.py check -r -s

#. Edit the release on Gitlab (e.g. https://gitlab.advancedanalytics.generali.com/aa-generali-italia/aa-pypackage/tags). Paste the release notes into the release's release page, and come up with a title for the release.

About This Checklist
--------------------

This checklist is adapted from:

* https://gist.github.com/audreyr/5990987
* https://gist.github.com/audreyr/9f1564ea049c14f682f4

It assumes that you are using all features of Cookiecutter PyPackage.
