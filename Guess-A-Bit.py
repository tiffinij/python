#Program Title: Guess-A-Bit 
'''
PROGRAM REQUIRMENTS
Post a Python program that accepts a string as input. It should analyze some
characteristic of that string and display the result of that analysis.
The program must use at least one of the following: string slices, string
conditions or string methods.
'''
import random #import to generate ranodm number in range

guess = input('Guess a letter in the alphabet a-z (lowercase): ') #User enters a guess
genr = random.randint(0, 25) #selects a number between 0 and 25, inclusive
case = 'abcdefghijklmnopqrstuvwxyz' #string of letters a-z
answer = case[genr] #taking random number assigned to genr and using it to pick a letter from case string.
                               #This becomes the answer the user will guess

while guess != case [genr]: #while not the answer, continue loop

    x = case.rfind(guess) #string method rfind() to find the index postion of the guess in the rstring

    if x < genr: # if index position of guess is less than the random number
        print ("The answer is a letter after ", guess)
    elif x > genr:#if index position of guess is greater than the random number
        print("The answer is a letter before ", guess)
    guess = input('Guess again: ') #keep looping guess again until the user finds the answer

print ('You WIN!')#when the user enters the correct letter, print win
