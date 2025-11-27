def solve():
    n = int(input())
    a = list(map(int, input().split()))
    st = [-1]
    leftGreater = [-1] * n
    rightNotGreater = [-1] * n
    for i in range(n):
        while len(st) > 1 and a[st[-1]] <= a[i]:
            st.pop()
        leftGreater[i] = st[-1]
        st.append(i)
    st.clear()
    st.append(-1)
    for i in range(n - 1, -1, -1):
        while len(st) > 1 and a[st[-1]] > a[i]:
            st.pop()
        rightNotGreater[i] = st[-1]
        st.append(i)
    ans = 0
    for i in range(n):
        if leftGreater[i] == -1 and rightNotGreater[i] == -1:
            ans += 1
    print(ans)

t = 1
t = int(input())
for _ in range(t):
    solve()