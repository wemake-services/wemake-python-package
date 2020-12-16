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

# Removing the previous .venv dir and creating a new one:
rm -rf "$(poetry env info --path)"

# Testing the project:
poetry install
poetry run make test
