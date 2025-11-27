def rounding(x):
    tmp = x - int(x)
    ans = int(x)
    return ans if tmp < 0.5 else ans + 1

def norm(x):
    if x > 10:
        return x / 10
    return x

class Candidate:
    def __init__(self, id, name, theo, prac):
        self.id = id
        self.name = name
        self.avg = (norm(theo) + norm(prac)) / 2
        gra = ""
        if self.avg >= 9.5:
            gra = "XUAT SAC"
        elif self.avg >= 8:
            gra = "DAT"
        elif self.avg >= 5:
            gra = "CAN NHAC"
        else:
            gra = "TRUOT"
        self.gra = gra

    def __str__(self):
        return f"TS0{self.id} {self.name} {self.avg:.2f} {self.gra}"

def solve():
    n = int(input())
    a = []
    for i in range(n):
        name = input()
        theo = float(input())
        prac = float(input())
        a.append(Candidate(i + 1, name, theo, prac))
    a.sort(key=lambda x: -x.avg)
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()