from random import random
import time

playing = False
inventoryP = []
inventoryB = ["Banana", "Fried Chicken", "Pencil", ]
inventoryD = ["HDMI cable", "Horn polishing solution", "Fried chicken receipt"]

def tw(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.025)

def theEnd():
    global playing
    playing = False
    tw("The game is over. Thanks for playing!")
    tw("Press enter to exit the game.")

def optionUno():
    global playing
    playing = False
    tw("You crouch behind the desks and oversized monitors\nMr. Marsh is busy writing something on the board\nYou creep toward the door\nTen feet\nFive feet\nTwo feet\nYour hand reaches for the handle\nSuddenly—\n“Going somewhere?”\nYou turn around\nMr. Marsh is staring at you")
    a1 = int(input("Do you want to: \n1. Run for it \n2. Claim you need to sharpen your pencil \n3. Use something from your inventory"))
    if a1 == 1:
        tw("You sprint toward the door\nMr. Marsh yells, “Stop right there!”\nYou make it to the door and open it\nYou are free!\nCongratulations, you have escaped the classroom! But you can still hear the horn honking in the distance\n")
    elif a1 == 2:
        tw("You claim you need to sharpen your pencil\nMr. Marsh looks at you suspiciously then looks down at your actual pencil\nYour alleged pencil is not even a pencil\nIt's a piece of fried chicken you were going to throw away\nMr.Marsh is intrigued by the piece of fried chicken and ask you a very important question\n")
        friedChicken = input("What is your favorite part of fried chicken? \n")
        tw("""Mr. Marsh goes on a tangent about how fried chicken in a way is so poetic because its like the mama chicken and the baby chicken are reunited right before consumption. "You see to bread a chicken you need to dip the mama chicken in her baby egg yolks and then..." \nIts offical, you are permantly tramatized but no longer bored\n""")
        theEnd()
    else:
        hand = random.choice(inventoryB)
        if hand == "Banana":
            tw("You reach into your backpack and pull out a banana\nYou throw the banana peel on the floor\nMr. Marsh slips on the banana peel and falls to the ground\nYou make a run for it and escape the classroom!\nCongratulations, you have escaped the classroom!\n")
        elif hand == "Pencil":
            tw("You reach into your backpack and pull out a pencil\nYou throw the pencil on the floor\nMr. Marsh trips over the pencil and falls to the ground\nYou make a run for it and escape the classroom!\nCongratulations, you have escaped the classroom!\n")
        elif hand == "Fried Chicken":

def optionDos():
    global playing
    playing = False
    tw("Hello")

def optionTres():
    global playing
    playing = False
    tw("Goodbye")

def optionCuatro():
    global playing
    playing = False
    tw("See you later")

tw("Welcome to the Choose Your Own Adventure game! \nYou are a student in Mr. Marsh's class, and you have 17 minutes left until the end of the school day. \nYour goal is to escape the classroom without getting caught by Mr. Marsh. \nGood luck!\nHit enter to start the game.\n")
input()
playing = True

if playing == True:
    tw("""The clock hits 3:00 \nYou stare at the classroom door \nFreedom is only twenty feet away and 17 minutes left\nUnfortunately, Mr. Marsh is standing directly in front of it\n"Before you leave,” he announces, “I have one very important thing to say.”\nThe entire class groans\nMr. Marsh smiles proudly\n"I am so good at this job."\nHe pauses dramatically\nThen he literally toots his own horn\nHONK!\nNobody knows where he got the tiny horn\nYou decide it is time to escape.\n""")
while playing == True:    
    try:
        sceneOne = int(input("Do you want to: \n1. Sneak toward the door \n2. Compliment his teaching \n3. Investigate his desk while he's distracted \n4. Attempt to take a nap while he yaps\n"))
        if sceneOne == 1:
            optionUno()
        elif sceneOne == 2:
            optionDos()
        elif sceneOne == 3:
            optionTres()
        elif sceneOne == 4:
            optionCuatro()
        else:
            print("Please choose one of the four options with 1, 2, 3, or 4.")
    except ValueError:
        print("Please enter a valid number.")