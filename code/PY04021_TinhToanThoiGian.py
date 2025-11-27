def toInt(s):
    ans = 0
    for x in s:
        ans = ans * 10 + int(x)
    return ans

def calTime(st, en):
    h = toInt(st[0:2])
    m = toInt(st[3:5])
    hh = toInt(en[0:2])
    mm = toInt(en[3:5])
    newh = hh - h
    newm = mm - m
    if newm < 0:
        newh -= 1
        newm += 60
    return newh * 60 + newm

class Customer:
    def __init__(self, id, name, st, en):
        self.id = id
        self.name = name
        self.playTime = calTime(st, en)
        self.h = self.playTime // 60
        self.m = self.playTime % 60

    def __str__(self):
        return f"{self.id} {self.name} {self.h} gio {self.m} phut"

def solve():
    n = int(input())
    a = []
    for i in range(n):
        id = input()
        name = input()
        st = input()
        en = input()
        a.append(Customer(id, name, st, en))
    a.sort(key=lambda x: -x.playTime)
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()