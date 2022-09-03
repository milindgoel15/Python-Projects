print('Welcome to the tip calculator!\n')

bill = eval(input('What is your total bill amount? $'))
tip = eval(input('What percentage tip you would like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

amount = (bill / people) * ((100 + tip) / 100)

print(f'\nEach person should pay: ${round(amount, 2)}')