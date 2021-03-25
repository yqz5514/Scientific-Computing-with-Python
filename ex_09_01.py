fh = open('words.txt')
dict = dict()
#pl = input('enter a word:')
for x in fh:
    line = x.rstrip()
    list = x.split()
    for y in list:
        dict[y] = 0
print(dict)

if 'are' in dict:
    print('ture')
