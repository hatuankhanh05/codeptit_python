fee = {
    "Xe_con_5": 10000,
    "Xe_con_7": 15000,
    "Xe_tai_2": 20000,
    "Xe_khach_29": 50000,
    "Xe_khach_45": 70000
}

def solve():
    N = int(input())
    dates = []
    profit = {}
    for _ in range(N):
        arr = input().strip().split()
        plate = arr[0]
        type = arr[1]
        numberOfSeats = arr[2]
        status = arr[3]
        date = arr[4]
        mping = type + "_" + numberOfSeats
        if status == "OUT":
            continue
        if date not in dates:
            dates.append(date)
            profit[date] = 0
        profit[date] += fee[mping]
    for date in dates:
        print(date + ": " + str(profit[date]))

solve()