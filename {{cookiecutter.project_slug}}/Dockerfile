ARG BASE_IMAGE
FROM $BASE_IMAGE

ARG PACKAGE_VERSION=dirty
ENV PACKAGE_VERSION=$PACKAGE_VERSION

LABEL mantainer="{{cookiecutter.full_name}} {{cookiecutter.email}}"\
      description="{{cookiecutter.project_short_description}}"

WORKDIR /{{cookiecutter.project_slug}}

RUN --mount=type=secret,id=creds GOOGLE_APPLICATION_CREDENTIALS=/run/secrets/creds \
    python -m pip install {{cookiecutter.package_name}}==$PACKAGE_VERSION

RUN groupadd -r aa && useradd --no-log-init -r -s /bin/false -g aa aauser
RUN chown -R aauser:aa /{{cookiecutter.project_slug}} && \
    chmod -R ug+rwx /{{cookiecutter.project_slug}}
USER aauser

ENTRYPOINT ["python", "-m", "{{cookiecutter.package_name}}.cli"]
