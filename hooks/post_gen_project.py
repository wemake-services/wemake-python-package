"""
This module is called after project is created.

From pydanny's cookiecutter-django:
https://github.com/pydanny/cookiecutter-django

"""

import os
import sys
import textwrap

# Get the root project directory:
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_NAME = '{{ cookiecutter.project_name }}'

# We need these values to generate correct license:
LICENSE = '{{ cookiecutter.license }}'
ORGANIZATION = '{{ cookiecutter.organization }}'


def generate_license():
    """Generates license file for the project."""
    license_result = os.system(  # noqa: S605
        'lice {0} -o {1} -p {2} > {3}/LICENSE'.format(
            LICENSE.lower(),
            ORGANIZATION,
            PROJECT_NAME,
            PROJECT_DIRECTORY,
        ),
    )
    if license_result:  # it means that return code is not 0, print exception
        print(license_result)  # noqa: WPS421
        sys.exit(1)


def print_futher_instuctions():
    """Shows user what to do next after project creation."""
    message = """
    Your project {0} is created.
    Now you can start working on it:

        cd {0}
    """
    print(textwrap.dedent(message.format(PROJECT_NAME)))  # noqa: WPS421


generate_license()
print_futher_instuctions()
