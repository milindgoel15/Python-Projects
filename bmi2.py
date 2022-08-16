# this is bmi 2.0
def value(bmi):
   if bmi <= 18.5:
      print(f'\nUnderweight - {bmi}')
   elif bmi <= 25:
      print(f'\nnormal weight - {bmi}')
   elif bmi <= 30:
      print(f'\noverweight - {bmi}')
   elif bmi <= 35:
      print(f'\nObese - {bmi}')
   else:
      print(f'\nclinically obese - {bmi}')

def main():
   height = float(input('Enter your height in centimetres: '))
   weight = float(input('Enter your weight in kilograms: '))

   bmi = round(weight / ((height / 100) ** 2), 2)
   value(bmi)

if __name__ == "__main__":
   main()