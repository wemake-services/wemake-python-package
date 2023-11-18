"""
This module is called after project is created.

From pydanny's cookiecutter-django:
https://github.com/pydanny/cookiecutter-django

"""

import os
import subprocess
import textwrap

# Get the root project directory:
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_NAME = '{{ cookiecutter.project_name }}'

# We need these values to generate correct license:
LICENSE = '{{ cookiecutter.license }}'
ORGANIZATION = '{{ cookiecutter.organization }}'


def generate_license():
    """Generates license file for the project."""
    license_result = subprocess.check_output([  # noqa: S603, S606
        'python',
        '-m',
        'lice',
        LICENSE.lower(),
        '-o',
        ORGANIZATION,
        '-p',
        PROJECT_NAME,
    ])
    with open(
        os.path.join(PROJECT_DIRECTORY, 'LICENSE'),
        mode='w',
        encoding='utf8',
    ) as license_file:
        license_file.write(license_result)


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
