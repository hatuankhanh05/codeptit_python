mp = {}

def setup():
    global mp
    for i in range(10):
        mp[i] = str(i)
    c = ord('A')
    for i in range(10, 16):
        mp[i] = str(chr(c))
        c += 1

def binToDec(x):
    ans = 0
    for c in x:
        ans = ans * 2 + int(c)
    return ans

def binToBase(x, b):
    global mp
    ans = ''
    while x > 0:
        r = x % b
        ans = mp[r] + ans
        x //= b
    return ans

setup()
with open('DATA.in', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    T = int(lines[0].strip())
    i = 1
    for _ in range(T):
        n = int(lines[i].strip())
        x = lines[i + 1].strip()
        print(binToBase(binToDec(x), n))
        i += 2