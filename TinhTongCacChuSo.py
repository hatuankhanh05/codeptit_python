T = int(input())
for _ in range(T):
    S = input()
    num = 0
    arr = []
    for c in S:
        if str(c).isdigit():
            num += int(c)
        else:
            arr.append(c)
    arr.sort()
    for x in arr:
        print(x, end='')
    print(num)