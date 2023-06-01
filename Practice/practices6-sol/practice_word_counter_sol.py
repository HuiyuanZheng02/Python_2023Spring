"""
课堂上我们介绍了如何统计句子中单词的个数，现在改为得到句子中的各个单词，如何实现？

"""
import string

def get_words(sentence):
    words = []
    inword = False
    for idx, c in enumerate(sentence):  #  0, ch
        if not inword: # False
            if c in string.ascii_letters: # start of word
                start = idx
                inword = True
        else: # True
            if c not in string.ascii_letters:
                inword = False
                word = sentence[start:idx]
                words.append(word)

    if c in string.ascii_letters:
        word = sentence[start:]
        words.append(word)
    return words

if __name__ == '__main__':
    sentence = 'ascii_lower = string.ascii_lowercase'
    # 返回：['ascii', 'lower', 'string', 'ascii', 'lowercase']
    print(get_words(sentence))
