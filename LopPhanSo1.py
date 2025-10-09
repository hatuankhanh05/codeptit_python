def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

class Fraction:
    def __init__(self, x, y):
        g = gcd(x, y)
        self.x = x // g
        self.y = y // g
    
    def toString(self):
        return str(self.x) + "/" + str(self.y)
    
x, y = map(int, input().split())
p = Fraction(x, y)
print(p.toString())