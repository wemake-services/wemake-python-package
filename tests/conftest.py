# -*- coding: utf-8 -*-

import pytest


@pytest.fixture()
def context():
    """Creates default prompt values."""
    return {
        'project_name': 'test-project',
        'project_description': 'Custom description',
        'organization': 'custom-org',
        'license': 'MIT',
    }
