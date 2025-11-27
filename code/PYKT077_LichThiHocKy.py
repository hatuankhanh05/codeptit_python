subj = {}

class CaThi:
    def __init__(self, id, mamh, ngay, gio, nhom):
        self.id = id
        self.ma = mamh
        self.mon = subj[mamh]
        self.ngay = ngay
        self.gio = gio
        self.y = int(ngay[6:])
        self.M = int(ngay[3:5])
        self.d = int(ngay[0:2])
        self.h = int(gio[0:2])
        self.m = int(gio[3:])
        self.nhom = nhom

    def __str__(self):
        return f"T{self.id:03d} {self.ma} {self.mon} {self.ngay} {self.gio} {self.nhom}"

def solve():
    n, m = map(int, input().split())
    global subj
    for _ in range(n):
        mamh = input().strip()
        tenmh = input().strip()
        subj[mamh] = tenmh
    a = []
    for _ in range(m):
        arr = input().split()
        a.append(CaThi(_ + 1, arr[0], arr[1], arr[2], arr[3]))
    a.sort(key=lambda x: (x.y, x.M, x.d, x.h, x.m, x.id))
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()