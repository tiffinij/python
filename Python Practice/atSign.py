'''
Post a Python program that contains an array variable whose values are
input by the user. It should the perform some modification to each element
of array using a loop and then the modified array should be displayed.
Include comments in your program that describe what the program does.
'''

entries = []
i = 0
while i < 5:
    entry = input('Please enter any word that contains an `a`: ')
    entries.append(entry)
    i += 1
    
print(entries)


c = 0
while c < len(entries):
    for x in entries[c]:
        if x == 'a':
            x = '@'
    c += 1
print(entries)
