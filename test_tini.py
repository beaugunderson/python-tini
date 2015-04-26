import io

from tini import Tini


def assert_test_ini(settings):
    """
    Assert for everything in ./test.ini.
    """
    assert settings.test['string'] == 'a string'
    assert settings.test['quoted-string-1'] == 'single quoted'
    assert settings.test['quoted-string-2'] == 'single quoted'
    assert settings.test['quoted-string-3'] == 'double quoted'
    assert settings.test['quoted-string-4'] == 'double quoted'
    assert settings.test['number'] == 123456789
    assert settings.test['boolean-true'] is True
    assert settings.test['boolean-false'] is False


def test_filenames():
    """
    Test basic argument coercion.
    """
    settings = Tini('./test.ini')

    assert_test_ini(settings)


def test_f():
    """
    Test loading from a file-like object.
    """
    settings = Tini(f=open('./test.ini'))

    assert_test_ini(settings)

    string_file = io.StringIO(io.open('./test.ini').read())

    settings = Tini(f=string_file)

    assert_test_ini(settings)
