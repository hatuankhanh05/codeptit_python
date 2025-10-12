mp = {}

def calHs(id):
    if id[0] == "A":
        d = int(id[1:3])
        if d >= 16:
            return 20
        elif d >= 9:
            return 14
        elif d >= 4:
            return 12
        else:
            return 10
    if id[0] == "B":
        d = int(id[1:3])
        if d >= 16:
            return 16
        elif d >= 9:
            return 13
        elif d >= 4:
            return 11
        else:
            return 10
    if id[0] == "C":
        d = int(id[1:3])
        if d >= 16:
            return 14
        elif d >= 9:
            return 12
        elif d >= 4:
            return 10
        else:
            return 9
    d = int(id[1:3])
    if d >= 16:
        return 13
    elif d >= 9:
        return 11
    elif d >= 4:
        return 9
    else:
        return 8

class Employee:
    def __init__(self, id, name, lcb, snc):
        self.id = id
        self.name = name
        self.dpm = mp[id[3:]]
        hs = calHs(id)
        self.tot = hs * lcb * snc

    def __str__(self):
        return f"{self.id} {self.name} {self.dpm} {self.tot}000"

def solve():
    global mp
    n = int(input())
    for i in range(n):
        x = input().split()
        mp[x[0]] = ' '.join(x[1:])
    m = int(input())
    a = []
    for i in range(m):
        id = input()
        name = input()
        lcb = int(input())
        snc = int(input())
        a.append(Employee(id, name, lcb, snc))
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()