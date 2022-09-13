from letters import alphabet
from art import logo

def caesar(text, shiftAmt, direction):
   output = ""
   if direction == 'decode':
      shiftAmt *= -1
   for letter in text:
      if letter in alphabet:
         old_pos = alphabet.index(letter)
         new_pos = old_pos + shiftAmt
         new_letter = alphabet[new_pos]
         output += new_letter
      else:
         output += letter
   print(f'The {direction}d text is {output}')

def main():
   continueApp = True
   print(logo)
   while continueApp:
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      shift = shift % 26
      caesar(text, shift, direction)

      restart = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
      if restart == 'no':
         continueApp = False
         print('goodbye!')

if __name__ == '__main__':
   main()