import string

fname = input('enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)


dic = dict()
for line in hand:
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.translate(line.maketrans('', '', '1234567890'))
    list0 = line.lower().split()
    for x in list0:#indicate different items in list
        for y in x:#indicate letters from x in list.
           dic[y] = dic.get(y,0)+1

lista = list()# if goona indicate list statement , can not use 'list' this word to
               #to dentify variables.

for k, v in dic.items():
    lista.append((v,k))#if change to (v,k),the will sort by value. 
    lista.sort(reverse=True)

for k,v in lista:
    print(k,v)
