
def format_sequence1(n):
    """writing out the integers between 1 and n, separated by commas. """
    for i in range(1, n + 1):
        print('%d, ' % i, end='')
    print()

def format_sequence2(n):
    """writing out the integers between 1 and n, separated by commas. """
    for i in range(1, n + 1):
        if i < n:
            print('%d, ' % i, end='')
        else:
            print(i)

def format_sequence3(n):
    """writing out the integers between 1 and n, separated by commas. """
    print(1, end='')
    for i in range(2, n + 1):
        print(', %d' % i, end='')
    print()

def test_format_sequence():
    format_sequence1(10)
    format_sequence2(10)
    format_sequence3(10)

def multiprint1(s, times):
    """print a string a particular number of times, surrounded by parentheses, seperated by semicolons"""
    print('(', end='')
    for i in range(times):
        print('%s; ' % s, end='')
    print(')')

def multiprint2(s, times):
    """print a string a particular number of times, surrounded by parentheses, seperated by semicolons"""
    print('(', end='')
    for i in range(times):
        print(s, end='')
        if i < times - 1:
            print('; ', end='')
    print(')')

def multiprint3(s, times):
    """print a string a particular number of times, surrounded by parentheses, seperated by semicolons"""
    print('(', end='')
    print(s, end='')
    for i in range(times - 1):
        print('; %s' % s, end='')
    print(')')

def multiprint4(s, times):
    """print a string a particular number of times, surrounded by parentheses, seperated by semicolons"""
    if times <= 0:
        print('()')
        return
    print('(', end='')
    print(s, end='')
    for i in range(times - 1):
        print('; %s' % s, end='')
    print(')')


def test_multiprint():
    multiprint1('abc', 3)
    multiprint2('abc', 3)
    multiprint3('abc', 3)
    multiprint4('abc', 3)

    multiprint2('abc', 0)
    multiprint3('abc', 0)
    multiprint4('abc', 0)

if __name__ == '__main__':
    test_multiprint()
