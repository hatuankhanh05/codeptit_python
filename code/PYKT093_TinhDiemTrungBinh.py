def chuanHoaTen(name):
    ans = []
    for x in name.split():
        ans.append(x.capitalize())
    return ' '.join(ans)

def lamTron(x):
    r = x - int(x)
    if r < 0.5:
        return int(x)
    else:
        return int(x) + 1

class Student:
    def __init__(self, id, name, sc1, sc2, sc3):
        self.id = id
        self.name = chuanHoaTen(name)
        self.tot = sc1 * 3 + sc2 * 3 + sc3 * 2
        self.avg = self.tot / 8
        
    def __str__(self):
        return f"SV{self.id:02d} {self.name} {lamTron(self.avg * 100) / 100:.2f}"

def solve():
    n = int(input())
    a = []
    for i in range(n):
        name = input().strip()
        sc1 = int(input())
        sc2 = int(input())
        sc3 = int(input())
        a.append(Student(i + 1, name, sc1, sc2, sc3))
    a.sort(key=lambda x: (-x.tot, x.id))
    lastTot = 0
    rank = 0
    for i in range(n):
        print(a[i], end = " ")
        if a[i].tot != lastTot:
            rank = i + 1
        lastTot = a[i].tot
        print(rank)

t = 1
# t = int(input())
for _ in range(t):
    solve()