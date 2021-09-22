# Main ATM program that runs the ATM and all underlying functions
# -- Arman Iqbal

from atmfunctions import atm
import sys     #For error checking at line 11

def main():
    try:
        atm()
    except Exception:
        print(sys.exc_info()[2])
    except SystemExit as e:
        print(f"You chose to shut down the ATM. -> {e}")
    except OSError as e:
        print(f"Error reading files. -> {e}")

if __name__ == "__main__":
    main()