import random
import time

playingsceneone = False
inventoryB = ["Banana", "Fried Chicken", "Pencil", ]
inventoryD = ["HDMI cable", "Giant Expo marker","Horn polishing solution", "Fried chicken receipt", "Backup Horn"]
chairFront = False
escaped = False
ss = False

def tw(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.050)

def FriedChickenE():
    global escaped
    endingCho = random.randint(0, 1)
    friedChicken = input("What is your favorite part of fried chicken? \n")
    if endingCho == 0:
        tw("""Mr. Marsh goes on a tangent about fried chicken\n"Fried Chicken is basically a system"\n"Chicken is the input... Breading is the processing... And the fried chicken is the output..."\n"Thats computer science kids, I'm so good at my job"\n"Isn't that just cooking?" a kid in the back whispers\nMr. Marsh picks up his horn and says "Cooking is computer science with seasoning!"\n"HONK!"\nIts offical, you are an expert in FriedChicken = The secrets of computer science\n""")
    else:
        tw("""Mr. Marsh goes on a tangent about fried chicken\n"In a way is so poetic because its like the mama chicken and the baby chicken are reunited right before consumption. "You see to bread a chicken you need to dip the mama chicken in her baby egg yolks and then..."\nIts offical, you are permantly tramatized but no longer bored\n""")
    tw("Inventory Gained: Fried Chicken Trama\n")
    escaped = False
    EndingEnd()

def DefensiveE():
    global escaped
    hand = random.choice(inventoryB)
    if hand == "Banana":
        tw("You reach into your backpack and pull out a banana\nYou throw the banana peel on the floor\nMr. Marsh slips on the banana peel and falls to the ground\nYou make a run for it and escape the classroom!\n")
        escaped = True
        EndingEnd()
    elif hand == "Pencil":
        tw("You reach into your backpack and pull out a pencil\nYou throw the pencil on the floor\nMr. Marsh trips over the pencil and falls to the ground\n")
        RunAwayE()
    elif hand == "Fried Chicken":
        tw("You reach into your backpack and pull out a fried chicken\nMr. Marsh is intrigued by the piece of fried chicken and ask you a very important question\n")
        FriedChickenE()

def RunAwayE():           
    tw("You sprint toward the door\nMr. Marsh yells, “Stop right there!”\nYou make it to the door and open it\nYou are free!\n")
    escaped = True
    EndingEnd()

def SleepyE():
    global escaped
    wakeup = random.randint(0, 2)
    if wakeup == 0:
        tw("In his hand is a giant textbook about computer science\nHe SLAMS it down on the desk\n You are suddenly spooked awake\n")
    elif wakeup == 1:
        tw("""He prepares himself for whats to come\n"DUDE YOUR MOMMY JUST CALLED"\n"You wake up slowly and Mr. Marsh looks disappointed"\nYou ask if you can go home then\nHe retorts with "If my mommy calls can I go home?"\nYou answer no and just look at each other\nHe got bored and goes back to teaching\n""")
    else:
        tw("By some miracle you wake up and he decided to instead leave you alone\n")
    escaped = False
    EndingEnd()

def InvestigateE():
    global chairFront
    global escaped
    tw("You approach his desk and crouching under all the massive computers\nAs you look through his drawers you find ")
    for x in inventoryD:
        tw(x + ", ")
    tw("You store all the items in your inventory sucessfully however...\nMr. Marsh suddenly turns around\nHe yells across the room \"What are you doing there?\"\n")
    inventoryB.append(inventoryD)
    storage = (input("Which item do you show him?" + str(inventoryB) + "\n"))
    if storage == "Bannana" or storage == "bannana":
        tw("You show him the banana\nHe looks at it confused\n\"Where did you get that?\"\n\"It's a banana, Mr. Marsh\"\n\"I don't care as long as it doesn't contain nuts, I don't want to accidently kill those two kids\"\n You look at him weird\n\"Just go back to your seat\"\n\n")
    elif storage == "Pencil" or storage == "pencil":
        tw("You show him the pencil\n\"I needed a pencil for your wonderful work?\"\n\"Doesn't mean you get to pass my yellow line that says no students\"\n\"Actually I don't get payed enough to care, just go back to your seat\"\n\n")
    elif storage == "HDMI cable" or storage == "hdmi cable":
        tw("You show him the HDMI cable\nHe looks at it with surprise\n\"Where did you get that?\"\n\"It's the HDMI cable, Mr. Marsh\"\n\"No you aren't allowed to have that back\"\nHe takes it from you and you suddenly find yourself in the chair of shame up in front\n\n")
        chairFront = True
    elif storage == "Giant Expo marker" or storage == "giant expo marker":
        tw("You show him the giant expo marker\nHe looks at it with surprise\nYou immediately know what to do\nYou go up to the board and draw a smiley face\n\"Hm good answer but give me the marker and go back to your desk\"\nHe takes it from you\n\n")
    elif storage == "Horn Polishing Solution" or storage == "horn polishing solution" or storage == "Horn polishing solution":
        tw("You show him the horn polishing solution\n\"Oh so I am assuming you are now volunteering to polish my horn right?\"\n\"Uh exactly! It was going to be a surprise!\"\n\"Oh cool bet\"\nHe gave you his horn from his pocket and for the next hour you spend time polishing it\n")
        SecretEnding()
    elif storage == "Backup Horn" or storage == "backup horn":
        tw("You show him the backup horn\nHe looks at it with surprise and then looks back at you with anger\n\"Why do you have the most precious thing in my life?\"\n\"Uh... I wanted to be you sir\"\n\"Absoultely not!\"\nHe takes it from you and you suddenly find yourself in the chair of shame up in front\n\n")
        chairFront = True
    else:
        tw("You show him ")
        print(storage)
        tw("He looks at you with so much excitement\n\"I have a very important question for you so answer carefully\"\n")
        FriedChickenE()

