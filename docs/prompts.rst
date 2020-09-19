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

freedaa_version
    Version of FrEEdAA to be used. Ignored if use_gcf == 'n'.

gcf_name
    Name of the Google Cloud Function to be deployed. Ignored if use_gcf == 'n'.

gcf_python_runtime
    Python runtime to be used by the Google Cloud Function. Ignored if use_gcf == 'n'.

gcf_trigger
    Trigger to be used by the Google Cloud Function (http, pubsub topic or gcs bucket). Ignored if use_gcf == 'n'.

gcf_topic
    PubSub topic to be used as trigger by the Google Cloud Function. Ignored if use_gcf == 'n'.

gcf_bucket
    Google Cloud Storage bucket to be used as trigger by the Google Cloud Function. Ignored if use_gcf == 'n'.

gcf_memory
    Memory to be used by the Google Cloud Function. Ignored if use_gcf == 'n'.

gcf_service_account
    Service Account to be impersonated by the Google Cloud Function. Ignored if use_gcf == 'n'.

project_bucket
    Bucket to be associated to the Google Cloud Function (it would contain the FrEEdAA trained pipeline). Ignored if use_gcf == 'n'.

pipeline_path
    Path within the specified project_bucket where we would find the FrEEdAA trained pipeline. Ignored if use_gcf == 'n'.

Options
-------

The following package configuration options set up different features for your project.

use_pytest
    Whether to use pytest as test suite.

command_line_interface
    Whether to create a console script using Click. Console script entry point will match the project_slug. Options: ['Click', "No command-line interface"]

use_gcf
    Whether to use FrEEdAA for the project and serving of the model