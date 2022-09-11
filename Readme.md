# alan-rickman


<img alt="version-0.1.0" src="https://img.shields.io/badge/version-0.1.0-orange" />

<img 
alt="tests-unittest" src="https://img.shields.io/badge/tests-unittest-green" /><img 
alt="tests-mock" src="https://img.shields.io/badge/tests-mock-green" /><img
alt="tests-pytest" src="https://img.shields.io/badge/tests-pytest-green" />

<img
alt="codestyle-black" src="https://img.shields.io/badge/codestyle-black-%23222222" /><img 
alt="codestyle-flake8" src="https://img.shields.io/badge/codestyle-flake8-blue" />

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

<img alt="python-3.9-3.10" src="https://img.shields.io/badge/python-3.9%7C3.10-blue" />

![Alan Rickman](docs/img/snape.jpg)

A Python project that wraps an authenticated API, and
implements tests with pytest and mock. Also demonstrates
how to separate offline and online tests, and safely
manage secrets.


## What's in this repo?

* `environment` - you must copy `environment.example` to `environment`
  and update the environment variable values before using this package.
  This environment file is ignored by git so that secrets are not accidentally
  added to the git repo.

    * Run `source environment` to load the variables.

* `src/` - contains a simple library wrapping a few calls to
  the GitHub API.  This API requires a GitHub API token to call.
  This package uses the [PyGithub](https://github.com/PyGithub/PyGithub)
  package under the hood.

    * Run `make requirements` to install dependencies.
    * Run `make build` to build and install the package.

* `tests/` - contains tests implemented with pytest and unittest.
  Tests are categorized as offline (standalone) or online (integration).
  Which tests are run is controlled by environment variables.

    * Run `make requirements-test` to install packages required for tests.
    * Update `environment` to control whether standalone or integration tests are run.
    * Run `make test` to run the test suite.


## Quick Start

```
git clone git@github.com:charlesreid1-toy-factory/alan-rickman.git
cd alan-rickman
```

Set up a virtual environment:

```
python3 -m virtualenv vp && source vp/bin/activate
```

Next, run `make requirements` to install dependencies.

Next, run `make build` to build and install the package.

Now you should be able to successfully import the package from Python:

```
$ python3

>>> import alan_rickman
>>>
```

Finally, to install the pre-commit hooks, run this command
from the command line from the repository root:

```
pre-commit install
```

This will install pre-commit checks as specified in `.pre-commit-config.yaml`.


## Running Tests

Follow this procedure to run the test suite.

Run `make requirements-test` to install packages required for tests.

Update `environment` to control whether standalone (offline) or integration (online)
tests are run.

Run `make test` to run the test suite.

**Note: Running standalone tests does not require a real GitHub API access token.
Integration tests do require a real access token. Any Github user's access token
will work.**


## Technologies Used

Core library:
* [PyGithub](https://github.com/PyGithub/PyGithub)

Tests:
* [unittest](https://docs.python.org/3/library/unittest.html)
* [Mock](https://docs.python.org/3/library/unittest.mock.html)
* [pytest](https://docs.pytest.org/en/7.1.x/)

Lint and style:
* [flake8](https://flake8.pycqa.org/en/latest/)
* [black](https://github.com/psf/black)
* [pre-commit](https://pre-commit.com/)


## Patterns Demonstrated

* Environment variables and `environment` file to safely manage secrets
  and access them from the program when needed
* Makefile, and associated useful Makefile patterns
* Pre-commit hooks to enforce linting and code style
* Pytest to run the test suite
* Separation of standalone and integation tests

(The use of the PyGithub library is not the feature of this repo,
but it is a really great library!)
