nums = []

def Try(n, s):
    for j in range(0, 10, 2):  # even digits
        if len(s) < 1 and j == 0:  # no leading zero
            continue
        new_s = s + str(j)
        if len(new_s) == n:
            rs = new_s[::-1]
            # odd-length palindromes
            for i in range(0, 10, 2):
                if n * 2 + 1 > 6:  # optional restriction
                    break
                nums.append(int(new_s + str(i) + rs))
            # even-length palindrome
            nums.append(int(new_s + rs))
        else:
            Try(n, new_s)

# generate for n = 1..3
for i in range(1, 5):
    Try(i, "")
nums.sort()
t = int(input())
for _ in range(t):
    n = int(input())
    print(' '.join([str(x) for x in nums if x < n]))