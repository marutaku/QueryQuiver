.PHONY: setup
setup:
	poetry install

.PHONY: test
test:
	poetry run pytest

.PHONY: lint
lint:
	poetry run pflake8
	poetry run black --check .
	poetry run isort --check .
	poetry run mypy .

.PHONY: format
format:
	poetry run black .
	poetry run isort .

.PHONY: build
build:
	poetry build