# LUCKY SEVENS

import random

name = input('Hi, welcome to the game of Lucky Seven! What’syour name?')

print(" Welcome",name, "How much money would you like to put in?(Use whole integer i.e. 5 or 10)")

def sumDots():

    first = random.randint(1,6) #Produces arandom number for first dice

    second = random.randint(1,6) #Produces arandom number for second dice

    return first+second #Returns the totalroll

def getinput(): #Getting the input from the user

    while True:

        amount = input("Howmuch money would you like to put in?:") #Taking input

        try:

           amm = int(amount) #Converts it to a integer

           if(amm<=0):

               print("Invalid number, greater than zero please") #Letting userknow that they cannot use any negative number or 0

               continue

           return amm

        except valueError:#if not given an integer as input, repeat samething

           print ("Invalid number, greater than zero please")

           continue

initial = getinput() #Gets input

total = initial #The initial pot value to a total value

rolls = 0

maxi = initial;

print("Number of Rollstttt Win or Loss tttt CurrentValue of the Pot") #This is the model

while(total > 0):

    dices = sumDots() #roll the two dices

    rolls +=1 #Counts the number of rolls

    result = "" #Win or Loss

    if dices == 7: #Winning will add $4

        total = total + 4

        result = "Win"

    else: #If loss we will reduce $1

        total = total - 1

        result = "Loss"

    if(maxi < total):

        maxi = total;

print(rolls,"ttttt",result,"ttttt",total) #Printresults

print("The maximum amount in pot was $",maxi);
