## tini

A simple module for loading simple `ini` files.

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
