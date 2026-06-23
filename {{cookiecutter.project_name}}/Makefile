SHELL := /usr/bin/env bash
POETRY ?= poetry
.DEFAULT_GOAL := help

.PHONY: help
help: ## Show the help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: lint
lint: ## Run linting checks (ruff, flake8, mypy)
	$(POETRY) run ruff check --exit-non-zero-on-fix
	$(POETRY) run ruff format --check --diff
	$(POETRY) run flake8 .
	$(POETRY) run mypy .

.PHONY: unit
unit: ## Run unit tests with pytest
	$(POETRY) run pytest

.PHONY: package
package: ## Check package dependencies with pip
	$(POETRY) run pip check

.PHONY: test
test: lint package unit ## Run all checks (lint, unit, package)
