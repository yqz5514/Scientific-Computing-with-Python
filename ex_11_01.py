import re

x = input('enter regular expression: ')
fh = open('mbox.txt')

lista = list()
for y in fh:
    z = re.findall(x,y)
    if len(z)<1: continue
    lista += z

print('mbox.txt has', len(lista), 'lnes that matched', x)
