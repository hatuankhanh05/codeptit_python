class Rectangle:
    def __init__(self, l, w, c):
        self.l = l
        self.w = w
        self.c = c

    def peri(self):
        return 2 * (self.l + self.w)

    def area(self):
        return self.l * self.w
    
    def __str__(self):
        return f"{self.peri()} {self.area()} {self.c.capitalize()}"

def solve():
    l, w, c = input().strip().split()
    l = int(l)
    w = int(w)
    rec = Rectangle(l, w, c)
    print(rec)

if __name__ == '__main__':
    solve()