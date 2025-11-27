def solve():
    exp = input().strip()
    st = []
    res = []
    cnt = 0
    for i in range(len(exp)):
        ch = exp[i]
        if ch == '(':
            cnt += 1
            st.append(cnt)
            res.append(cnt)
        elif ch == ')':
            res.append(st.pop())
    for x in res:
        print(x, end = " ")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()