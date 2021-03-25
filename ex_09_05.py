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
            em = list[1]
            #
            name, dom = em.split('@')
            dict[dom] = dict.get(dom,0)+1

print(dict)
