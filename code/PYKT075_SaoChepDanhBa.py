'''
    author: htkhanh05
    created at: 04.12.2025 16:23:45
'''

import sys

class Contact:
    def __init__(self, name, phone, date):
        self.name = name
        self.phone = phone
        self.date = date

    def __str__(self):
        return f'{self.name}: {self.phone} {self.date}'
    
def get_sorting_key(contact):
    words = contact.name.split()
    return (words[-1], ' '.join(words[:-1]))

def solve():
    with open('SOTAY.txt', 'r') as f:
        content = f.readlines()
    # content = sys.stdin.readlines()

    i = 0
    date = None
    contacts = []
    while i < len(content):
        if content[i].startswith('Ngay'):
            date = content[i].strip().split()[1]
            i += 1
        else:
            contacts.append(Contact(content[i].strip(), content[i + 1].strip(), date))
            i += 2
    contacts.sort(key=get_sorting_key)
    
    # with open('DIENTHOAI.txt', 'w') as f:
    #     for contact in contacts:
    #         f.writeline(str(contact) + '\n')
    for contact in contacts:
        print(contact)
        

t = 1
#t = int(input())
for _ in range(t):
    solve()