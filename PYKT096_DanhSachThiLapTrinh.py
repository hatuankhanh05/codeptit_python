b = []

class Candidate:
    def __init__(self, id, name, teamid):
        self.id = id
        self.name = name
        self.teamid = teamid
        num = int(teamid[4:])
        self.teamName = b[num - 1][0]
        self.uniName = b[num - 1][1]

    def __str__(self):
        return f"C{self.id:03d} {self.name} {self.teamName} {self.uniName}"

def solve():
    global b
    n = int(input())
    for _ in range(n):
        teamName = input()
        uniName = input()
        b.append((teamName, uniName))
    m = int(input())
    a = []
    for _ in range(m):
        name = input()
        teamid = input()
        a.append(Candidate(_ + 1, name, teamid))
    a.sort(key=lambda x: (x.name))
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()