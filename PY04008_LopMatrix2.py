import sys

# -----------------------------------------------------
# Your clean Matrix class (this part is perfect)
# -----------------------------------------------------
class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a

    def __mul__(self, other):
        res = Matrix(self.n, other.m, [[0] * other.m for i in range(self.n)])
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    res.a[i][j] += self.a[i][k] * other.a[k][j]
        return res
    
    def printOut(self):
        a = self.a
        for i in range(self.n):
            for j in range(self.m):
                print(a[i][j], end = " ")
            print()

# -----------------------------------------------------
# Your friend's "Accepted" input logic
# -----------------------------------------------------

# Read T, handling empty input
try:
    T = int(input())
except (EOFError, ValueError):
    T = 0

# Read all subsequent lines into a single list 'e'
e = []
while True:
    try: 
        line = input().split()
        if line: # Only extend if the line wasn't blank
            e.extend(map(int, line))
    except (EOFError, ValueError): 
        break # Stop at end of file

I = 0 # This is the index for a 'cursor' in our list 'e'

# Loop T times
for t in range(T):
    try:
        # Read n and m from the list
        n, m = e[I], e[I+1]
        I += 2
        
        # --- The "Magic" Fix ---
        # Pad with zeros if 'e' doesn't have enough numbers
        while len(e) - I < n*m: 
            e.append(0)
            
        # Build matrix 'a' from the list 'e'
        a = []
        for i in range(n):
            row = e[I : I+m] # Get one row
            a.append(row)
            I += m # Move the cursor
        
        # --- Your 'solve' logic ---
        
        # Create the transpose 'b'
        b = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                b[i][j] = a[j][i]
                
        thisMat = Matrix(n, m, a)
        thatMat = Matrix(m, n, b)
        
        # Calculate and print
        (thisMat * thatMat).printOut()
        
    except (IndexError, ValueError):
        # Stop if 'e' runs out (e.g., T was wrong)
        break