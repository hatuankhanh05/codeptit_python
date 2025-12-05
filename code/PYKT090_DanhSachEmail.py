'''
    author: htkhanh05
    created at: 04.12.2025 17:15:42
'''
import sys

def solve():
    lines = None
    with open('CONTACT.in', 'r') as f:
        lines = f.readlines()
    # lines = sys.stdin.readlines()

    emailSet = set()
    
    for line in lines:
        email = line.strip().lower()
        emailSet.add(email)

    ans = list(emailSet)
    ans.sort()
    for email in ans:
        print(email)

t = 1
#t = int(input())
for _ in range(t):
    solve()