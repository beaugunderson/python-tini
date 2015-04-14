from tini import Tini


def test_coercion():
    """
    Test basic argument coercion.
    """
    settings = Tini('./test.ini')

    assert settings.test['string'] == 'a string'
    assert settings.test['quoted-string-1'] == 'single quoted'
    assert settings.test['quoted-string-2'] == 'single quoted'
    assert settings.test['quoted-string-3'] == 'double quoted'
    assert settings.test['quoted-string-4'] == 'double quoted'
    assert settings.test['number'] == 123456789
    assert settings.test['boolean-true'] is True
    assert settings.test['boolean-false'] is False
