SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	mypy {{ cookiecutter.project_name.lower().replace('-', '_') }} tests/**/*.py
	flake8 .
	doc8 -q docs

.PHONY: unit
unit:
	pytest

.PHONY: package
package:
	poetry check
	pip check
	safety check --bare --full-report

.PHONY: test
test: lint unit package
