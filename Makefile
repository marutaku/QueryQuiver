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

.PHONY: install
install:
	pip install dist/*.whl

.PHONY: gen-docs
gen-docs:
	poetry run pdoc --output-dir docs query_quiver