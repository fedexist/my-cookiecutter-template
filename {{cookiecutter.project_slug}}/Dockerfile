{%- if cookiecutter.python_version == 'python38' -%}
FROM python:3.8
{%- elif cookiecutter.python_version == 'python37' -%}
FROM python:3.7
{% endif %}

LABEL mantainer="{{cookiecutter.full_name}} {{cookiecutter.email}}"\
      description="{{cookiecutter.project_short_description}}"

{%- if cookiecutter.release_pypi != 'y' -%}
COPY src /{{cookiecutter.project_slug}}/
COPY resources /{{cookiecutter.project_slug}}/
COPY setup.py /{{cookiecutter.project_slug}}/
COPY setup.cfg /{{cookiecutter.project_slug}}/
{%- else -%}
RUN echo -e "\
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
{%- if cookiecutter.release_pypi != 'y' -%}
 python -m pip install .
{%- else -%}
 python -m pip install {{cookiecutter.package_name}}
{% endif %}

ENTRYPOINT ["python", "-m", "{{cookiecutter.package_name}}"]
