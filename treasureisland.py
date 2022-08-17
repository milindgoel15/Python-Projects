def main():
   print('''
   *******************************************************************************
            |                   |                  |                     |
   _________|________________.=""_;=.______________|_____________________|_______
   |                   |  ,-"_,=""     `"=.|                  |
   |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
   _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
   |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
   |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
   _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
   |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
   |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
   ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
   /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
   ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
   /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
   ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
   /______/______/______/______/______/______/______/______/______/______/_____ /
   *******************************************************************************
   ''')
   print("Welcome to Treasure Island.")
   print("Your mission is to find the treasure.")


   direction = input('In which direction you want to go? Choose Left(L) or Right(R): ').lower()

   findTreasure(direction)



def findTreasure(direction):
   if direction == 'left' or direction == 'l':
      swimOrNot = input('Whether you want to swim now or wait for boat? Choose Yes(Y) or No(N): ').lower()
      if swimOrNot == 'yes' or swimOrNot == 'y':
         print('Please wait for the boat!')
         print('You have now reached the castle.')
         door = input('Please choose the door to win your treasure? Choose Red(R) or Blue(B) or Yellow(Y): ').lower()
         if door == 'red' or door == 'r':
            print('You were burned by fire.\n=====  GAME OVER!  ======')
         elif door == 'blue' or door == 'b':
            print('You were eaten by beasts.\n=====  GAME OVER!  ======')
         elif door == 'yellow' or door == 'y':
            print('You won!.')
         else:
            print('You chose a door that doesn\'t exist and got lost.\n=====  GAME OVER!  ======')
      else:
         print('You were attacked by trout.\n=====  GAME OVER!  ======')
   else:
      print('You fall into a hole.\n=====  GAME OVER!  ======')

if __name__ == '__main__':
   main()