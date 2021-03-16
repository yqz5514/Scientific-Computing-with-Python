fname = input('enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

dic = dict()
for lin in hand :
    lin = lin.rstrip()
    #print(lin)
    wds = lin.spilt()
    #print(wds)
    for w in wds
        dic[w] = dic.get(w,0) + 1 #this step = up 4 steps.
#
#print(dic)

temp = list()
for k,v in dic.items() :
    #print(k.v)
    newt = (v,k)
    temp.append(newt)
#print('flipped', newt)

temp = sorted(tmp, revere=True)
#print('Sorted', temp[:5])

for v,k in tem[:5] :
    print(k,v)
