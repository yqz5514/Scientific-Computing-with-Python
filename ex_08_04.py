fname = input('enter the file name:')
fhand = open(fname)
wlist = list()
for line in fhand:
    line = line.rstrip().split()
    for word in line:
        if not word in wlist:
            wlist.append(word)
wlist.sort()
print(wlist)
