fn = input('enter a file name:')
fh = open(fn)

dict = dict()

for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
    # why ('form ')
              # ^ here has a space then the code willnot shoue error :list index out of range
    # below comment code is wrong, if len excuate first then it will not execute 'from' condition
    #if len(line)>3 or line.startswith('From'):

       list = line.split()
    # use list becasue make it convince to retrive items out of list.
       if '@'in list[1]:
           dy = list[2]
           dict[dy] = dict.get(dy,0)+1
print(dict)