def SecretEnding():
    global playingsceneone
    tw("""Mr. Marsh's horn is now incredibly shiney\nHe looks at it with tears slowly developing\n"My horn..."\n"It's so beautiful!"\n"Class is cancelled for the rest of the day, we need to make this a national holiday"\n""")
    global ss
    ss = True

def EndingEnd():
    global playingsceneone
    global escaped
    global ss
    if ss:
        tw("You have discovered the secret ending! Congratulations! You will never see Mr. Marsh this happy again\n")
    elif escaped:
        tw("You have successfully escaped the classroom!\nCongratulations on your freedom!\n")
    else:
        tw("Class has finally ended congradulations!\nUnfortunately you still have to see Mr. Marsh again in two days\n")
    playingsceneone = False

tw("Welcome to the Choose Your Own Adventure game! \nYou are a student in Mr. Marsh's class, and you have 17 minutes left until the end of the school day. \nYour goal is to escape the classroom without getting caught by Mr. Marsh. \nGood luck!\nHit enter to start the game.\n")
input()
playingsceneone = True

while (playingsceneone):     
    if chairFront:
        tw("You are now sitting in the chair of shame\nEvery move you now do is watched with extra caution\nSo make your choices wisely.")
    else:
        tw("""The clock hits 3:00 \nYou stare at the classroom door \nFreedom is only twenty feet away and 17 minutes left\nUnfortunately, Mr. Marsh is standing directly in front of it\n"Before you leave,” he announces, “I have one very important thing to say.”\nThe entire class groans\nMr. Marsh smiles proudly\n"I am so good at this job."\nHe pauses dramatically\nThen he literally toots his own horn\nHONK!\nNobody knows where he got the tiny horn\nYou decide it is time to escape.\n\n""")
    try:
        sceneOne = int(input("Do you want to: \n1. Sneak toward the door \n2. Compliment his teaching \n3. Investigate his desk while he's distracted \n4. Attempt to take a nap while he yaps\n"))
        if sceneOne != 1 and sceneOne != 2 and sceneOne != 3 and sceneOne != 4:
            print("Please choose one of the four options with 1, 2, 3, or 4.")
    except ValueError:
        print("Please enter a valid number.")
    if sceneOne == 1:
        if chairFront:
            tw("You tried going behind a couple of desks but Mr. Marsh saw you\n\"Go back to your seat!\"")
        else:
            tw("You crouch behind the desks and oversized monitors\nMr. Marsh is busy writing something on the board\nYou creep toward the door\nTen feet\nFive feet\nTwo feet\nYour hand reaches for the handle\nSuddenly—\n“Going somewhere?”\nYou turn around\nMr. Marsh is staring at you\n")
            try:
                a1 = int(input("Do you want to: \n1. Run for it \n2. Claim you need to sharpen your pencil \n3. Use something from your inventory\n"))
                if a1 != 1 and a1 != 2 and a1 != 3:
                    print("Please choose one of the three options with 1, 2, or 3.")
            except ValueError:
                print("Please enter a valid number.")
        if a1 == 1:
            RunAwayE()
        elif a1 == 2:
            tw("You claim you need to sharpen your pencil\nMr. Marsh looks at you suspiciously then looks down at your actual pencil\nYour alleged pencil is not even a pencil\nIt's a piece of fried chicken you were going to throw away\nMr. Marsh is intrigued by the piece of fried chicken and ask you a very important question\n")
            FriedChickenE()
        else:
            DefensiveE()
    elif sceneOne == 2:
        tw("""You decide its easier if you manipulate his ego, afterall he literally just tooted his own horn\n"Mr. Marsh you teach us so well!"\nHe stops, his eyes widen, you can start to see tears forming in his eyes\n"You really mean it"\n"Yeah" you say as you realized you have made a grave mistake\n"Well let me tell you how I raised the most insane Computer Science student of all time... His name was Grant"\nYou decide this isn't worth it anymore and evaluate your options of escape\n""")
        try:
            a2 = int(input("Do you want to: \n1. Try to sleep with the tunes of his bragging\n2. Investigate his desk\n"))
            if a2 != 1 and a2 != 2:
                print("Please choose one of the two options with 1 or 2.")
        except ValueError:
            print("Please enter a valid number.")
        if a2 == 1:
            tw("As you start getting comfy Mr. Marsh notices and approaches\n")
            SleepyE()
        elif a2 == 2:
            if chairFront:
                tw("You tried going to his desks but Mr. Marsh saw you\n\"Go back to your seat!\"")
            else:
                InvestigateE()
    elif sceneOne == 3:
        if chairFront:
            tw("You tried going to his desks but Mr. Marsh saw you\n\"Go back to your seat!\"")
        else:
            tw("You decide that while you're bored you might as well look for the HDMI cable he took from your computer earlier\n")
            InvestigateE()
    elif sceneOne == 4:
        tw("You can't really do anything and you are so tired from everything you try to take a nap, you put your head down\nMr. Marsh however notices and approaches\n")
        SleepyE()
