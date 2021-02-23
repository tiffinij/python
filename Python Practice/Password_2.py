'''
The fifth assignment involves writing a Python program to determine
whether a password meets all the requirements for a secure password.
Your program should prompt the user for the candidate password and
output either that the password is valid or the reason it is invalid.
To be valid the length of the password must greater than some minimum
length but less than some maximum. It must not include the substring
"umgc" in any combination of upper or lower case letters. Finally,
it must contain the # symbol is some position other than the first or
last character. You should decide on the minimum and maximum allowable lengths.

'''

#create functions for requirements

#length requirement
def check_length(input):
    
