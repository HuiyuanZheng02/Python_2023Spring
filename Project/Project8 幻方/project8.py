'''
2023-04-27
@HuiyuanZheng02
'''

def is_magic_square(matrix, normal=False, dup=False):
    """
    @description : to check if the matrix is a magic square
    @param matrix : a 2D list
    @param normal : to check if the matrix contains all numbers from 1 to n^2
    @param dup : to check if the matrix contains duplicate numbers
    @Returns : True or False
    """
    # Get the number of rows and columns in the matrix
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    
    # Check if the matrix is square
    if n_rows != n_cols:
        raise ValueError("The matrix is not square.")
    
    
    # Check if the matrix is a magic square
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(col) for col in zip(*matrix)]
    diagonal_sum1 = sum(matrix[i][i] for i in range(n_rows))
    diagonal_sum2 = sum(matrix[i][n_rows-i-1] for i in range(n_rows))

    # a set of numbers in the matrix
    nums = set(num for row in matrix for num in row)
    
    if normal:
        # Check if the parameters dup and normal are both True
        if dup:
            raise ValueError("The parameters dup and normal cannot be true at the same time.")

        # Check if the matrix contains all numbers from 1 to n^2
        if nums != set(range(1, n_rows**2+1)):
            return False
    
    # Check if the matrix contains duplicate numbers
    if not dup ^ (len(nums) == n_rows**2):
        return False

    # Check if the sums are equal to the expected sum
    if row_sums == col_sums == [diagonal_sum1] * n_rows == [diagonal_sum2] * n_rows:
        return True
    else:
        return False

def Test():
    test_case_non_square = [[1, 2, 3], [4, 5, 6]]
    test_case_normal_3 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    test_case_dup = [[6, 9, 9], [11, 8, 5], [7, 7, 10]]
    test_case_non_normal_or_dup = [[5, 12, 1], [2, 6, 10], [11, 0, 7]]
    test_case_normal_4 = [[8, 11, 14, 1], [13, 2, 7, 12], [3, 16, 9, 6], [10, 5, 4, 15]]
    test_case_normal_6 = [
        [28, 4, 3, 31, 35, 10],
        [36, 18, 21, 24, 11, 1], 
        [7, 23, 12, 17, 22, 30], 
        [8, 13, 26, 19, 16, 29], 
        [5, 20, 15, 14, 25, 32], 
        [27, 33, 34, 6, 2, 9]
        ]
    # Test cases for is_magic_square function
    # Test case 1: Non-square matrix
    try:
        is_magic_square(test_case_non_square)
    except ValueError:
        print("Test case 1 passed: Non-square matrix")
    else:
        print("Test case 1 failed: Non-square matrix")

    # Test case 2: Normal magic square - 3*3
    assert is_magic_square(test_case_normal_3, normal=True, dup=False) == True
    print("Test case 2 passed: Normal magic square - 3*3")

    # Test case 3: Normal magic square - 4*4
    assert is_magic_square(test_case_normal_4, normal=True, dup=False) == True
    print("Test case 3 passed: Normal magic square - 4*4")

    # Test case 4: Normal magic square - 6*6
    assert is_magic_square(test_case_normal_6, normal=True, dup=False) == True
    print("Test case 4 passed: Normal magic square - 6*6")

    # Test case 5: Non-magic square
    assert is_magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == False
    print("Test case 5 passed: Non-magic square")

    # Test case 6: Duplicate numbers in normal matrix
    # 测试用例的幻方矩阵中有重复数字，但是参数normal为True，所以返回False
    assert is_magic_square(test_case_dup, normal=True, dup=False) == False
    print("Test case 6 passed: Duplicate numbers in normal matrix")

    # Test case 7: Abnormal magic square with duplicate numbers
    # 测试用例的幻方矩阵中有重复数字，但是参数dup为True，所以返回True
    assert is_magic_square(test_case_dup, normal=False, dup=True) == True
    print("Test case 7 passed: Abnormal magic square with duplicate numbers")

    # Test case 8: Abnormal magic square with duplicate numbers but the parameters dup is False
    # 测试用例的幻方矩阵中有重复数字，但是参数dup为False，所以返回False
    assert is_magic_square(test_case_dup) == False
    print("Test case 8 passed: Abnormal magic square with duplicate numbers but the parameters dup is False")

    # Test case 9: No duplicate numbers in abnormal matrix
    # 测试用例的幻方矩阵中没有重复数字，但不满足各个整数恰好为1到N^2，参数normal为True，所以返回False
    assert is_magic_square(test_case_non_normal_or_dup, normal=True, dup=False) == False
    print("Test case 9 passed: No duplicate numbers in abnormal matrix")

    # Test case 10: Abnormal magic square without duplicate numbers
    # 测试用例的幻方矩阵中没有重复数字，但参数dup为True，所以返回False
    assert is_magic_square(test_case_non_normal_or_dup, normal=False, dup=True) == False
    print("Test case 10 passed: Abnormal magic square without duplicate numbers")

    # Test case 11: Abnormal magic square when normal and dup are both False
    # 测试用例的幻方矩阵中没有重复数字，但参数dup和normal都为False，所以返回True
    assert is_magic_square(test_case_non_normal_or_dup) == True
    print("Test case 11 passed: Abnormal magic square when normal and dup are both False")

    # Test case 12: The parameters dup and normal are both True
    try:
        is_magic_square(test_case_normal_3, normal=True, dup=True)
    except ValueError:
        print("Test case 12 passed: dup and normal cannot both be True")
    else:
        print("Test case 12 failed: dup and normal cannot both be True")

if __name__ == '__main__':
    Test()