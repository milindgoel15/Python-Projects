import random
from art import stages, logo
from words import word_list

def main():
   print(logo)
   print('######  Welcome to the game of Hangman!  ######\n\nTry to figure out the word or phrase by guessing the letters, without killing the man.\nNote: Each wrong letter cost a life. You have a total of 6 lives.')

   lives = 6
   chosen_word = random.choice(word_list)
   wordLength = len(chosen_word)
   counter = Counter(wordLength)
   display = []

   for i in range(wordLength):
      display.append("_")

   print(f'\nThe word is {counter} letters long.\n{display} ')
   GameLogic(wordLength, chosen_word, display, lives)


def Counter(wordLength):
   counter = 0
   for i in range(wordLength):
      counter += 1
   
   return counter


def GameLogic(wordLength, chosen_word, display, lives):
   while '_' in display:
      guess = input('\nPlease guess a letter: ').lower()
      
      for i in range(wordLength):
         letter = chosen_word[i]
         
         if letter == guess:
            display[i] = letter
            print(f'You guessed letter "{guess}" correctly.')
      print(display)

      if guess not in chosen_word:
         print('You guessed a letter that is not in the given word. You lose 1 life.')
         lives -= 1

      print(stages[lives])
      print(f'You have {lives} lives left.')
      
      if lives == 0:
         print('\nYou have killed the man. Game over!')
         exit()

      if '_' not in display:
         print('\nYou have won!')
         exit()


if __name__ == '__main__':
   main()