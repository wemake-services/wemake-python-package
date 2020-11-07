# {{ cookiecutter.project_name }}

[![Build Status](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/workflows/test/badge.svg?branch=master&event=push)](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/actions?query=workflow%3Atest)
[![Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

{{ cookiecutter.project_description }}


## Features

- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)
- Add yours!


## Installation

```bash
pip install {{ cookiecutter.project_name }}
```


## Example

Showcase how your project can be used:

```python
from {{cookiecutter.project_name.lower().replace('-', '_')}}.example import some_function

print(some_function(3, 4))
# => 7
```

## License

[{{ cookiecutter.license }}](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/blob/master/LICENSE)


## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [{% gitcommit %}](https://github.com/wemake-services/wemake-python-package/tree/{% gitcommit %}). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/{% gitcommit %}...master) since then.
