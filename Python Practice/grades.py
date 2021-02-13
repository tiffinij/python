"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


"""


total = 0
def find_avg(aList):
    t = sum(aList)
    total = t/len(aList)
    return total




students = ["Johnathan J.","Joseph J.","Jotaro J.","Josuke H.","Giorno G."]
grades = []

for student in students:
        grade = int(input("Enter the quiz grade for " + student + ":"))
        grades.append(grade)
    
x = 0
while x < len(students):
    print(students[x], grades[x])
    x += 1

print("The highest quiz score is:", max(grades))


avg_grade = find_avg(grades)
print("The average quiz score is", avg_grade)


