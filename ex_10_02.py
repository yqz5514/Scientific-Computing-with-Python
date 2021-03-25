
fname = input('enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

dic = dict()

for line in hand:
    if line.startswith('From '):
        line = line.rstrip()
        list = line.split()
        time = list[5]
        time = time.split(':')
        hr = time[0]
        #hr = time[:2]


        #if '@' in list[1]:
            #time = list[5]
            #time = time.split(':')
            #hr = time[0]
        dic[hr] = dic.get(hr,0) + 1
#print(dic)
for k,v in sorted(dic.items()):
    print(k,v)
