import string
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

"""
凯撒密码(caesar cipher)，其密钥为一个[1, 25]的整数，称为偏移量offset。
如果为英文字母，则其替换为后面偏移offset个位置的字符。最后一个字符z的下一个位置为从头开始的0。比如offset=3时，abcde分别替换为defgh，而uvwxyz替换为xyzab。

rot13是offset=13的凯撒密码，其加密和解密的算法都一样，都是替换为之后13个位置的字符
比如abcde经过13编码后为nopqr，而nopqr经过rot13编码后为abcde
"""

def caesar_encode(text, offset=13):
    encrypted = []
    for char in text:
        if char in string.ascii_lowercase:
            r_index = (ord(char) - ord('a') + offset) % 26
            encrypted.append(string.ascii_lowercase[r_index]) # chr(ord('a') + r_index)
        elif char in string.ascii_uppercase:
            r_index = (ord(char) - ord('A') + offset) % 26
            encrypted.append(string.ascii_uppercase[r_index])
        else:
            encrypted.append(char)

    return ''.join(encrypted)

def caesar_decode(crypt, offset=13):
    return caesar_encode(crypt, -offset)   # or 26- offset


def caesar_encode1(text, offset=13):
    """凯撒密码：每个英文字母替换为其后移动k个位置的英文字母
    """
    before = string.ascii_letters
    after = (string.ascii_lowercase[offset:] + string.ascii_lowercase[:offset] +
              string.ascii_uppercase[offset:] + string.ascii_uppercase[:offset])
    table = str.maketrans(before, after)
    return text.translate(table)

def caesar_decode1(text, offset=13):
    """凯撒密码：每个英文字母替换为其后移动k个位置的英文字母
    """
    before = string.ascii_letters
    after = (string.ascii_lowercase[offset:] + string.ascii_lowercase[:offset] +
              string.ascii_uppercase[offset:] + string.ascii_uppercase[:offset])
    table = str.maketrans(after, before)
    return text.translate(table)


if __name__ == '__main__':
    print(caesar_encode('abcde'))
    print(caesar_decode('nopqr'))
    print()

    print(caesar_encode(caesar_encode('Since rot thirteen is symmetric you should see this message')))
    print()

    offset = random.randrange(1, 26)
    print('offset={}'.format(offset))
    text1 = caesar_encode(string.ascii_letters, offset)
    print(text1)
    text2 = caesar_decode(text1, offset)
    print(text2)
