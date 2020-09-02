{%- if cookiecutter.gcf_python_runtime == 'python38' -%}
FROM python:3.8
{%- elif cookiecutter.gcf_python_runtime == 'python37' -%}
FROM python:3.7
{% endif %}

LABEL mantainer="{{cookiecutter.full_name}} {{cookiecutter.email}}"\
      description="{{cookiecutter.project_short_description}}"

COPY {{cookiecutter.project_slug}} /{{cookiecutter.project_slug}}/
COPY config /{{cookiecutter.project_slug}}/
COPY bash /{{cookiecutter.project_slug}}/
COPY resources /{{cookiecutter.project_slug}}/
COPY setup.py /{{cookiecutter.project_slug}}/
COPY setup.cfg /{{cookiecutter.project_slug}}/

WORKDIR /{{cookiecutter.project_slug}}

RUN apt-get update -y && \
 python -m pip install .


ENTRYPOINT ["python", "-m", "{{cookiecutter.project_slug}}"]
