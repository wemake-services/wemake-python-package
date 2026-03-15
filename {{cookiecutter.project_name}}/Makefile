SHELL := /usr/bin/env bash
POETRY ?= poetry

.PHONY: lint
lint:
	$(POETRY) run ruff check --exit-non-zero-on-fix
	$(POETRY) run ruff format --check --diff
	$(POETRY) run flake8 .
	$(POETRY) run mypy .

.PHONY: unit
unit:
	$(POETRY) run pytest

.PHONY: package
package:
	$(POETRY) run pip check

.PHONY: test
test: lint package unit
