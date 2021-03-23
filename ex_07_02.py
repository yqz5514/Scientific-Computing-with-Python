#Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:”
#pull apart the line to extract the floating-point number on the line.
#Count these lines and then compute the total of the spam confidence values from these lines.
#When you reach the end of the file, print out the average spam confidence.

fname = input('enter the file name:')
fop = open(fname)
count = 0
sum = 0
for l in fop:
    l = l.rstrip()
    if not l.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    pos = l.find('0')
    #print(pos)
    num = float(l[pos:])
    #print(num)
    sum = sum + num
    #print(sum)

print('Average:', sum/count)
