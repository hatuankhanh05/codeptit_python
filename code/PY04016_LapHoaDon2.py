import datetime

class Customer:
    def __init__(self, id, name, roomid, st, en, bonus):
        self.id = id
        self.name = name
        self.roomid = roomid
        date1 = datetime.datetime(int(st[6:]), int(st[3:5]), int(st[0:2]))
        date2 = datetime.datetime(int(en[6:]), int(en[3:5]), int(en[0:2]))
        self.totDays = int((date2 - date1).days) + 1
        bill = 0
        f = int(roomid[0])
        if f == 1:
            bill = self.totDays * 25
        elif f == 2:
            bill = self.totDays * 34
        elif f == 3:
            bill = self.totDays * 50
        else: bill = self.totDays * 80
        bill += bonus
        self.bill = bill

    def __str__(self):
        return f"KH{self.id:02d} {self.name} {self.roomid} {self.totDays} {self.bill}"

def solve():
    n = int(input())
    a = []
    for i in range(n):
        name = input().strip()
        roomid = input().strip()
        st = input().strip()
        en = input().strip()
        bonus = int(input())
        a.append(Customer(i + 1, name, roomid, st, en, bonus))
    a.sort(key=lambda x: -x.bill)
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()