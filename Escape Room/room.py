############################
######    Imports    #######
############################

from random import randint
from livingroom import LivingRoom

class Room:
    def __init__(self, name) -> None:
        self._name = name
        self._key_status = False   #False = player does not have key
        self._way_out = False

    def __repr__(self) -> str:
        #return f"Door: {self.door}\nWay out: {self.way_out}"
        pass
    
       

def main():
    pass

if __name__ == "__main__":
    main()