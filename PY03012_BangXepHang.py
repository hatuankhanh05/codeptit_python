class Student:
    def __init__(self, name, c, t):
        self.name = name
        self.c = c
        self.t = t

    def __str__(self):
        return f"{self.name} {self.c} {self.t}"

n = int(input())
a = []
for _ in range(n):
    name = input()
    c, t = map(int, input().split())
    a.append(Student(name, c, t))
a.sort(key=lambda x: (-x.c, x.t, x.name))
for s in a:
    print(s)