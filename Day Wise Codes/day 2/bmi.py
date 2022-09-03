height = float(input("Enter your height in metres: "))
weight = int(input("Enter your weight in kg: "))

bmi = weight / (height ** 2)
result = round(bmi)
print(result)