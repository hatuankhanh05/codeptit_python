def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

class Fraction:
    def __init__(self, x, y):
        g = gcd(x, y)
        self.x = x // g
        self.y = y // g

    def add(self, other):
        return Fraction(self.x * other.y + self.y * other.x, self.y * other.y)
    
    def toString(self):
        return str(self.x) + "/" + str(self.y)
    
a = list(map(int, input().split()))
p = Fraction(a[0], a[1])
q = Fraction(a[2], a[3])
print(p.add(q).toString())