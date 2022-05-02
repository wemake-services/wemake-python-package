# wemake-python-package

[![wemake.services](https://img.shields.io/badge/-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake-services.github.io)
[![Build status](https://github.com/wemake-services/wemake-python-package/workflows/test/badge.svg?branch=master&event=push)](https://github.com/wemake-services/wemake-python-package/actions?query=workflow%3Atest)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/wemake-services/wemake-python-package/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Bleeding edge [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) template to create new python packages.

---

## Purpose

This project is used to scaffold a `python` project structure.
Just like `poetry new` but better.


## Features

- Always [`up-to-date`](https://github.com/wemake-services/wemake-python-package/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot) dependencies with the help of [`@dependabot`](https://dependabot.com/)
- Supports latest `python3.7+`
- [`poetry`](https://github.com/python-poetry/poetry) for managing dependencies
- [`mypy`](https://mypy.readthedocs.io) for optional static typing
- [`pytest`](https://github.com/pytest-dev/pytest) for testing
- `flake8` and [`wemake-python-styleguide`](https://github.com/wemake-services/wemake-python-styleguide) for linting
- `Github Actions` as the default CI
- [`sphinx`](http://www.sphinx-doc.org/en/master/) and [`readthedocs.org`](https://readthedocs.org/) for documentation
- Easy update process, so your template will always be up-to-date


## Installation

Firstly, you will need to install dependencies:

```bash
pip install cookiecutter jinja2-git lice
```

Then, create a project itself:

```bash
cookiecutter gh:wemake-services/wemake-python-package
```

In order for the github actions to work smoothly (ie badge), you must, during the setup, use your github username in the `organization` field.
```bash
project_name [my-awesome-project]: foo-project
organization [wemake.services]: <github_username>
```


## Projects using it

Here's [a nice list of real-life open-source usages](https://github.com/search?q=wemake-python-package&type=Code)
of this template.


## License

MIT. See [LICENSE](https://github.com/wemake-services/wemake-python-package/blob/master/LICENSE) for more details.
