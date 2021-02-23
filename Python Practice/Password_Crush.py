#Password_Crush
password = str(input("Enter your password: ")) #forcing the input to be a string with str
password = password.lower()#Converting the string to lowercase for UMGC or any varation
if len(password) >16: #password maxium length is 16 characters
    print("Not valid, your password is over length requirments(16max).")
elif len(password) < 8:#minimum password length is 8 characters
    print ("Not valid, your password must be more than 8 characters.")
elif len(password) >=8 or len(password)  <=16:#verifys the user that they meet length requirements of their password
    print ('Valid, your password meets the length requirments.')

spec_char = '!@#$%^&*+/\'?:(){}[]`~-_.'#special characters allowed in the password
valid = password 

specials = 0
for itervar in valid:#for loop for password
    index = 0
    while index < len(spec_char):#checks special characters against each itervar in for loop
        if spec_char[index] == itervar:
            specials = specials + 1   #if this finds a special character adds +1 
        index = index +1

if specials > 0:#prints to let user know if they require a special character or not. 
    print ("Valid, There is a special character in your password!")
else:
    print ("Not valid, there is no special character in your password!")

specs = 0 #counter for # character
for letter in valid: #for loop for looping through password
    if letter == '#': # looks for `#`
        specs = specs + 1 #counts the `#`

if specs > 0: #if the `#` exists...
    print('Valid, your password contains a `#`')
else:
    print('Not valid, you need a `#` in your password')

pound = '#'
if pound == valid[0] or pound == valid[-1]:# checks if the # symbol is within the first character with [0] and last character with [-1]
    print("Not vaild, password cannot contain a `#` in the first of last position")

test = valid.find("umgc") #checks for umgc within the password

if test != -1:
    print('Not valid, please remove umgc from your password.')


