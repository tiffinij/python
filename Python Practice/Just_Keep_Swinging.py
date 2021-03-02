#Program Title: JUST KEEP SWINGING!
'''
PORGRAM REQUIREMENTS
Post a Python program that contains a while loop. The number of times the
loop iterates should depend upon input supplied by the user. Your program
should display some output each time the loop executes. Include comments in
your program that describe what the program does.
'''
import random

playAgain = "y"
while playAgain == "y":

    print("You are in a dungeon.")
    input("Press ENTER to continue")
    print("You are running for your life after losing the other members of your party to an ambush.")
    print("The only thing you can see is the amber circles of light as you run by the torches on the wall.")
    input("Press ENTER to continue")
    print("You hit a dead-end and put your back to the wall,")
    print("prepared to stand your ground to your last breath.")
    input("Press ENTER to continue")
    print("Wall to wall, the horde takes up the width of the old stone corridor,")
    print("and you can't see an end to them.")
    print("You grit your teeth, firm your stance, and remember three words...")
    input("Press ENTER to continue")
    print("JUST. KEEP. SWINGING.")

    health = 74

    def swing_sword():
        #input("ENTER to Swing!")
        print("Swing!")
        swing = random.randint(6, 15)
        return swing

    numberOfEnemies = random.randint(60, 120)
    damage = random.randint(9, 13)

    while health > 0:
        swing = swing_sword()
        numberOfEnemies = numberOfEnemies - swing
        if (numberOfEnemies <= 0):
            print("Through some miracle, you survived!")
            break
        health = health - damage
        print(numberOfEnemies, "enemies remaining")


    if (numberOfEnemies > 0):
        print("You take your final swing, and the", numberOfEnemies, "enemies before you converge")
        print("on your lifeless body")

    playAgain = input("Pla[y] Again?: ")
