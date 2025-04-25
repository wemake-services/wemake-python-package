SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run ruff check --exit-non-zero-on-fix --diff
	poetry run ruff format --check --diff
	poetry run flake8 .
	poetry run mypy .
	if poetry run command -v doc8 > /dev/null 2>&1; then poetry run doc8 -q docs; fi

.PHONY: unit
unit:
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check

.PHONY: test
test: lint package unit
