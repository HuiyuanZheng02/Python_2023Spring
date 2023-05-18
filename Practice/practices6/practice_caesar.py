import string
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

"""
凯撒密码(caesar cipher)，其密钥为一个[1, 25]的整数，称为偏移量offset。
如果为英文字母，则其替换为后面偏移offset个位置的字符。最后一个字符z的下一个位置为从头开始的0。比如offset=3时，abcde分别替换为defgh，而uvwxyz替换为xyzab。

rot13是offset=13的凯撒密码，其加密和解密的算法都一样，都是替换为之后13个位置的字符
比如abcde经过13编码后为nopqr，而nopqr经过rot13编码后为abcde

提示：可以有两种解法，(1) 利用ord+chr函数，(2) maketrans/translate
"""

def caesar_encode(text, offset=13):
    return text

def caesar_decode(crypt, offset=13):
    return crypt


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
