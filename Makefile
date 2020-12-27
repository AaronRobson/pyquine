.DEFAULT_GOAL := all

.PHONY: all
all: check test

.PHONY: clean
clean:
	rm -rf __pycache__/
	rm -rf .mypy_cache/

.PHONY: check
check: lint typecheck

.PHONY: lint
lint:
	flake8

.PHONY: typecheck
typecheck:
	mypy .

.PHONY: test
test: unittest confirm

.PHONY: unittest
unittest:
	python3 -m unittest

.PHONY: confirm
confirm:
	python3 quine.py | cmp quine.py

.PHONY: run
run:
	python3 quine.py
