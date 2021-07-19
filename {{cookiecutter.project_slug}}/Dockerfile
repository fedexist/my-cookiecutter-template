{% if cookiecutter.python_version == 'python3.8' %}
FROM python:3.8-slim
{% elif cookiecutter.python_version == 'python3.7' %}
FROM python:3.7-slim
{% endif %}

ARG PACKAGE_VERSION=dirty
ENV PACKAGE_VERSION=$PACKAGE_VERSION

LABEL mantainer="{{cookiecutter.full_name}} {{cookiecutter.email}}"\
      description="{{cookiecutter.project_short_description}}"

RUN echo "\
[install] \n\
index-url = https://pypi.python.org/simple/ \n\
extra-index-url = \n\
    http://pypi.advancedanalytics.generali.com/ge-it-aa/staging \n\
    http://pypi.advancedanalytics.generali.com/ge-it-aa/stable \n\
trusted-host = pypi.advancedanalytics.generali.com\
" > /etc/pip.conf

WORKDIR /{{cookiecutter.project_slug}}

RUN apt-get update -y && \
    python -m pip install {{cookiecutter.package_name}}==$PACKAGE_VERSION

ENTRYPOINT ["python", "-m", "{{cookiecutter.package_name}}.cli"]
