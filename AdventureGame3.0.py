import time
import random

CREATURE = ['John Dillinger', 'Billy the Kid', 'Jack the Ripper', 'D.B Cooper']
hasFirePotion = False

#
# Time sleep function
#


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


#
# Check for valid input
#
def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if response in option:
                return response
        print_pause("Please enter 1 or 2")


#
# Prints intro
#


def intro(creature):
    print_pause("You are waiting in an old cobblestone"
                " train station lit by a dim light.")
    print_pause("Wanted papers are posted"
                " for " + creature + " are posted"
                " on the bulletin board. ")
    print_pause("Nearby is a local village tavern.\n"
                " Far away is a hostel you may find solstice in.")
    print_pause("All you have is your knapsack.")

# Making first choice
#


def get_aboard(creature):
    response = valid_input("Enter 1 to head to the tavern\n"
                           "Enter 2 to travel to the hostel\n"
                           "Choice: ", ["1", "2"])
    if "1" in response:
        print("You enter the dark tavern.")
        saloon(creature)
    elif "2" in response:
        print("You head down to the hostel")
        hostel(creature)

# Losing case


def tavern(creature):
    print_pause("You sit down at the tavern.")
    print_pause("Suddenly you realize you realize you"
                "are sitting next to " + creature + ".")
    print_pause("You are not ready to take on the quickest hand in the west.")
    response = valid_input("Should you, (1) try and fight "
                           "or (2) find the quickest way "
                           "out of there?", ["1", "2"])
    if response == '1':
        print_pause("With a quick draw, you were no match."
                    " Better luck next time!")
        play_again()
    elif response == '2':
        print_pause("You run back to the train station. It doesn’t:"
                    "seem like you’ve been spotted.")
        train_stop(creature)


def hostel(creature):
    global hasFirePotion
    print_pause("You are served a hot meal and some ale.")
    print_pause("You suddenly have super strength from your meal.")
    print_pause("You are given the Strength of Fire.")
    hasFirePotion = True
    print_pause("You grab your things and head back to the train station.")
    train_stop(creature)


def saloon(creature):
    global hasFirePotion
    if hasFirePotion:
        tavern(creature)
    else:
        print_pause("You sit down at the tavern. "
                    "This is no place for cowards.")
        print_pause("By the slip of their hat"
                    "," + creature + " tries to attack you!")
        response = valid_input("Would you like to, (1) fight"
                               " or (2) run away?", ["1", "2"])
    if response == '1':
        print_pause(creature + " goes for their pistol.")
        print_pause("They are no match for your newly acquired Fire Strength!")
        print_pause("In the heat of the moment you swiftly annihilate them!")
        print_pause("Now you are the swiftest hand in the west.")
        play_again()
    elif response == '2':
        print_pause("You head back to the hostel.\n"
                    " The sign on the front door says ‘CLOSED’.")
        print_pause("You head back to the train station.")

#
# Asks if user wants to play again
#


def play_again():
    global CREATURE
    global hasFirePotion
    response = valid_input("Would like to play again? "
                           "Reply 'yes' or 'no'.\n",
                           ["yes", "no"])
    if "no" in response:
        print_pause("Goodbye!")
    elif "yes" in response:
        print_pause("Wonderful! Let's begin.")
        rand = random.Random()
        crint = rand.randint(0, len(CREATURE) - 1)
        hasFirePotion = False
        train_stop(CREATURE[crint])


def train_stop(creature):
    intro(creature)
    get_aboard(creature)


rand = random.Random()
crint = rand.randint(0, len(CREATURE) - 1)

train_stop(CREATURE[crint])
