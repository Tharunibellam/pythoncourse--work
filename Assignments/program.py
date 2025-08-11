# my_programs.py

# 1. Check if brackets are balanced
def check_balanced_brackets():
    print("🧠 Program: Check if Brackets are Balanced")
    print("""
def is_balanced(expr):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack
""")
    print("🧪 Test Case 1: is_balanced('{[()]}') -> True")
    print("🧪 Test Case 2: is_balanced('{[(])}') -> False")
    print("📝 Explanation: Uses a stack to ensure every opening bracket has a matching closing bracket in the correct order.")

# 2. Second largest number without sort
def second_largest():
    print("🧠 Program: Find Second Largest Number without sort()")
    print("""
def second_largest_number(lst):
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second
""")
    print("🧪 Test Case 1: second_largest_number([1,5,2,4]) -> 4")
    print("🧪 Test Case 2: second_largest_number([10,10,9]) -> 9")
    print("📝 Explanation: Tracks largest and second largest while iterating without sorting.")

# 3. Palindrome number
def palindrome_number():
    print("🧠 Program: Check if a Number is Palindrome")
    print("""
def is_palindrome(num):
    return str(num) == str(num)[::-1]
""")
    print("🧪 Test Case 1: is_palindrome(121) -> True")
    print("🧪 Test Case 2: is_palindrome(123) -> False")
    print("📝 Explanation: Converts number to string and checks if it equals its reverse.")

# 4. Count vowels and consonants
def vowels_consonants_count():
    print("🧠 Program: Count Vowels and Consonants")
    print("""
def count_vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    v_count = sum(1 for ch in s if ch.isalpha() and ch in vowels)
    c_count = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
    return v_count, c_count
""")
    print("🧪 Test Case 1: count_vowels_consonants('hello') -> (2, 3)")
    print("🧪 Test Case 2: count_vowels_consonants('Python') -> (1, 5)")
    print("📝 Explanation: Loops through characters and counts vowels/consonants separately.")

# 5. Binary search
def binary_search_program():
    print("🧠 Program: Binary Search Algorithm")
    print("""
def binary_search(lst, target):
    low, high = 0, len(lst)-1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
""")
    print("🧪 Test Case 1: binary_search([1,2,3,4,5], 4) -> 3")
    print("🧪 Test Case 2: binary_search([10,20,30,40], 25) -> -1")
    print("📝 Explanation: Repeatedly halves the search space to find the target index.")

# 6. Check duplicates without set
def contains_duplicates():
    print("🧠 Program: Check if List has Duplicates without set()")
    print("""
def has_duplicates(lst):
    seen = []
    for item in lst:
        if item in seen:
            return True
        seen.append(item)
    return False
""")
    print("🧪 Test Case 1: has_duplicates([1,2,3,1]) -> True")
    print("🧪 Test Case 2: has_duplicates([1,2,3]) -> False")
    print("📝 Explanation: Uses a list to keep track of seen elements and checks for repetition.")

# 7. All prime numbers in range
def primes_in_range():
    print("🧠 Program: Generate Prime Numbers in Range")
    print("""
def primes_between(start, end):
    primes = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes
""")
    print("🧪 Test Case 1: primes_between(10, 20) -> [11, 13, 17, 19]")
    print("🧪 Test Case 2: primes_between(1, 5) -> [2, 3, 5]")
    print("📝 Explanation: Loops through range and checks divisibility up to sqrt(n).")

# 8. Rotate matrix 90 degrees clockwise
def rotate_matrix():
    print("🧠 Program: Rotate Matrix 90° Clockwise")
    print("""
def rotate_matrix_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]
""")
    print("🧪 Test Case 1: rotate_matrix_90([[1,2],[3,4]]) -> [[3,1],[4,2]]")
    print("🧪 Test Case 2: rotate_matrix_90([[1,2,3],[4,5,6],[7,8,9]]) -> [[7,4,1],[8,5,2],[9,6,3]]")
    print("📝 Explanation: Reverses rows then transposes using zip().")

# 9. Check if two strings are permutations
def are_permutations():
    print("🧠 Program: Check if Two Strings are Permutations")
    print("""
def is_permutation(s1, s2):
    return sorted(s1) == sorted(s2)
""")
    print("🧪 Test Case 1: is_permutation('abc', 'cab') -> True")
    print("🧪 Test Case 2: is_permutation('hello', 'bello') -> False")
    print("📝 Explanation: Two strings are permutations if their sorted characters match.")

# 10. Pascal's triangle
def pascals_triangle():
    print("🧠 Program: Pascal's Triangle")
    print("""
def pascal_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
""")
    print("🧪 Test Case 1: pascal_triangle(3) -> [[1],[1,1],[1,2,1]]")
    print("🧪 Test Case 2: pascal_triangle(5) -> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]")
    print("📝 Explanation: Builds triangle row-by-row using values from previous row.")