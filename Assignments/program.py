# my_programs.py

# program.py

# 1. Longest Consecutive Sequence (O(n) using dict)
def longest_consecutive_sequence():
    print("Program: Longest Consecutive Sequence (O(n) using dictionary)")
    print("""
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:  # start of a sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest
""")
    print("Test Case: longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4")
    print("Explanation: Sequence [1,2,3,4] has length 4.")


# 2. Trie Implementation
def trie_program():
    print("Program: Trie with insert and search_prefix")
    print("""
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = True  # end marker

    def search_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
""")
    print("Test Case: Insert ['apple','app']; search_prefix('app') -> True")
    print("Test Case: search_prefix('apt') -> False")
    print("Explanation: Dictionary-based trie stores words by characters.")


# 3. Power of Two (bit manipulation)
def power_of_two():
    print("Program: Check if Number is Power of Two")
    print("""
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
""")
    print("Test Case 1: is_power_of_two(8) -> True")
    print("Test Case 2: is_power_of_two(10) -> False")
    print("Explanation: Power of 2 has only one bit set.")


# 4. Shortest Path in Binary Matrix (BFS)
def shortest_path_matrix():
    print("Program: Shortest Path in Binary Matrix using BFS")
    print("""
from collections import deque

def shortest_path_binary_matrix(grid):
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]:
        return -1
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    queue = deque([(0,0,1)])
    visited = set((0,0))
    while queue:
        x,y,d = queue.popleft()
        if (x,y) == (n-1,n-1):
            return d
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0 and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append((nx,ny,d+1))
    return -1
""")
    print("Test Case: shortest_path_binary_matrix([[0,0,0],[1,1,0],[1,1,0]]) -> 4")
    print("Explanation: BFS explores all neighbors layer by layer.")


# 5. Reverse Words in String (manual)
def reverse_words():
    print("Program: Reverse Words in a String (no split/join)")
    print("""
def reverse_words_in_string(s):
    words, word, result = [], '', []
    for ch in s:
        if ch != ' ':
            word += ch
        elif word:
            words.append(word)
            word = ''
    if word: words.append(word)
    for i in range(len(words)-1, -1, -1):
        result.append(words[i])
    return ' '.join(result)
""")
    print("Test Case: reverse_words_in_string('  hello world  ') -> 'world hello'")
    print("Explanation: Builds words manually and reverses their order.")


# 6. Min Stack
def min_stack_program():
    print("Program: Min Stack with O(1) getMin")
    print("""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
""")
    print("Test Case: push [3,5,2,1], getMin -> 1; pop -> getMin -> 2")
    print("Explanation: min_stack keeps track of current minimums.")


# 7. Maximum Depth of Binary Tree
def max_depth_tree():
    print("Program: Maximum Depth of Binary Tree (recursion)")
    print("""
def max_depth(tree):
    if not tree: return 0
    return 1 + max(max_depth(tree[1]), max_depth(tree[2]))
""")
    print("Test Case: max_depth([1,[2,None,None],[3,[4,None,None],None]]) -> 3")
    print("Explanation: Recursively finds depth of left and right subtrees.")


# 8. Group Anagrams
def group_anagrams():
    print("Program: Group Anagrams using Dictionary")
    print("""
from collections import defaultdict

def group_anagrams(words):
    d = defaultdict(list)
    for w in words:
        key = tuple(sorted(w))
        d[key].append(w)
    return list(d.values())
""")
    print("Test Case: group_anagrams(['eat','tea','tan','ate','nat','bat']) -> [['eat','tea','ate'],['tan','nat'],['bat']]")
    print("Explanation: Uses sorted tuple as dictionary key.")


# 9. First Unique Character
def first_unique_char():
    print("Program: First Unique Character in String")
    print("""
def first_unique_character(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch,0)+1
    for i,ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
""")
    print("Test Case 1: first_unique_character('leetcode') -> 0")
    print("Test Case 2: first_unique_character('aabb') -> -1")
    print("Explanation: Uses dictionary for counts, scans twice.")


# 10. Sliding Window Maximum
def sliding_window_maximum():
    print("Program: Sliding Window Maximum using deque")
    print("""
from collections import deque

def max_sliding_window(nums, k):
    dq, result = deque(), []
    for i, n in enumerate(nums):
        while dq and dq[0] <= i-k:
            dq.popleft()
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if i >= k-1:
            result.append(nums[dq[0]])
    return result
""")
    print("Test Case: max_sliding_window([1,3,-1,-3,5,3,6,7],3) -> [3,3,5,5,6,7]")
    print("Explanation: Maintains deque of indices for sliding max.")
    