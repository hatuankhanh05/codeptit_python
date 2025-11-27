class Student:
    def __init__(self, id, name, classid):
        self.id = id
        self.name = name
        self.classid = classid
        self.ag = 10

    def updateAg(self, s):
        for c in s:
            if c == 'v':
                self.ag -= 2
            elif c == 'm':
                self.ag -= 1
        self.ag = max(0, self.ag)
    
    def __str__(self):
        ans = f"{self.id} {self.name} {self.classid} {self.ag}"
        if self.ag == 0: ans += " KDDK"
        return ans

def solve():
    n = int(input())
    a = []
    for i in range(n):
        id = input()
        name = input()
        classid = input()
        a.append(Student(id, name, classid))
    for idx in range(n):
        s = input().split()
        for x in a:
            if x.id == s[0]:
                x.updateAg(s[1])
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()