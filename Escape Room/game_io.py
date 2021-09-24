############################
######    Imports   ########
############################

from player import Player

def print_house():
    print("""
                                   /\ 
                              /\  //\\\\
                       /\    //\\\\///\\\\\        /\ 
                      //\\\\  ///\////\\\\\\\\  /\  //\\\\ 
         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \ 
        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \ 
       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\ 
     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\ 
    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\ 
   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\ 
  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\ 
 / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |
/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

                **********      THE HOUSE      **********
    """)

def print_welcome(name):
    print(f"""
    Welcome {name}!
    """)

def print_bed_room():
    print("""
    You find yourself in the bedroom of a house. You find a bed, a drawer and a side table.
    What do you opt to search?
    A.  Bed
    B.  Drawer
    C.  Side table
    """)

def take_input() -> str:
    choice = input("Enter you choice (A, B or C): ")
    print(choice)
    if choice == "a" or choice == "b" or choice == "c":
        return choice
        #raise ValueError
    else:
        print("Invalid choice.")

def input_name():
    name = " "
    while name != "":
        name = input("Enter your name: ")
        #Error handling
        return str(name)

def print_intro(name):
    print(f"""
You wake up in an unfamiliar place, dizzy and confused. Unable to recognise your surroundings,
you try to exit the room through the door but find out that it is locked.
-{name}: 'The key has got to be here somewhere....'

Checking your surroundings more carefully this time you see there is a bed, a bedside table, and a closet.
-{name}: 'Let's see where this key is at...'

        What do you do?
        A. Search bed.
        B. Search bedside table.
        C. Search closet.
    """)
    
    
            

def main():
    input_name()  #Runs the atm without any exception handling.

if __name__ == "__main__":
    main()

