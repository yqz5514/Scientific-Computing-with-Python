
fname = input('enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)


dic = dict()

for line in hand:
    if line.startswith('From '):
        list1 = line.split()
        if '@' in list1[1]:
            address = list1[1]
            dic[address] = dic.get(address, 0) + 1

list2 = list()
for k, v in dic.items():
    list2.append((v, k))

k, v = max(list2)
print(v,k)
