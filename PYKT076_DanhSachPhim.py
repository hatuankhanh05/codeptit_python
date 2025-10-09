mp = {}

def getNum(s):
    ans = 0
    for x in s:
        ans = ans * 10 + int(x)
    return ans

class Phim:
    def __init__(self, id, matl, ngaykc, ten, sotap):
        self.id = id
        self.tl = mp[matl]
        self.ngaykc = ngaykc
        self.ten = ten
        self.sotap = sotap
        self.dd = getNum(ngaykc[0:2])
        self.mm = getNum(ngaykc[3:5])
        self.yyyy = getNum(ngaykc[6:])

    def __str__(self):
        return f"P{self.id:03d} {self.tl} {self.ngaykc} {self.ten} {self.sotap}"

def solve():
    n, m = map(int, input().split())
    global mp
    for _ in range(1, n + 1):
        id = f"TL{_:03d}"
        mp[id] = input().strip()
    a = []
    for _ in range(m):
        matl = input()
        ngaykc = input()
        ten = input()
        sotap = int(input())
        a.append(Phim(_ + 1, matl, ngaykc, ten, sotap))
    a.sort(key=lambda x: (x.yyyy, x.mm, x.dd, x.ten, -x.sotap))
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()