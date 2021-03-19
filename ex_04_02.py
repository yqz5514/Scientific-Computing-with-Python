
def computegrade(score) :
    if score < 0.0 or score > 1.0 :
       out = 'bad score'
    elif 1.0 > score >= 0.9 :
       out = 'A'
    elif 0.9 > score >= 0.8 :
       out = 'B'
    elif 0.8 > score >= 0.7 :
       out = 'C'
    elif 0.7 > score >= 0.6 :
       out = 'D'
    else :
       out = 'F'

    return out

scr = input('enter score: ')
try:
    fscr = float(scr)
except:
    print('bad score')
    quit()
    
gr = computegrade(fscr)
print('grade:', gr)
