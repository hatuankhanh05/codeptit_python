class HoaDon:
    def __init__(self, mamh, tenmh, sl, dg, ck):
        self.mamh = mamh
        self.tenmh = tenmh
        self.sl = sl
        self.dg = dg
        self.ck = ck
        self.tot = sl * dg - ck
    
    def __str__(self):
        return f"{self.mamh} {self.tenmh} {self.sl} {self.dg} {self.ck} {self.tot}"

def solve():
    n = int(input())
    a = []
    for _ in range(n):
        mamh = input()
        tenmh = input()
        sl = int(input())
        dg = int(input())
        ck = int(input())
        a.append(HoaDon(mamh, tenmh, sl, dg, ck))
    a.sort(key=lambda x: -x.tot)
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()