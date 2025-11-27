class Subject:
    def __init__(self, id, name, typ):
        self.id = id
        self.name = name
        self.typ = typ

    def __str__(self):
        return self.id + " " + self.name + " " + self.typ

def solve():
    n = int(input())
    a = []
    for i in range(n):
        id = input()
        name = input()
        typ = input()
        a.append(Subject(id, name, typ))
    a.sort(key=lambda x: x.id)
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()