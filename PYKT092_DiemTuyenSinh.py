kvv = [1.5, 1, 0]

def chuanHoaTen(s):
    ans = ""
    ss = s.split()
    cnt = 0
    length = len(ss)
    for x in ss:
        x1 = x[0:1]
        x1 = list(x1)
        if x1[0].islower():
            x1[0] = chr(ord(x1[0]) - 32)
        x2 = x[1:]
        x2 = list(x2)
        for i in range(len(x2)):
            if x2[i].isupper():
                x2[i] = chr(ord(x2[i]) + 32)
        x3 = ''.join(x1) + ''.join(x2)
        ans += x3
        if cnt != length - 1:
            ans += " "
        cnt += 1
    return ans

class ThiSinh:
    def __init__(self, id, ten, diem, dantoc, kv):
        self.id = id
        self.ten = chuanHoaTen(ten.strip())
        tot = diem + kvv[kv - 1]
        if dantoc != "Kinh": tot += 1.5
        self.tot = tot
        self.gra = ("Do" if tot >= 20.5 else "Truot")

    def __str__(self):
        return f"TS{self.id:02d} {self.ten} {self.tot} {self.gra}"

def solve():
    n = int(input())
    a = []
    for _ in range(n):
        ten = input()
        diem = float(input())
        dantoc = input()
        kv = int(input())
        a.append(ThiSinh(_ + 1, ten, diem, dantoc, kv))
    a.sort(key=lambda x: (-x.tot, x.id))
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()