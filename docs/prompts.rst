Prompts
=======

When you create a package, you are prompted to enter these values.

Templated Values
----------------

The following appear in various parts of your generated project.

full_name
    Your full name.

email
    Your email address.

python_version
    The Python version you want to use for your project. You can choose between python3.7 and python3.8 (Default is python3.8)

project_name
    The name of your new Python package project. This is used in documentation, so spaces and any characters are fine here.
    
project_slug
    The name of your directory. Typically, it is the slugified version of project_name.

package_name
    The namespace of your Python package. This should be Python import-friendly. Typically, it is the project_slug, but with '_' instead of '-'.

project_short_description
    A 1-sentence description of what your Python package does.

version
    The starting version number of the package.

gcp_project_id
    GCP project to be used by the Jenkinsfile and FrEEdAA

confluence_parent_page
    Name of the parent Confluent page under which the documentation will be published

freedaa_version
    Version of FrEEdAA to be used. **Ignored if use_gcf == 'n'**.

gcf_name
    Name of the Google Cloud Function to be deployed. **Ignored if use_gcf == 'n'**.

gcf_python_runtime
    Python runtime to be used by the Google Cloud Function. **Ignored if use_gcf == 'n'**.

gcf_trigger
    Trigger to be used by the Google Cloud Function (http, pubsub topic or gcs bucket). **Ignored if use_gcf == 'n'**.

gcf_topic
    PubSub topic to be used as trigger by the Google Cloud Function. **Ignored if use_gcf == 'n'**.

gcf_bucket
    Google Cloud Storage bucket to be used as trigger by the Google Cloud Function. **Ignored if use_gcf == 'n'**.

gcf_memory
    Memory to be used by the Google Cloud Function. **Ignored if use_gcf == 'n'**.

gcf_service_account
    Service Account to be impersonated by the Google Cloud Function. **Ignored if use_gcf == 'n'**.

project_bucket
    Bucket to be associated to the Google Cloud Function (it would contain the FrEEdAA trained pipeline). **Ignored if use_gcf == 'n'**.

pipeline_path
    Path within the specified project_bucket where we would find the FrEEdAA trained pipeline. **Ignored if use_gcf == 'n'**.

Options
-------

The following package configuration options set up different features for your project.

use_docker
    Whether you need a Docker image for you project

use_pytest
    Whether to use pytest as test suite.

init_git
    Whether you want to initialize a git repository with the start-up of the project. It will also configures some git-hooks to be used for pre-commit and pre-push.

init_venv
    Whether you want to initialize the project with a virtual environment with the basic dependencies.

use_sql
    Whether you're going to use sql queries within your project.

use_pycharm
    Whether you're going to use PyCharm as IDE.

release_pypi
    Whether you want your package to be released on pypi. This will update the Dockerfile and Jenkinsfile so that it will release a python package out of the project, that will be used within the Docker image as a simple 'pip install'

use_jupyter
    Whether your project will have jupyter notebooks. This option will add or remove a folder named 'ipynb', where you should be supposed to put your notebook files.

command_line_interface
    Whether to create a console script using Click. Console script entry point will match the project_slug. Options: ['Click', "No command-line interface"]

use_gcf
    Whether to deploy a Google Cloud Function for the project and serving of the model

use_freedaa
    Whether you're going to use FrEEdAA as dependency for your project. This will add freedaa as dependency in the setup.cfg file
