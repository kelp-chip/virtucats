import time
from vfunctions import pause

def PartOne(player_info):
    user_name = player_info[1]
    print("          CHAPTER ONE")
    print("\n[elder cat:]")
    input(" Well I better show you to your room.")
    time.sleep(0.3)
    print(" ", end="")
    pause(1, 0.25, 0)
    input(" Is that all you brought with you?")
    ans = input("\n[a] Tell the truth.\n[b] Make it up.\n[c] Is this not enough?\n\n")

    if ans == "a":
        time.sleep(.3)
        print("\n[{}]".format(user_name))
        time.sleep(0.5)
        input(" Yep.")
        print("\n[elder cat:]")
        time.sleep(0.5)
        print(" Excellent,", end="")
        time.sleep(0.8)
        input(" then the stairs won't be any trouble.")
    elif ans == "b":
        time.sleep(0.5)
        print("Well there was more", end="")
        pause(1, 0.5, 0)
        input("but I actually lost one of my bags on the way here.")
        print("\n[elder cat:]")
        print("Hmmm", end="")
        pause(1, 0.5, 0)
        input("That doesn't sound good.")
        input("Any idea where you left it?")
        ans = input("\n\n[a] Not a clue.\n[b] Make something up.\n\n")

    elif ans == "c":
        time.sleep(.5)
        input("\nOh, uh...")
        input("is this not enough?")
        input("\n[You showed a lack of self confidence.]")
        input("[The elder cat noticed that.]")
        print("\n[elder cat:]")
        input("No no, your room is fully furnished and we have laundry in the basement...")
        input("And As Tobias always says:")
        input('\n"One who lives without stuff is one who truly knows what life is!"')
        pause(1, 0.5, 0)
        input("...or something like that.")
        input("...he says it a little better, so...onwards to your room")