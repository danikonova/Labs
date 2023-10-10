import re

a = {0: 'ноль ', 1: 'один'}
c = False
with open('1.txt', mode='r') as f:
       f = f.readline().split()
if not f:
    print('\nФайл в дириктории проекта законч ился')
    exit()
for k in f:
    g = re.findall(r'\b[01]\d*\b', k)
    if g:
        c = True
        for i in range(len(g)-1):
            if g(i) < g(i+1):
                  print(a[g(i)], end = ' ')
            else:
                print('')
        print()
