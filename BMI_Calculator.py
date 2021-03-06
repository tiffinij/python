'''
Write a Python program to determine the body-mass index of a collection
of six individuals. Your program should include a list of six names.
Using a for loop, it should successively prompt the user for the height
in inches and weight in pounds of each individual. Each prompt should
include the name of the individual whose height and weight is to be input.
It should call a function that accepts the height and weight as parameters
and returns the body mass index for that individual using the formula
weight x 703 / height2. That body mass index should then be appended to
an array. Using a second loop it should traverse the array of body mass
indices and call another function that accepts the body mass index as a
parameter and returns whether the individual is underweight, normal weight
or overweight. The number of individuals in each category should be counted
and the number in each of those categories should be displayed. You should
decide on the names of the six individuals and the thresholds used for
categorization.

< 18.5 is underweight
18.5 - 24.9 normal
>= 25.0 overweight
'''

names = ["Jonathan Joestar", "Joseph Joestar", "Jotaro Kujo", "Josuke Higashikata", "Giorno Giovanna", "Jolyne Kujo"]

#test array of names
'''
print("Testing array: ")
for name in names:
    print(name)
'''

heights = [] #empty array for heights
weights = [] #empty array for weights
bmis = []    #empty array for weights

for name in names:
    print("Please enter the information for", name)
    height = float(input("Height (inches): "))
    heights.append(height)
    weight = float(input("Weight (lbs): "))
    weights.append(weight)


# test arrays are storiing data
'''
print(heights)
print(weights)
'''

def bmi_calc(h, w):
    bmi = (w * 703)/(h ** 2)
    return bmi

# loop through both arrays to calcuate bmi and then append to new array
x = 0
while x < len(heights):
    entry = bmi_calc(heights[x], weights[x])
    bmis.append(entry)
    x += 1
              
#test if bmis print as expected
'''    
print(bmis)
'''

def bmi_check(input1):
    u = 0
    n = 0
    o = 0
    for y in input1:
        if y < 18.5:
            u += 1
        elif (y >= 18.5 and y < 25.0):
            n += 1
        elif y >= 25.0:
            o +=1
    return u, n, o

                 
#call required second function 
results = bmi_check(bmis)

print(results[0], "users are Underweight")
print(results[1], "users are Normal")
print(results[2], "users are Overweight") 





    
    
