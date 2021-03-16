fname = input('enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

dic = dict()
for lin in hand :
    lin = lin.rstrip()
    #print(lin)
    wds = lin.spilt()
    #print(wds)
    for w in wds :
        #print('**',w,dic.get(w,-99))

        #if w in di :
            #dic[w] = dic[w] + 1
            #print('**existing**')
        #else :
            #dic[w] = 1
            #print('**New**'')
        #print(w, dic[w])


        # if the key is not there the count is zero
        #oldcount = dic.get(w,0)
        #print(w,'old',oldcount)
        #newcount = oldcount + 1
        #dic[w] = newcount

        dic[w] = dic.get(w,0) + 1 #this step = up 4 steps.
        #print(w,'new', newcount)
print(dic)

        # now we want to fidn the most common word
largest = -1
key = None
for k,v in dic.items() :
    #print(k,v)
    if v > largest :
        largest = v
        key = k
print('Done', key, largest)
