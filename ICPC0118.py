zodiacs = [
    (20, "Bao Binh"),
    (19, "Song Ngu"),
    (21, "Bach Duong"),
    (20, "Kim Nguu"),
    (21, "Song Tu"),
    (21, "Cu Giai"),
    (23, "Su Tu"),
    (23, "Xu Nu"),
    (23, "Thien Binh"),
    (23, "Thien Yet"),
    (23, "Nhan Ma"),
    (22, "Ma Ket")
]

def solve():
    d, m = map(int, input().split())
    res = ""
    if d < zodiacs[m - 1][0]:
        res = zodiacs[m - 2][1]
    else:
        res=  zodiacs[m - 1][1]
    print(res)

t = 1
t = int(input())
for _ in range(t):
    solve()