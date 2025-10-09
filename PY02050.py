import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    st = [-1]
    for i in range(n):
        while st[-1] != -1 and a[st[-1]] <= a[i]:
            st.pop()
        print(i - st[-1], end = " ")
        st.append(i)
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()