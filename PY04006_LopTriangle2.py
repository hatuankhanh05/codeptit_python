import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        if a + b <= c or a + c <= b or b + c <= a:
            return "INVALID"
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return f"{s:.2f}"

t = 1
t = int(input())
arr = []
for _ in range(t):
    for x in input().split():
        arr.append(float(x))
i = 0
for _ in range(t):
    p1 = Point(arr[i], arr[i + 1])
    p2 = Point(arr[i + 2], arr[i + 3])
    p3 = Point(arr[i + 4], arr[i + 5])
    tri = Triangle(p1, p2, p3)
    print(tri.area())
    i += 6