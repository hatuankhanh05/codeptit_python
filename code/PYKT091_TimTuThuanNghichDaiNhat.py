'''
    author: htkhanh05
    created at: 04.12.2025 17:20:00
'''
import sys

def isPalindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[n - 1 - i] != s[i]:
            return False
    return True

def solve():
    lines = None
    with open('VANBAN.in', 'r') as f:
        lines = f.readlines()
    # lines = sys.stdin.readlines()

    words = []
    for line in lines:
        for word in line.strip().split():
            words.append(word)

    freq = {}
    maxLength = -1

    for word in words:
        if isPalindrome(word):
            freq[word] = freq.get(word, 0) + 1
            if maxLength == -1 or maxLength < len(word):
                maxLength = len(word)

    for (key, val) in freq.items():
        if len(key) == maxLength:
            print(key, val)

t = 1
#t = int(input())
for _ in range(t):
    solve()