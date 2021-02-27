'''
The sixth assignment involves writing a Python program to read in the
temperatures, as user input, for ten consecutive days in Celsius and
store them into an array. The entire array should then be displayed.
Next each temperature in the array should be converted to Fahrenheit
and the entire array should be again be displayed. The formula for
converting Celsius to Fahrenheit is °F = (°C x1.8) + 32. Finally, the
number of cool, warm and hot days should be counted and the number of
each type of days should be displayed. You should decide on the thresholds
for determining whether a day is cool, warm or hot.
'''

temps = []
i = 0
while i < 10:
    u_input = float(input('Day {} temp: '.format(i+1)))
    y = i + 1
    print('Day', y, 'temp:',u_input, 'ENTERED.')
    temps.append(u_input)
    i+=1

print(temps)

for x in range(len(temps)):
    temps[x] = (temps[x] * 1.8) + 32


print(temps)
