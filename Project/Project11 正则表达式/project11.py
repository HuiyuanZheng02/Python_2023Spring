'''
2023-05-25
@HuiyuanZheng02
'''

import re, os
from collections import Counter

def main(file_name):
    '''
    @description: 统计文件中以元音字母开头，以ly, able, ful结尾的单词
    @param {str} file_name 文件名
    '''
    # Check if the input file exists
    if not os.path.exists(file_name):
        print(f"{file_name} does not exist.")
        return
    
    # Read the file
    with open(file_name, "r") as file:
        content = file.read()

    # Define the regex pattern for words starting with vowels (aieuo) and ending with ly, able, or ful
    pattern = r'\b[aeiouAEIOU][a-zA-Z]*?(?:ly|able|ful)\b'

    # Find all matching words in the content
    words = re.findall(pattern, content)

    # Count the occurrences of each word (case-insensitive)
    word_count = Counter(word.lower() for word in words)

    # Sort the words by their count in descending order
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Print the sorted words and their counts
    for index, (word, count) in enumerate(sorted_word_count, start=1):
        print(f"{index:>3}. {word:<20} {count}")

        
if __name__ == '__main__':
    main('treasure.txt')
'''
运行结果：
----------------------
  1. only                 91
  2. instantly            15
  3. entirely             11
  4. easily               8
  5. early                7
  6. exactly              6
  7. immediately          6
  8. evidently            5
  9. abominable           4
 10. utterly              4
 11. admirable            4
 12. agreeable            3
 13. ugly                 3
 14. actually             3
 15. usually              3
 16. obstinately          2
 17. apparently           2
 18. exceedingly          2
 19. unruly               2
 20. inexplicable         2
 21. angrily              1
 22. awful                1
 23. unmistakable         1
 24. indescribable        1
 25. absurdly             1
 26. annoyingly           1
 27. imaginable           1
 28. indomitable          1
 29. intolerable          1
 30. unmanly              1
 31. unsailorly           1
 32. originally           1
 33. useful               1
 34. unweariedly          1
 35. admiringly           1
 36. openly               1
 37. equally              1
 38. earnestly            1
 39. instinctively        1
 40. ally                 1
 41. invaluable           1
 42. evenly               1
 43. apologetically       1
 44. anxiously            1
 45. italy                1
 46. unearthly            1
 47. extremely            1
 48. innumerable          1
 49. infallibly           1
 50. idly                 1
 51. immensely            1
 52. ironically           1
 53. admirably            1
 54. uncomfortable        1
 55. obviously            1
 56. elderly              1
 57. oddly                1
 58. ungainly             1
 59. easterly             1
 60. impatiently          1
 61. ungrateful           1
 62. unfaithful           1
 63. obediently           1
 64. airily               1
 65. ungodly              1
 66. accordingly          1
 67. especially           1
'''