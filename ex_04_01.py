def computepay(hours, rate):
    #print("in computepay", hours, rate)
    if hours > 40 :
         reg = rate * hours
         otp = (hours - 40) * (rate *0.5)
         pay = reg + otp
    else :
         pay = hours * rate
    #print("returning", pay)
    return pay

sh = input("enter hours: ")
sr = input("enter rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh, fr)

print("pay:", xp)
