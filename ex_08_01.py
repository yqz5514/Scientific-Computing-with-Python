#Exercise 1: Write a function called chop that takes a list and modifies
 #it, removing the first and last elements, and returns None. Then write
  #a function called middle that takes a list and returns a new list that
  #contains all but the first and last elements.

letters = ['a', 'b', 'c']

#def chop(x):
#    del x[0]
#    del x[len(x)-1]
#print(chop(letters))
#print(list)

def middle(l):
    #e = len(l) - 1
    #e = float(e)
    #print(end)
    return l[1:len(l)-1]

print(middle(letters))
