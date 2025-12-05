'''
    author: htkhanh05
    created at: 04.12.2025 16:57:34
'''
arr = []

def initArr():
    for i in range(10):
        arr.append(i)

    for i in range(6):
        arr.append(chr(ord('A') + i))

def binToDec(s):
    ans = 0
    for c in s:
        ans = ans * 2 + int(c)
    return ans

def decToBaseB(x, b):
    global arr
    ans = []
    while x > 0:
        ans.append(arr[x % b])
        x //= b
    ans.reverse()
    return ''.join([str(item) for item in ans])

def solve():
    lines = None
    with open('DATA.in', 'r') as f:
        lines = f.readlines()

    initArr()

    t = int(lines[0].strip())
    i = 1
    for _ in range(t):
        b = int(lines[i].strip())
        s = lines[i + 1].strip()
        i += 2
        if b == 2:
            print(s)
            continue
        print(decToBaseB(binToDec(s), b))

if __name__ == '__main__':
    solve()