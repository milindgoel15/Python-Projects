print('Welcome to the love calculator!')

name1 = input('What is your name? ')
name2 = input('What is their name? ')

combinedNames = name1 + name2
lowerCaseStr = combinedNames.lower()

t = lowerCaseStr.count('t')
r = lowerCaseStr.count('r')
u = lowerCaseStr.count('u')
e = lowerCaseStr.count('e')

true = t + r + u + e

l = lowerCaseStr.count('l')
o = lowerCaseStr.count('o')
v = lowerCaseStr.count('v')
e = lowerCaseStr.count('e')

love = l + o + v + e

loveScore = int(str(true) + str(love))

if loveScore < 10 or loveScore > 90:
   print(f'Your love score is {loveScore}, you go together like coke and mentos!')
elif loveScore > 40 and loveScore < 50:
   print(f'Your score is {loveScore}, you are alright together!')
else:
   print(f'Your score is {loveScore}')