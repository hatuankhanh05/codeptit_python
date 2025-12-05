'''
    author: htkhanh05
    created at: 04.12.2025 17:55:45
'''

from datetime import datetime

class MonThi:
    def __init__(self, ma, ten, hinhthuc):
        self.ma = ma
        self.ten = ten
        self.hinhthuc = hinhthuc

class CaThi:
    def __init__(self, ma, ngay, gio, phong):
        self.ma = ma
        self.ngay = ngay
        self.gio = gio
        self.phong = phong

class LichThi:
    def __init__(self, cathi, monthi, nhom, sosv):
        self.cathi = cathi
        self.monthi = monthi
        self.nhom = nhom
        self.sosv = sosv
    
    def __str__(self):
        cathi = self.cathi
        monthi = self.monthi
        return f'{cathi.ngay} {cathi.gio} {cathi.phong} {monthi.ten} {self.nhom} {self.sosv}'
    
def sortingKey(lichthi):
    cathi = lichthi.cathi
    return (datetime.strptime(f'{cathi.ngay} {cathi.gio}', '%d/%m/%Y %H:%M'), cathi.ma)

def solve():
    monthiMap = {}
    with open('MONTHI.in', 'r') as f:
        n = int(f.readline().strip())
        for i in range(n):
            ma = f.readline().strip()
            ten = f.readline().strip()
            hinhthuc = f.readline().strip()
            monthiMap[ma] = MonThi(ma, ten, hinhthuc)

    cathiMap = {}
    with open('CATHI.in', 'r') as f:
        m = int(f.readline().strip())
        for i in range(m):
            ma = f'C{(i + 1):03d}'
            ngay = f.readline().strip()
            gio = f.readline().strip()
            phong = f.readline().strip()
            cathiMap[ma] = CaThi(ma, ngay, gio, phong)

    ds_lichthi = []
    with open('LICHTHI.in', 'r') as f:
        k = int(f.readline().strip())
        for i in range(k):
            maca, mamon, manhom, sosv = f.readline().strip().split()
            sosv = int(sosv)
            monthi = monthiMap[mamon]
            cathi = cathiMap[maca]
            ds_lichthi.append(LichThi(cathi, monthi, manhom, sosv))

    ds_lichthi.sort(key=sortingKey)
    for lichthi in ds_lichthi:
        print(lichthi)

t = 1
#t = int(input())
for _ in range(t):
    solve()