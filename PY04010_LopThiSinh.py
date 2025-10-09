class Candidate:
    def __init__(self, name, dob, sc1, sc2, sc3):
        self.name = name
        self.dob = dob
        self.sc1 = sc1
        self.sc2 = sc2
        self.sc3 = sc3
        self.tot = sc1 + sc2 + sc3
    
    def __str__(self):
        return f"{self.name} {self.dob} {self.tot:.1f}"

def solve():
    name = input()
    dob = input()
    sc1 = float(input())
    sc2 = float(input())
    sc3 = float(input())
    candidate = Candidate(name, dob, sc1, sc2, sc3)
    print(candidate)

t = 1
# t = int(input())
for _ in range(t):
    solve()