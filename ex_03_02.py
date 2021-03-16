sh = input("enter hours: ")
sr = input("enter rate: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("error, please enter numeric input")
    quit()
    #fh = -1 my wrong step
    #fr = -1 my wrong step

print(fh, fr)#if fh > 0 and fh > 0  orgin wrong step
        #print(fh) (origin wrong step)
if fh > 40 :
    #print("over time")
              reg = fr * fh
              otp = (fh - 40) * (fr *0.5)
              xp = reg + otp
else:
    #print("regular")
              xp = fh * fr
print("pay:", xp)
#else:  (origin wrong step)
        #print("error, please enter numeric input")(origin wrong step)
