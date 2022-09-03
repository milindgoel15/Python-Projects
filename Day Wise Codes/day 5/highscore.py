studentScores = input("Enter the marks of students: ").split()

for i in range(0, len(studentScores)):
   studentScores[i] = int(studentScores[i])

highestMark = 0
for score in studentScores:
   if score > highestMark:
      highestMark = score

print(f"The highest score in the class is: {highestMark}")