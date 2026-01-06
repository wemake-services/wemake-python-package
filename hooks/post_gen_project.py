"""
This module is called after project is created.

From pydanny's cookiecutter-django:
https://github.com/pydanny/cookiecutter-django

"""

import subprocess  # noqa: S404
import textwrap
from pathlib import Path
from typing import Final

# Get the root project directory:
PROJECT_DIRECTORY = Path.cwd().resolve(strict=True)
PROJECT_NAME: Final = '{{ cookiecutter.project_name }}'

# We need these values to generate correct license:
LICENSE: Final = '{{ cookiecutter.license }}'
ORGANIZATION: Final = '{{ cookiecutter.organization }}'


def generate_license() -> None:
    """Generates license file for the project."""
    license_result = subprocess.check_output(  # noqa: S603
        [  # noqa: S607
            'lice',
            LICENSE.lower(),
            '-o',
            ORGANIZATION,
            '-p',
            PROJECT_NAME,
        ],
        universal_newlines=True,
        encoding='utf8',
    )
    with (PROJECT_DIRECTORY / 'LICENSE').open(
        mode='w',
        encoding='utf8',
    ) as license_file:
        license_file.write(
            license_result
            .strip()
            .replace(' \n ', ' \n')
            .replace('\n \n', '\n\n'),
        )
        license_file.write('\n')


def print_further_instructions() -> None:
    """Shows user what to do next after project creation."""
    message = """
    Your project {0} is created.
    Now you can start working on it:

        cd {0}
    """
    print(textwrap.dedent(message.format(PROJECT_NAME)))  # noqa: WPS421


generate_license()
print_further_instructions()
