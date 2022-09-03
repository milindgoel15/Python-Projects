studentHeights = input("Enter the heights of students to calculate their average: ").split()
# print(studentHeights)
avg = 0
total = 0
for height in studentHeights:
   total += int(height)

num = 0
for student in studentHeights:
   num += 1

avg = round(total / num)
print(f"The average height of students is: {avg}")