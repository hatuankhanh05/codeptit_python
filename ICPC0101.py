def solve():
    n = int(input())
    a = list(map(int, input().split()))
    st = []
    for i in range(n):
        st.append(a[i])
        if len(st) >= 2 and (st[-1] + st[-2]) % 2 == 0:
            st.pop()
            st.pop()
    print(len(st))

t = 1
# t = int(input())
for _ in range(t):
    solve()