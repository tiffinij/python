q = "go"
while q == "go":
  
  sel = input("Please enter a coin type - (p)enny, (n)ickel, (d)ime, or (q)uarter: ")
  day_max = eval(input("Please enter the number of days to count your coins: "))


  if(sel == "penny"):
    coin = 0.01
  elif(sel == "nickel"):
    coin = 0.05
  elif(sel == "dime"):
    coin = 0.10
  elif(sel == "quarter"):
    coin = 0.25


  i = 0
  d = 1
  while i < (day_max):
    x = pow(2, i)
    money = x * coin
    print("Day", d, "$",money)
    if (i == (day_max-1)):
        print ("After", d," days, you have $", money) 
    i += 1
    d += 1

  q = input("Type go to keep going ")
