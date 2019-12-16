# {{ cookiecutter.project_name }}

[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services)
[![Build Status](https://travis-ci.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}.svg?branch=master)](https://travis-ci.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }})
[![Coverage](https://coveralls.io/repos/github/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/badge.svg?branch=master)](https://coveralls.io/github/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}?branch=master)
[![Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

{{ cookiecutter.project_description }}


## Features

- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)


## Installation

```bash
pip install {{ cookiecutter.project_name }}
```


## Examples

The usage is identical to `assert` keyword, but a function:

```python
from {{cookiecutter.project_name.lower().replace('-', '_')}}.example import some_function

print(some_function(3, 4))
# => 7
```

## License

[{{ cookiecutter.license }}](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/blob/master/LICENSE)


## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [{% gitcommit %}](https://github.com/wemake-services/wemake-python-package/tree/{% gitcommit %}). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/{% gitcommit %}...master) since then.
