s = input()
cntl, cntu = 0, 0
for c in s:
    if c.isupper():
        cntu += 1
    else:
        cntl += 1
if cntl >= cntu:
    print(s.lower())
else:
    print(s.upper())