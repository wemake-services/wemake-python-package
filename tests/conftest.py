import pytest


@pytest.fixture
def context() -> dict[str, str]:
    """Creates default prompt values."""
    return {
        'project_name': 'test-project',
        'project_description': 'Custom description',
        'organization': 'custom-org',
        'license': 'MIT',
    }
