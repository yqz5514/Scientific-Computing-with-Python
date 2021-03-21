

num = 0
tot = 0.0
while True:
    val = input('enter a numner:')
    if val == 'done':
        break
    try:
       fval = float(val)
    except:
       print('invalid input')
       continue
    num = num + 1
    tot = tot + fval
#print('all done')
print(tot, num, tot/num)

# redo assignment 01, find out somethings needs to be remembeed.
#define charactor should be first deined before the while loop.
#always forget ':' while using if,while,statement.
# counting shoud be writ down before sum
