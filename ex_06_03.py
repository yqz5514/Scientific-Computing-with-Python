
def cl(str, let):
    count = 0
    for letter in word:
        if letter == let :
           count = count + 1
           print(count)
        return count

word = input('Please enter a word:')
char = input('what letter are you looking for?')
count = 0

relcou = cl(word, char)
rl = float(relcou)

if rl > 0:
    print("Character appears", rl, "times")
else:
    print("Letter you are searching for does not appear in the string")
