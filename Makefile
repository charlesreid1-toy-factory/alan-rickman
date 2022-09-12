include common.mk

MODULES=src tests

all:
	@echo "no default make rule defined"

help:
	cat Makefile

lint:
	flake8 $(MODULES)
	black --check $(MODULES)

requirements:
	python3 -m pip install --upgrade -r requirements.txt

requirements-test:
	python3 -m pip install --upgrade -r requirements-test.txt

build: clean
	python3 setup.py build install

test:
	pytest -v

buildtest: clean build test

cleantest: clean requirements requirements-test build test

clean:
	rm -fr build dist __pycache__ *.egg-info/
