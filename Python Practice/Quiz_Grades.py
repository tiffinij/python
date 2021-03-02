'''
Write a Python program to compute the average quiz grade for a group
of five students. Your program should include a list of five names.
Using a for loop, it should successively prompt the user for the quiz
grade for each of the five students. Each prompt should include the
name of the student whose quiz grade is to be input. It should compute
and display the average of those five grades and the highest grade. You
should decide on the names of the five students. Your program should
include the pseudocode used for your design in the comments.
'''


total = 0
def find_avg(aList): #created a function to determine the avg of a list of numbers
    t = sum(aList)
    total = t/len(aList)
    return total




students = ["Johnathan Joestar","Joseph Joestar","Jotaro Kujo","Josuke Higashikata","Giorno Giovanna"] #created list of 5 students
grades = []

for student in students: #loop through the list of students and prompt for a grade input
        grade = int(input("Enter the quiz grade for " + student + ":"))
        grades.append(grade)#add the entered grade to the list of grades

x = 0
while x < len(students):
    print(students[x], grades[x]) #print all students and grades
    x += 1

print("The highest quiz score is:", max(grades)) #print highest grade


avg_grade = find_avg(grades)
print("The average quiz score is", avg_grade) #print average grade
