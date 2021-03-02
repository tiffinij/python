#Program Title: Leet_Translator
'''
PROGRAM REQUIRMENTS
Post a Python program that contains an array variable whose values are
input by the user. It should the perform some modification to each element
of array using a loop and then the modified array should be displayed.
Include comments in your program that describe what the program does.
'''
print('Please enter any words that contains an `a`.')
print('Press ENTER bewteen each word and enter `done` when')
print('you have entered all your words. ')

entries = []
#i = ''
entry = ''
while entry != 'done':
    entry = input('Please enter word: ')
    entries.append(entry)
    #i += 1

print(entries[:-1])

def find_a(input):
    while 'a' in input:
        char = '@'
        repl_a = input.find('a')
        input = input[:repl_a] + char + input[repl_a + 1:]
    return input

def find_s(input):
    while 's' in input:
        char = '5'
        repl_s = input.find('s')
        input = input[:repl_s] + char + input[repl_s + 1:]
    return input


c = 0
entries2 = []
while c < len(entries):
    for x in entries: #loops through entered strings
        y = entries.index(x) #store the position of the string to replace in the array
        while 'a' in x:
            x = find_a(x)
        entries[y] = x
        while 's' in x:
            x = find_s(x)
        entries[y] = x
    c += 1 #progresses the while loop through the array of strings entered by the user
print(entries[:-1])

'''#tested using find() to get positition of `a` in a string and replacing it
entry = 'apple'
char = '@'
print(entry)
repl_a = entry.find('a')

entry = entry[:repl_a] + char + entry[repl_a + 1:]
print(entry)
'''
