#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def test_unicode_encode():
    s1 = 'I love Python程序设计!'
    try:
        print(s1.encode('ascii', errors='strict'))
    except Exception as e:
        print(type(e), e)

    for error in ('ignore', 'replace', 'backslashreplace', 'xmlcharrefreplace', 'namereplace'):
        print("encoding with errors '%s'" % error)
        print(s1.encode('ascii', errors=error))


def test_unicode_decode():
    s1 = 'I love Python程序设计!'

    for char_set in ('ascii', 'gbk', 'utf-8'):
        b1 = s1.encode(char_set, errors='ignore')
        print('-' * 40)
        print("encoding to '%s':<%s>" % (char_set, b1))

        s2 = b1.decode(encoding=char_set, errors='ignore')
        print(s2)

        s3 = str(b1, encoding=char_set, errors='ignore')
        print(s3)

        if char_set == 'gbk':
            try:
                s4 = b1.decode(encoding='utf-8', errors='strict')
                print(s4)
            except Exception as e:
                print(type(e), e)


if __name__ == '__main__':
    test_unicode_encode()
    test_unicode_decode()
