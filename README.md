## tini

A simple module for loading `.ini`-style configuration files.

Based on [ConfigParser][configparser] and works in Python 2 and Python 3.

[configparser]: https://docs.python.org/3/library/configparser.html

### Running tests

```bash
$ py.test
```

Or, with `tox` (test with multiple Python versions):

```bash
$ tox
```

### Example

#### settings.py

```python
import os
import sys

from tini import Tini

filenames = [
    './foobar.ini',
    os.path.join(os.path.expanduser('~'), '.foobar.ini'),
    os.path.join(os.path.expanduser('~'), '.config', '.foobar.ini'),
]

defaults = {
    'foobar': {
        'baz': 'a string',
        'buzz': True,
        'bizz': 123,
    }
}

sys.modules[__name__] = Tini(filenames, defaults=defaults)
```

#### foobar.ini

```
[foobar]
buzz = false
```

#### test.py

```python
import settings

assert settings.foobar['baz'] == 'a string'
assert settings.foobar['buzz'] is False
assert settings.foobar['baz'] == 123
```
