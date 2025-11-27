def check(s):
    arr = s.split(".")
    if len(arr) != 4:
        return False
    for x in arr:
        if not x.isdigit():
            return False
        x = int(x)
        if x < 0 or x > 255:
            return False
    return True

def solve():
    s = input()
    print("YES" if check(s) else "NO")

T = int(input())
for _ in range(T):
    solve()