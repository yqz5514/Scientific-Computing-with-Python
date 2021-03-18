

c = input('Enter a Celsius degree:')

try:
    cnum = float(c)
except:
    print('Error, please enter a number.')
    quit()


f = cnum * 1.8 + 32
print('Fahrenheit:', f)
