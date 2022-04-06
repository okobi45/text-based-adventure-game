import time
import random

# This is a simple text-based adventure game


def print_sleep(interval):
    # This this used to delay the printed message by 2secs
    print(interval)
    time.sleep(0.5)


list = ["dragon", "wicked fairie", "pirate", "troll", "gorgon"]
attacker = random.choice(list)
# This contains the list of all attackers in the game
# selected at random when the user restarts the game


items = []
# This is a blank item list


def intro():
    # This is the intro of the game
    print_sleep("You find yourself standing in an open field, filled with"
                " grass and yellow wildflowers.")
    print_sleep(f"Rumor has it that a {attacker} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def house(items):
    # This is the house
    if "sword" in items:
        print_sleep("You approach the door of the house.")
        print_sleep("You are about to knock")
        print_sleep(f"when the door opens and out steps a {attacker}.")
        print_sleep(f"Eep! This is the {attacker}'s house!")
        print_sleep(f"The {attacker} attacks you!")
    else:
        print_sleep("You approach the door of the house.")
        print_sleep("You are about to knock")
        print_sleep(f"when the door opens and out steps a {attacker}.")
        print_sleep(f"Eep! This is the {attacker}'s house!")
        print_sleep(f"The {attacker} attacks you!")
        print_sleep("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")


def fight(items):
    # This is code for every possible fight senario in the game
    if "sword" in items:
        print_sleep(f"As the {attacker} moves to attack, "
                    "you unsheath your new sword.")
        print_sleep("The sword of Ogoroth shines brightly in "
                    "your had as you brace "
                    "yourself for the attack.")
        print_sleep(f"But the {attacker} takes one look at your "
                    "shiny new toy and runs away!")
        print_sleep(f"You have rid the town of the {attacker}. "
                    "You are victorious!\n")
    else:
        print_sleep("You do your best...")
        print_sleep(f"but your dagger is no match for the {attacker}.")
        print_sleep("You have been defeated!\n")


def field():
    # This is an exit to the field
    print_sleep("You run back into the field. Luckily, "
                "you dont seem to have been followed.\n")


def cave(items):
    # This is the cave and its hidden gem. Play the game to find it
    if "sword" in items:
        print_sleep("You peer cautiously into the cave.")
        print_sleep("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now. "
                    "You walk back into the field\n")
    else:
        print_sleep("You peer cautiously into the cave.")
        print_sleep("It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock.")
        print_sleep("You have found the magical Sword of Ogoroth!")
        print_sleep("You discard your silly old dagger and "
                    "take the sword with you.")
        print_sleep("You walk back out to the field\n")
        items.append("sword")


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option


def play_again(items):
    # This is the option to play the game again or exit it
    play_code = valid_input("Would you like to play again? (y/n)", ['y', 'n'])
    if play_code == 'y':  # option 1
        print_sleep("Excellent! Restarting the game ...\n")
        play_game(items)
    else:  # option 2
        print_sleep("Thanks for playing! see you next time.\n")


def game_control(items):
    # This code controls most part of the action and senarios in the game
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")
    print_sleep("What would you like to do?")
    choice = valid_input("(Please enter 1 or 2.)\n", ['1', '2'])
    if choice == '1':
        house(items)
        choice2 = input("would you like to (1) fight or (2) run away?")
        if choice2 == '1':
            fight(items)
            play_again(items)
        elif choice2 == '2':
            field()
            game_control(items)
        else:
            play_again(items)
    else:
        cave(items)
        game_control(items)


def play_game(items):
    # This code can start or shut the game
    global attacker
    attacker = random.choice(list)
    intro()
    game_control(items)


play_game(items)
