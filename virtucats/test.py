import time
from vfunctions import pause
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

delay_print("Hello")








# print("[elder cat:]")
# input("Well I better show you to your room.")
# pause(1, 0.3, 0)
# input("Is that all you brought with you?")
# ans = input("\n[a] Truth\n[b] Make it up.\n[c] Is this not enough?\n\n")
#
# if ans == "a":
#     time.sleep(.5)
#     input("\nYep.")
#     print("\n[elder cat:]")
#     input("Excellent, then the stairs won't be any trouble.")
# elif ans == "b":
#     time.sleep(0.5)
#     print("Well there was more", end="")
#     pause(1, 0.5, 0)
#     input("but I actually lost one of my bags on the way here.")
#     print("\n[elder cat:]")
#     print("Hmmm", end="")
#     pause(1, 0.5, 0)
#     input("That doesn't sound good.")
#     input("Any idea where you left it?")
#     time.sleep(0.5)
#     ans = input("\n\n[a] Not a clue.\n[b] Make something up.\n\n")
#
# elif ans == "c":
#     time.sleep(.5)
#     input("\nOh, uh...")
#     input("is this not enough?")
#     input("\n[You showed a lack of self confidence.]")
#     input("[The elder cat noticed that.]")
#     print("\n[elder cat:]")
#     input("No no, your room is fully equipped.")
#     input("And As Tobias always says:")
#     input('\n"One who lives without is one who truly knows what life is!"')
#     pause(1, 0.6, 1)
#     input("\nHe, uh...says it better.")

















 # print("[elder cat:]")
 #    print("Well I'd better show you to your room.")
 #    time.sleep(2.5)
 #    print("...")
 #    time.sleep(1.5)
 #    print("Is that all you have with you?")
 #    time.sleep(1.3)
 #
 #    ans = input("\n[a] Truth\n[b] Make something up.\n[c] Is this not enough?\n\n")
 #
 #    if ans == "a":
 #        time.sleep(1.3)
 #        print("Yep.")
 #        time.sleep(1.3)
 #        print("\n[You chose to tell the truth.]\n")
 #        time.sleep(1.7)
 #        print("[elder cat:]")
 #        print("\nExcellent, then the stairs won't be any trouble.")
 #    elif ans == "b":
 #        time.sleep(1.3)
 #        print("Well there was more...but I actually lost one of my bags on the way here.")
 #        time.sleep(2)
 #        print("\n[You chose a detailed lie.]\n")
 #        time.sleep(1.7)
 #        print("[elder cat:]")
 #        print("Hmmm...that doesn't sound good...")
 #        time.sleep(1.3)
 #        print("Any idea where you left it?\n")
 #        ans = input("\n[a] Not a clue.\n[b] Make something up.\n")
 #        if ans == "a":
 #            time.sleep(1.3)
 #            print("No idea.")
 #            time.sleep(1.7)
 #            print("[elder cat:]")
 #            print("Hmmm....well you don't seem like you're missing it much...\n")
 #            time.sleep(1.7)
 #            print("Tobias once said that his bike was stolen once.")
 #            time.sleep(1)
 #            print("He said he realised that he never truly owned it to begin with.")
 #            time.sleep(1)
 #            print("You know what I mean?")
 #            ans = input("\n[a] wtf..?\n[b] Totally...\n")
 #            if ans == "a":
 #                time.sleep(1)
 #                print("Um...no, not really.")
 #                time.sleep(1.7)
 #                print("[elder cat:]")
 #                print("...\n")
 #                time.sleep(1)
 #                print("That's okay. You will, my child.")
 #            elif ans == "b":
 #                time.sleep(1)
 #                print("Yeah...I think I do actually.")
 #                time.sleep(1.7)
 #                print("[elder cat:]")
 #                print("I'm glad. I think you'll be very happy here.")
 #
 #        elif ans == "b":
 #            time.sleep(1.3)
 #            print("I think I left it on the bus I took to get out to Growlspath..")
 #            time.sleep(1.7)
 #            print("[elder cat:]")
 #            print("Shall I call the bus company and see if it was turned in?\n")
 #            time.sleep(1.7)
 #            ans = input("\n[a] I'll take care of it.\n[b] Go with it.\n")
 #            if ans == "a":
 #                time.sleep(1.3)
 #                print("No, don't worry about it. I'll give them a call tomorrow morning.")
 #                time.sleep(1.7)
 #                print("[elder cat:]")
 #                print("Oh, I thought you might have known already...")
 #                time.sleep(1.7)
 #                print("Cell phones are not permitted on the grounds.")
 #                time.sleep(1.7)
 #                print("Only communication is by radio or by our cordless in Tobias's office.")
 #
 #    elif ans == "c":
 #        time.sleep(1)
 #        print("Oh, uh...is this not enough?")
 #        time.sleep(1.7)
 #        print("\n[You showed a lack of self confidence.]\n")
 #        time.sleep(1.3)
 #        print("[The elder cat noticed that.]")
 #        time.sleep(1.7)
 #        print("\n[elder cat:]")
 #        print("No no, your room is fully equipped.")
 #        time.sleep(1.5)
 #        print("And As Tobias always says: less is more!")
 #
 #
