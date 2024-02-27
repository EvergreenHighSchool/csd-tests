from main import hello

names = ['alayna', 'frances', 'jeremy', 'justice', 'naima', 'cristian']
template = 'Hello, {}!'

def test_lower():
    """alayna -> Hello, alayna!"""
    for name in names:
        assert hello(name.lower()) == template.format(name.lower())


def test_upper():
    """ALAYNA -> Hello, ALAYNA!"""
    for name in names:
        assert hello(name.upper()) == template.format(name.upper())


def test_title():
    """Alayna -> Hello, Alayna!"""
    for name in names:
        assert hello(name.title()) == template.format(name.title())


def test_empty():
    """ '' -> 'Hello, World!' """
    assert hello('') == template.format('World')

def test_null():
    """ -> 'Hello, World!' """
    assert hello() == template.format('World')