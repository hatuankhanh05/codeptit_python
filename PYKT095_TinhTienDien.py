mp = {
    "A": 100,
    "B": 500,
    "C": 200
}

def capitalizeName(name):
    y = []
    for x in name.split():
        y.append(x.capitalize())
    return ' '.join(y)

class Household:
    def __init__(self, id, name, ifmt):
        self.id = id
        self.name = capitalizeName(name)
        x = ifmt.split()
        type = x[0]
        sd = int(x[2]) - int(x[1])
        self.ttdm = min(sd, mp[type]) * 450
        self.tvdm = max(0, sd - mp[type]) * 1000
        self.vat = self.tvdm // 20
        self.tot = self.ttdm + self.tvdm + self.vat

    def __str__(self):
        return f"KH{self.id:02d} {self.name} {self.ttdm} {self.tvdm} {self.vat} {self.tot}"

def solve():
    n = int(input())
    a = []
    for i in range(n):
        name = input().strip()
        ifmt = input()
        a.append(Household(i + 1, name, ifmt))
    a.sort(key=lambda x: (-x.tot))
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()