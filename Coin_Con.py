#Program Title: Coin Con
'''
PROGRAM REQUIRMENTS
Program Name: COIN CON
a Python program that accepts at least two values as input, performs some
computation and displays at least one value as the result. The computation
must involve calling one of the predefined functions in the math library.
Include comments in your program that describe what the program does.
'''

q = "go"
while q == "go":

    sel = input("Please enter a coin type - (p)enny, (n)ickel, (d)ime, or (q)uarter: ")
    day_max = eval(input("Please enter the number of days to count your coins: "))


    if(sel == "p"):
        coin = 0.01
    elif(sel == "n"):
        coin = 0.05
    elif(sel == "d"):
        coin = 0.10
    elif(sel == "q"):
        coin = 0.25


    i = 0
    d = 1
    while i < (day_max):
        x = pow(2, i)
        money = x * coin
        print("Day", d, "$",money)
        if (i == (day_max-1)):
            formatted_money = "{:.2f}".format(money)
            print ("After", d," days, you have $", formatted_money)
        i += 1
        d += 1

    formatted_money = "{:.2f}".format(money)


q = input("Type go to keep going ")
