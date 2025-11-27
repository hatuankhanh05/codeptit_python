# import math

# def solve():
#     n, k = map(int, input().split())
#     s = input()
#     pos = []
#     for i in range(n):
#         if s[i] == '1':
#             pos.append(i)
#     if len(pos) == 0:
#         print("0/1")
#         return
#     nume = 0
#     l, r = 0, 0
#     for p in pos:
#         while l < len(pos) and p - pos[l] > k:
#             l += 1
#         while r + 1 < len(pos) and pos[r + 1] - p <= k:
#             r += 1
#         nume += (r - l + 1)
#     deno = n * n
#     g = math.gcd(nume, deno)
#     print(f"{nume // g}/{deno // g}")

# t = 1
# t = int(input())
# for _ in range(t):
#     solve()
import math

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    dq = []
    nume = 0
    for i in range(n):
        if s[i] == '1':
            dq.append(i)
            while len(dq) > 0 and dq[-1] - dq[0] > k:
                dq.pop(0)
            nume += len(dq) * 2 - 1
    deno = n * n
    g = math.gcd(nume, deno)
    print(f"{nume // g}/{deno // g}")