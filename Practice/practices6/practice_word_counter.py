"""
课堂上我们介绍了如何统计句子中单词的个数.单词由英文字母组成，其他字符只是用来分隔单词

现在改为得到句子中的各个单词，如何实现？

"""


def get_words(sentence):
    return sentence

if __name__ == '__main__':
    sentence = 'ascii_lower = string.ascii_lowercase'
    # 返回：['ascii', 'lower', 'string', 'ascii', 'lowercase']
    print(get_words(sentence))
