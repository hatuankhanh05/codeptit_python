import math

def rounding(x):
    tmp = x - int(x)
    if tmp < 0.5:
        return int(x)
    else:
        return int(x) + 1

class Student:
    def __init__(self, id, name, a):
        self.id = id
        self.name = name
        self.a = a
        self.avg = 0.0
        cnt = 0
        for x in self.a:
            self.avg += x
            if cnt < 2: self.avg += x
            cnt += 1
        self.avg /= 12
        self.grade = ""
        if self.avg >= 9:
            self.grade = "XUAT SAC"
        elif self.avg >= 8:
            self.grade = "GIOI"
        elif self.avg >= 7:
            self.grade = "KHA"
        elif self.avg >= 5:
            self.grade = "TB"
        else:
            self.grade = "YEU"

    def __str__(self):
        return f"HS{self.id:02d} {self.name} {rounding(self.avg * 10) / 10:.1f} {self.grade}"

def solve():
    n = int(input())
    vec = []
    for i in range(n):
        name = input()
        a = list(map(float, input().split()))
        vec.append(Student(i + 1, name, a))
    vec.sort(key=lambda x: (-x.avg, x.id))
    for x in vec:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()