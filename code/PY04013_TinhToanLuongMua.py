def calTime(start_time, end_time):
    dh = int(end_time[:2]) - int(start_time[:2])
    dm = int(end_time[3:]) - int(start_time[3:])
    if dm < 0:
        dm += 60
        dh -= 1
    return dh + dm / 60

class RainStation:
    def __init__(self, id, name, start_time, end_time, rain_amount):
        self.id = id
        self.name = name
        self.total_time = calTime(start_time, end_time)
        self.total_rain = rain_amount

    def update(self, start_time, end_time, rain_amount):
        self.total_time += calTime(start_time, end_time)
        self.total_rain += rain_amount

    def __str__(self):
        return f"T{self.id:02d} {self.name} {(self.total_rain / self.total_time):.2f}"
    
def find(a, name):
    for i in range(len(a)):
        if name == a[i].name:
            return i
    return -1

def solve():
    n = int(input())
    a = []
    for _ in range(n):
        name = input()
        start_time = input()
        end_time = input()
        rain_amount = int(input())
        pos = find(a, name)
        if pos != -1:
            a[pos].update(start_time, end_time, rain_amount)
        else:
            a.append(RainStation(len(a) + 1, name, start_time, end_time, rain_amount))
    for station in a:
        print(station)

t = 1
# t = int(input())
for _ in range(t):
    solve()