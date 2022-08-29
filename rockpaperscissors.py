import random

def artSigns():
   rock = '''
      ______
   ---'   ___)
         (_____)
         (______)
         (_____)
   ---.__(___)
   '''

   paper = '''
      _______
   ---'   ____)____
            ______)
            _______)
            ______)
   ---.________)
   '''

   scissors = '''
      _     ,/'
   (_).  ,/'
      _  ::
   (_)'  `\.
            `\.
   '''

   return (rock, paper, scissors)

def computerChoice():
   possibleChoices = ['rock', 'paper', 'scissor']

   computerChoice = random.choice(possibleChoices)
   return computerChoice

def compArt(computer_choice):
   r, p, s = artSigns()

   compArt = ''
   if computer_choice == 'rock':
      compArt = r
   elif computer_choice == 'paper':
      compArt = p
   elif computer_choice == 'scissor':
      compArt = s
   return compArt

def userArt(user_choice):
   r, p, s = artSigns()

   userArt = ''
   if user_choice == 'rock':
      userArt = r
   elif user_choice == 'paper':
      userArt = p
   elif user_choice == 'scissor':
      userArt = s
   return userArt

def gameLogic(user_choice):
   computer_choice = computerChoice()
   # user_choice = userChoice()
   comp_art = compArt(computer_choice)
   user_art = userArt(user_choice)
  

   if user_choice == computer_choice:
      print(f'Computer chose: {computer_choice}\n {comp_art}\n User chose: {user_choice}\n {user_art}\n')
      print("Both players selected same action, it's a tie!")
   elif user_choice == 'rock':
      if computer_choice == 'scissor':
         print(f'Computer chose: {computer_choice}\n {comp_art}\n User chose: {user_choice}\n {user_art}\n')
         print("Rock smashes scissors! You win!")
      else:
         print(f'Computer chose: {computer_choice}\n {comp_art}\n User chose: {user_choice}\n {user_art}\n')
         print("Paper covers rock! You lose!")
   elif user_choice == 'paper':
      if computer_choice == 'rock':
         print(f'Computer chose: {computer_choice}\n {comp_art}\n User chose: {user_choice}\n {user_art}\n')
         print("Paper covers rock! You win!")
      else:
         print(f'Computer chose: {computer_choice}\n {comp_art}\n User chose: {user_choice}\n {user_art}\n')
         print("scissor cuts paper! You lose!")
   
   elif user_choice == 'scissor':
      if computer_choice == 'paper':
         print(f'Computer chose: {computer_choice}\n {comp_art}\n User chose: {user_choice}\n {user_art}\n')
         print("scissor cuts paper! You win!")
      else:
         print(f'Computer chose: {computer_choice}\n {comp_art}\n User chose: {user_choice}\n {user_art}\n')
         print("Rock smashes scissors! You lose!")
   

def main():
   userChoice = input("Please choose your input for the game: rock, paper or scissor: ").lower()
   gameLogic(userChoice)


if __name__ == "__main__":
   main()