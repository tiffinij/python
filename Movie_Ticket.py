#Program Title: Movie Ticket
'''
PROGRAM REQUIRMENTS
Write a Python program that computes the price of a movie ticket depending on
if the person is seeing a 2D or 3D movie and if they are a child, and adult, or
a senior citizen.
'''
age = eval(input("Please enter your age: "))

if(age < 13):
    ticket = "c"
elif(12 < age < 60):
    ticket = "a"
else:
    ticket = "s"


screen = input("Please enter 2D or 3D: ")

#10.69 13.69 12.69
#14.69 17.69 15.69

if (ticket == "c" and screen == "2D"):
    price = 10.69
elif(ticket == "a" and screen == "2D"):
    price = 13.69
elif(ticket == "s" and screen == "2D"):
    price = 12.69
elif(ticket == "c" and screen == "3D"):
    price = 14.69
elif(ticket == "a" and screen == "3D"):
    price = 17.69
elif(ticket == "s" and screen == "3D"):
    price = 15.69


print("Your ticket will cost", price, " for viewing a ", screen, " movie")
