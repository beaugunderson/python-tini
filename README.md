## tini

A simple module for loading simple `ini` files.

### Example

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

```python
import settings

settings.foobar['baz'] == 'a string'
```
