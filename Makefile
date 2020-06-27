.PHONY: run e2e-test

run:
	pipenv run python3 main.py

test:
	pipenv run  python3 -m pytest tests/test_*.py  -v
e2e-test:
	pipenv run python3 tests/e2e.py