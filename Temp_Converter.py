#Program Title: Temp Converter
'''
PROGRAM REQUIRMENTS
The sixth assignment involves writing a Python program to read in the
temperatures, as user input, for ten consecutive days in Celsius and
store them into an array. The entire array should then be displayed.
Next each temperature in the array should be converted to Fahrenheit
and the entire array should be again be displayed. The formula for
converting Celsius to Fahrenheit is °F = (°C x1.8) + 32. Finally, the
number of cool, warm and hot days should be counted and the number of
each type of days should be displayed. You should decide on the thresholds
for determining whether a day is cool, warm or hot.

Cool - <55

Warm - 55 to 74, inclusive

Hot - >75
'''
print('Please enter the temperatures for the days below.')
temps = []
i = 0
while i < 10:
    u_input = float(input('Day {} temp: '.format(i+1)))
    y = i + 1
    #print('Day', y, 'temp:',u_input, 'ENTERED.')
    temps.append(u_input)
    i+=1

print(temps)

for x in range(len(temps)):
    temps[x] = (temps[x] * 1.8) + 32


print(temps)

h = 0#hot count
w = 0#warm count
c = 0#cold count
for x in temps:
    if x >= 75:
        h += 1
    elif (x < 75 and x > 55):
        w += 1
    elif x <= 55:
        c += 1

print(h, 'days were HOT')
print(w, 'days were WARM')
print(c, 'days were COLD')
