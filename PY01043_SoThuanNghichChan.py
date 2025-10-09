nums = []

def Try(n, s):
    for i in range(0, 10, 2):
        if len(s) < 1 and i == 0:
            continue
        new_s = s + str(i)
        if len(new_s) == n:
            nums.append(int(new_s + new_s[::-1]))
        else:
            Try(n, new_s)

def solve():
    n = int(input())
    for x in nums:
        if x >= n:
            break
        print(x, end = " ")
    print()

for i in range(1, 4):
    Try(i, "")
nums.sort()
t = 1
t = int(input())
for _ in range(t):
    solve()