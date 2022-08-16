def main():
   print('Welcome to Python Pizza Deliveries!')

   size = input('\nWhat size of pizza do you want?\nSmall(S) - $15\nMedium(M) - $20\nLarge(L) - $25\nChoose S, M or L: ')
   pepperoni = input('\nDo you want pepperoni?\nCost prices:\n$2 for Small\n$3 for Medium and large\nChoose Y or N: ')
   extraCheese = input('\nDo you want to add extra cheese ($1) on top? Y or N: ')

   total = getBillAmt(size, pepperoni, extraCheese)

   print(f'\nYour final bill is {total}.')

def PizzaSizeAmt(size):
   if size == 'S':
      bill = 15
      return bill
   elif size == 'M':
      bill = 20
      return bill
   elif size == 'L':
      bill = 25
      return bill

def addCheese(extraCheese, size):
   bill = PizzaSizeAmt(size)
   if extraCheese == 'Y':
      bill += 1
      return bill
   else:
      return bill

def getBillAmt(size, pepperoni, extraCheese):
   bill = addCheese(extraCheese, size)
   if pepperoni == 'Y':
      if size == 'S':
         bill += 2
         return bill
      else:
         bill += 3
   else:
      return bill 

if __name__ == '__main__':
   main()