import csv
from newPlayer import NewPlayer
from part_one import PartOne
from part_two import PartTwo
import time
from vfunctions import pause, delay_print

clear = "\n\n\n\n\n\n\n\n\n\n"
players_file = 'players.csv'
responses = ["Yeah, wrong answer...", "You gotta answer y or n", "Jess, Stop.",
            "*The elder cat appears to have bowed his head in prayer*", "Lord, please help me during this trying time...",
             "\n#/ᐠ- ꞈ -ᐟ\ \nListen, kid, I'm kinda busy. Maybe you should come back another time.\n\nSorry, Virtucats has quit your game.\nPlease try again later.",
             "IT\"S Y OR N!!!!"]

def main():

    outer_repeat = 1
    inner_repeat = 0
    response = 0

    # Loop for "Wanna play Virtucats? (y/n): "
    while outer_repeat == 1:
        play = str(input("Do you want to play Virtucats? (y/n): ")).lower()

        # (yes) response to Do you want to play Virtucats?
        if play == 'y':
            outer_repeat = 0
            response = 6

        # (no) response to Do you want to play Virtucats?
        elif play == 'n':
            print("\nOh....okay...then why did yo-")
            time.sleep(.5)
            pause(1,0.3,0)
            input("\nIt's fine, whatever...")
            exit()

        else:
            print(responses[response])
            if response == 5:
                exit()
            response += 1


    # Loop for "Is this a new game? (y/n): "
    while inner_repeat == 0:
        new = str(input("Is this a new game? (y/n): ")).lower()

        if new == "y":
            user_name = str(input("What is your holy feline name?: ")).capitalize()
            player_info = new_game(user_name, players_file)
            inner_repeat = 1

        elif new == "n":
            user_name = str(input("What is your holy feline name?: "))
            player_info, inner_repeat = load_game(user_name, players_file)

        else:
            print(responses[response])
            if response == 5:
                exit()
            elif response == 6:
                response += 1


    # Send player to checkpoint
    game_mapper = {0: PartOne, 1: PartTwo, 2: PartThree}
    tracker = int(player_info[2])
    track = game_mapper[tracker]
    track(player_info)



def new_game(user_name, players_file):
    check = str(input("{}...is that right? (y/n): ".format(user_name)))
    while check != 'y':
        user_name = str(input("What is your holy feline name?: ")).capitalize()
        check = str(input("{}...is that right? (y/n): ".format(user_name)))

    player = NewPlayer(user_name, players_file)
    player_data = [player.id, player.name, player.game_tracker, player.chapt_tracker]

    print("\n[ Game created ]\n")
    print("\n/ᐠ｡ ꞈ ｡ᐟ\ \nExcellent, {}, most excellent...".format(user_name))
    time.sleep(2)
    print("\nVital information indeed.")
    time.sleep(3)


    print("\n\n         welcome to")
    print("█░█ █ █▀█ ▀█▀ █░█ █▀▀ ▄▀█ ▀█▀ █▀")
    print("▀▄▀ █ █▀▄ ░█░ █▄█ █▄▄ █▀█ ░█░ ▄█   ")
    print("\n--------------------------------")
    time.sleep(1)


    check = "n"

    return player_data


def load_game(user_name, players_file):
    file = open(players_file, newline='')
    reader = csv.reader(file)
    header = next(reader)  # skips over first line since it is a header

    data = [row for row in reader]
    test = 0
    for line in data:
        if line[1].lower() == user_name.lower():
            player_data = line
            test = 1
            print("\nOh {}, welcome back!".format(user_name.capitalize()))
            time.sleep(1)
            print("\n█░█ █ █▀█ ▀█▀ █░█ █▀▀ ▄▀█ ▀█▀ █▀")
            print("▀▄▀ █ █▀▄ ░█░ █▄█ █▄▄ █▀█ ░█░ ▄█   ")
            print("\n--------------------------------")
            time.sleep(1)

    if test == 0:
        player_data = 0
        inner_repeat = 0
        print("Player not found.\n")
    else:
        inner_repeat = 1
    return [player_data, inner_repeat]


main()
