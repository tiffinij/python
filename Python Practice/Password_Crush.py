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
password = str(input("Enter your password: ")) #forcing the input to be a string with str
password = password.lower()

#create functions for requirements



#length requirement
def check_length(input):
    if len(input) > 16:
        print("Not valid, your password is over length requirments(16max).")
    elif len(password) < 8:#minimum password length is 8 characters
        print ("Not valid, your password must be more than 8 characters.")
    elif len(password) >=8 or len(password)  <=16:#verifys the user that they meet length requirements of their password
        print ('Valid, your password meets the length requirments.')
    return None

#checks for `#` and counts them
def check_spec(input):
    spec = 0
    for itervar in input:
        if itervar == '#':
            spec = spec + 1
    return spec


check_length(password)
specs = check_spec(password)

#prints validation message for `#` special char
if specs > 0:
    print('Valid, your password contains a `#`')
else:
    print('Not valid, you need a `#` in your password')


pound = '#'
if pound == password[0] or pound == password[-1]:# checks if the # symbol is within the first character with [0] and last character with [-1]
    print("Not vaild, password cannot contain a `#` in the first or last position")
else:
    print("Vaild, password does not contain a `#` in the first or last position")    

test = password.find("umgc") #checks for umgc within the password

if test != -1:
    print('Not valid, please remove `umgc` from your password.')
else:
    print('Valid, your pswd does not contain `umgc`')

