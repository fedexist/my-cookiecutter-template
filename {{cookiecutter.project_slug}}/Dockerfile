{% if cookiecutter.python_version == 'python3.8' %}
FROM python:3.8-slim
{% elif cookiecutter.python_version == 'python3.7' %}
FROM python:3.7-slim
{% endif %}

{% if cookiecutter.release_pypi == 'y' %}
ARG PACKAGE_VERSION=dirty
ENV PACKAGE_VERSION=$PACKAGE_VERSION
{% endif %}
LABEL mantainer="{{cookiecutter.full_name}} {{cookiecutter.email}}"\
      description="{{cookiecutter.project_short_description}}"
{% if cookiecutter.release_pypi != 'y' %}
COPY src /{{cookiecutter.project_slug}}/
COPY setup.py /{{cookiecutter.project_slug}}/
COPY setup.cfg /{{cookiecutter.project_slug}}/
COPY .git /{{cookiecutter.project_slug}}/
{% else %}
RUN echo "\
[install] \n\
index-url = https://pypi.python.org/simple/ \n\
extra-index-url = \n\
    http://pypi.advancedanalytics.generali.com/ge-it-aa/staging \n\
    http://pypi.advancedanalytics.generali.com/ge-it-aa/stable \n\
trusted-host = pypi.advancedanalytics.generali.com\
" > /etc/pip.conf
{% endif %}

WORKDIR /{{cookiecutter.project_slug}}

RUN apt-get update -y && \
{% if cookiecutter.release_pypi != 'y' %}
    python -m pip install . && \
    rm -rf .git
{% else %}
    python -m pip install {{cookiecutter.package_name}}==$PACKAGE_VERSION
{% endif %}

ENTRYPOINT ["python", "-m", "{{cookiecutter.package_name}}.cli"]
