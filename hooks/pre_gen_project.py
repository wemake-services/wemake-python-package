import re
import sys
from typing import Final

MODULE_REGEX: Final = r'^[a-z][a-z0-9\-]+[a-z0-9]$'
MODULE_NAME: Final = '{{ cookiecutter.project_name }}'


def _validate_project_name() -> None:
    """
    This validator is used to ensure that `project_name` is valid.

    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or hyphens.
    Ends with a lowercase letter or number.

    Valid example: `school_project3`.
    """
    if not re.match(MODULE_REGEX, MODULE_NAME):
        # Validates project's module name:
        message = [
            'ERROR: The project slug {0} is not a valid Python module name.',
            'Start with a lowercase letter.',
            'Followed by any lowercase letters, numbers or hyphens (-).',
            'End with a lowercase letter or number.',
        ]
        if '_' in MODULE_NAME:
            message.append('Do not use underscores (_) in your project name.')
        raise ValueError(' '.join(message).format(MODULE_NAME))


def _validate_deps() -> None:
    """Ensure that all deps are installed."""
    try:
        import lice  # noqa: F401, PLC0415
    except ImportError:
        raise RuntimeError(
            'lice is not installed, please install it before proceeding',
        ) from None

    try:
        import jinja2_git  # noqa: F401, PLC0415
    except ImportError:
        raise RuntimeError(
            'jinja2_git is not installed, please install it before proceeding',
        ) from None


validators = (
    _validate_project_name,
    _validate_deps,
)

for validator in validators:  # noqa: WPS481
    try:
        validator()
    except ValueError as ex:  # noqa: PERF203
        print(ex)  # noqa: WPS421
        sys.exit(1)
