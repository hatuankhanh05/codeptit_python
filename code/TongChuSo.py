'''
    author: htkhanh05
    created at: 27.11.2025 13:07:48
'''

def solve():
    n = input()
    ans = 0
    while True:
        ans += 1
        sumOfDig = 0
        for c in n:
            sumOfDig += ord(c) - ord('0')
        n = str(sumOfDig)
        if len(n) < 2:
            break
    print(ans)

t = 1
#t = int(input())
for _ in range(t):
    solve()