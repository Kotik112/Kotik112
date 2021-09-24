############################
######    Imports  #########
############################

from bedroom import Bedroom
from game_io import print_house, print_welcome, input_name, print_intro, take_input
from player import Player
from random import randint


############################
####   Game functions  #####
############################

def game():
    """Runs the escape room game"""
    while True:
        bedroom = construct_house()
        print_house()
        name = input_name()
        print_welcome(name)
        player = Player(name, "Living Room")
        print_intro(player._name)
        choice = take_input()
        search_key(bedroom, choice)  #Not working yet.
        break

def search_key(bedroom: Bedroom, choice):
    """"""
    if choice == "a":
            #Choice bed
        pass
    elif choice == "b":
        #Choice bedside table
        state = bedroom.search("bedside table")
        pass
    elif choice == "c":
            #Choice closet
        state = bedroom.search("closet")
        if state == True:
            print("Hurray! You found the key!")
        else:    
            print("Alas! No key!")


def construct_house():
    return Bedroom()

def randomise_key_location():
    number = randint(1,3)
    if number == 1:
        bedroom.bed = True


def main():
    game()

if __name__ == "__main__":
    main()
