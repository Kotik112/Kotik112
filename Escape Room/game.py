############################
######    Imports   ########
############################

from game_functions import game

def main():
    try:
        game() #Kör spelet
    except ValueError as e:
        print(f"Your input was invalid. -> {e}")

if __name__ == "__main__":
    main()
