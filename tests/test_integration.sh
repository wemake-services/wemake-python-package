#!/usr/bin/env sh

set -o errexit
set -o nounset

# This file is used to setup fake project,
# run tests inside it,
# and remove this project completely.

# Creating a test directory:
mkdir -p "$HOME/.test" && cd "$HOME/.test"

# Scaffold the project:
PROJECT_NAME="fake-project"

cookiecutter "$GITHUB_WORKSPACE" \
  --no-input \
  --overwrite-if-exists \
  project_name="$PROJECT_NAME" \
  project_description="My custom app" \
  license="MIT" \
  organization="wemake.services"

cd "$PROJECT_NAME"

# Create new venv:
python -m venv .venv
# shellcheck disable=SC1091
. .venv/bin/activate
pip install -U pip

# Testing the project:
POETRY_VIRTUALENVS_CREATE=false poetry install
make test

# Extra tests for the infra:
pip install -U pre-commit
pre-commit run -a
