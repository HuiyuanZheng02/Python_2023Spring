import string
import random
from functools import reduce

num_words = random.randint(1, 100)
words = [ ''.join(random.choices(string.ascii_letters, k=random.randint(0, 30))) for i in range(num_words)]
print('%d words' % len(words))

max_len = reduce(max, map(len, words))
max_len = max(map(len, words))
longest = reduce(lambda word1, word2: word1 if len(word1) > len(word2) else word2, words)
print(longest)
