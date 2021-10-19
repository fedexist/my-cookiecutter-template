# -*- coding: utf-8 -*-
# """Top-level package for {{ cookiecutter.project_name }}."""

from pkg_resources import DistributionNotFound, get_distribution


__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"


try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = "{{ cookiecutter.version }}"
finally:
    del get_distribution, DistributionNotFound
