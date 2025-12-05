'''
    author: htkhanh05
    created at: 04.12.2025 17:36:39
'''
from datetime import datetime

class CaThi:
    def __init__(self, i, ngay, gio, phongthi):
        self.macathi = i
        self.ngay = ngay
        self.gio = gio
        self.phongthi = phongthi

    def __str__(self):
        return f'C{self.macathi:03d} {self.ngay} {self.gio} {self.phongthi}'
    
def sortingKey(cathi):
    return (datetime.strptime(cathi.ngay + ' ' + cathi.gio, '%d/%m/%Y %H:%M'), cathi.macathi)

def solve():
    with open('CATHI.in', 'r') as f:
        n = int(f.readline().strip())
        ds_cathi = []
        for i in range(n):
            ngay = f.readline().strip()
            gio = f.readline().strip()
            phongthi = f.readline()
            ds_cathi.append(CaThi(i + 1, ngay, gio, phongthi))
        ds_cathi.sort(key=sortingKey)
        for cathi in ds_cathi:
            print(cathi)

t = 1
#t = int(input())
for _ in range(t):
    solve()