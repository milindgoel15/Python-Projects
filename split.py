import random

names = input("Give me some names: ")

nameList = names.split(", ")

x = len(nameList)
choice = random.randint(0, x - 1)

# or just use the choice function instead

message = nameList[choice] + ' is going to buy the meal today!'
print(message)