scr = input('enter score: ')
try:
    fscr = float(scr)
except:
    print('bad score')
    quit()

if fscr > 1.0 :
    print('bad score')
elif 1.0 > fscr >= 0.9 :
    print('A')
elif 0.9 > fscr >= 0.8 :
    print('B')
elif 0.8 > fscr >= 0.7 :
    print('C')
elif 0.7 > fscr >= 0.6 :
    print('D')
else :
    print('F')
