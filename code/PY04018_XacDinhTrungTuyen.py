subj = {
    "A": "TOAN",
    "B": "LY",
    "C": "HOA"
}

prio = {
    "1": 2,
    "2": 1.5,
    "3": 1,
    "4": 0
}

class Candidate:
    def __init__(self, id, name, examID, th, cm):
        self.id = id
        self.name = name
        self.subjj = subj[examID[0:1]]
        self.tot = th * 2 + cm + prio[examID[1:]]
        self.gra = ""
        if self.tot >= 18:
            self.gra = "TRUNG TUYEN"
        else:
            self.gra = "LOAI"

    def __str__(self):
        return f"GV{self.id:02d} {self.name} {self.subjj} {self.tot:.1f} {self.gra}"

def solve():
    n = int(input())
    a = []
    for i in range(n):
        name = input()
        examID = input()
        th = float(input())
        cm = float(input())
        a.append(Candidate(i + 1, name, examID, th, cm))
    a.sort(key=lambda x: -x.tot)
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()