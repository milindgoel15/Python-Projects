# LOGIC:
# a leap year has to be divisible by 4 leaving remainder 0
# but if its divisible by 100, then it is not a leap year.
# However, if the same year is divisible by 400, then it's a leap year.

def checkLeapYear(year):
   if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
      print(f'\n{year} is a leap year!')
   else:
      print('\nNot a year year!')

def main():
   year = int(input('Which year you want to check? '))
   checkLeapYear(year)

if __name__ == '__main__':
   main()