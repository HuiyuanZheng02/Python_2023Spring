import math
def square_numbers(n=100):
    numbers = []
    for i in range(n+1):
        k = int(math.sqrt(i))
        if k * k == i:
            numbers.append(i)
    return numbers

def square_numbers2(n=100):
    numbers = []
    for i in range(int(math.sqrt(n)) + 1):
        numbers.append(i*i)
    return numbers

if __name__ == '__main__':
    numbers = square_numbers()
    print(numbers)
    numbers = square_numbers2()
    print(numbers)
