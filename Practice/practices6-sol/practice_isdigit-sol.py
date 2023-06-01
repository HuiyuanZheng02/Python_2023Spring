"""
自己实现 isdigit/islower/isupper/isidentifier(text)

"""
import string
import random


def isdigit(text):
    if not text:
        return False
    for ch in text:
        if ch not in '0123456789':
            return False
    return True

def test_isdigit():
    print('testing isdigit(text)...', end='')
    assert isdigit('1234') == True
    assert isdigit('1234 ') == False
    assert isdigit('-1234') == False
    print('passed!')

def islower(text):
    if not text:
        return False
    for ch in text:
        if ch not in string.ascii_lowercase:
            return False
    return True

def test_islower():
    print('testing islower(text)...', end='')
    assert islower('') == False
    assert islower('1234') == False
    assert islower('ABC') == False
    assert islower('abc') == True
    print('passed!')

def isupper(text):
    if not text:
        return False
    for ch in text:
        if ch not in string.ascii_uppercase:
            return False
    return True

def test_isupper():
    print('testing islower(text)...', end='')
    assert isupper('') == False
    assert isupper('1234') == False
    assert isupper('ABC') == True
    assert isupper('abc') == False
    print('passed!')

VALID_IDENTIFIER_CHARS = string.ascii_letters + string.digits + '_'

def isidentifier(text):
    if not text:
        return False
    if text[0] != '_' and text[0] not in string.ascii_uppercase:
        return False
    # not (text[0] == '_' or text[0] in string.ascii_uppercase)
    for ch in text:
        if ch not in VALID_IDENTIFIER_CHARS:
            return False
    return True

def test_isidentifer():
    print('testing islower(text)...', end='')
    assert isidentifier('') == False
    assert isidentifier('_') == True
    assert isidentifier('1234') == False
    assert isidentifier('_ABC123b') == True
    assert isidentifier('abc') == True
    print('passed!')

if __name__ == '__main__':
    test_isdigit()
    test_islower()
    test_isupper()
    test_isidentifer()
