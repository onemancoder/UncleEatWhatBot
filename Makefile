.PHONY: run e2e-test

run:
	pipenv run python3 main.py

e2e-test:
	pipenv run python3 tests/e2e.py