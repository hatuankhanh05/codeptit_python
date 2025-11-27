def calBill(old, new):
    amt = new - old
    ans = 0
    fine = 0
    if amt >= 101:
        ans = 50 * 100 + 50 * 150 + (amt - 100) * 200
        fine = 0.05
    elif amt >= 51:
        ans = 50 * 100 + (amt - 50) * 150
        fine = 0.03
    else:
        ans = amt * 100
        fine = 0.02
    ans += ans * fine
    tmp = ans - int(ans)
    ans = int(ans)
    if tmp < 0.5:
        return ans
    return ans + 1

class Customer:
    def __init__(self, id, name, old, new):
        self.id = id
        self.name = name
        self.tot = calBill(old, new)

    def __str__(self):
        return f"KH{self.id:02d} {self.name} {self.tot}"

def solve():
    n = int(input())
    a = []
    for i in range(n):
        name = input()
        old = int(input())
        new = int(input())
        a.append(Customer(i + 1, name, old, new))
    a.sort(key=lambda x: -x.tot)
    for x in a:
        print(x)
    
t = 1
# t = int(input())
for _ in range(t):
    solve()