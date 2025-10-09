import math

fee = {
    "Xe_con5": 10000,
    "Xe_con7": 15000,
    "Xe_tai2": 20000,
    "Xe_khach29": 50000,
    "Xe_khach45": 70000
}
days = {}

def solve():
    n = int(input())
    for _ in range(n):
        a = input().split()
        type = a[1] + a[2]
        goIn = (True if a[3] == "IN" else False)
        day = a[4]
        if goIn:
            days[day] = days.get(day, 0) + fee[type]
    for day in days:
        print(day + ": " + str(days[day]))

t = 1
# t = int(input())
for _ in range(t):
    solve()