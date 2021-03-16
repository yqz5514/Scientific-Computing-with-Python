fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    #if line == ''
       #print('skip blank')
      # continue
    nl = line.split()
    #print('words:', nl)
    #guardian a bit stronger when set < 3
    #if len(nl) < 3:
      # continue
# guardians in compound statement
    if len(nl) < 3 or nl[0] != 'From':
        #print('ignore')
        continue
    print(nl[2])
