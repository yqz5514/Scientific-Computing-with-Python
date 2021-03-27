import re

fn = input('enter the file name: ')
if len(fn) == 0:
    fn = 'mbox.txt'

fh = open(fn)

lista = list()
listb = list()

for x in fh:
    y = re.findall('^New Revision: ([0-9.]+)', x)
# must use () to quote number, then number can be retrived at below float(num)
    if len(y) < 1: continue
    lista += y

for num in lista:
    listb.append(float(num))

print(sum(listb) / len(listb))
