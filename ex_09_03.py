fn = input('enter a file name:')
if len(fn) < 1:
    fn = 'mbox-short.txt'
try:
    fh = open(fn)
    print('File not found:', fn)
except:
    quit()


dict = dict()

for line in fh:

    if line.startswith('From '):
        list = line.split()
        if '@' in list[1]:
            ad = list[1]
            dict[ad] = dict.get(ad,0) + 1
print(dict)
