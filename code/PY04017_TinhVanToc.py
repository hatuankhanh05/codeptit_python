def genID(name, addr):
    ans = ""
    for x in addr.split():
        ans += x[0:1]
    for x in name.split():
        ans += x[0:1]
    return ans

def getNum(s):
    ans = 0
    for x in s:
        ans = ans * 10 + int(x)
    return ans

def calSpeed(en):
    if len(en) == 4: en = "0" + en
    h = getNum(en[0:2])
    m = getNum(en[3:5])
    timeTaken = h - 6 + m / 60
    return 120 / timeTaken

def rounding(x):
    ans = int(x)
    if x - ans >= 0.5: ans += 1
    return ans

class Racer:
    def __init__(self, name, addr, en):
        self.name = name
        self.addr = addr
        self.id = genID(name, addr)
        self.speed = calSpeed(en)
        
    def __str__(self):
        return f"{self.id} {self.name} {self.addr} {rounding(self.speed)} Km/h"

def solve():
    n = int(input())
    a = []
    for i in range(n):
        name = input()
        addr = input()
        en = input()
        a.append(Racer(name, addr, en))
    a.sort(key=lambda x: -x.speed)
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()