############################
######    Imports   ########
############################

from random import randint

class Room:
    def __init__(self, name) -> None:
        self._name = name
        self._key_status = False   #False = player does not have key
        self._way_out = False

    def __repr__(self) -> str:
        #return f"Door: {self.door}\nWay out: {self.way_out}"
        pass



    

    
                

            
        
class Kitchen(Room):
    def __innit__(self):
        pass
    
class Entrance(Room):
    def __innit__(self):
        pass
       

def main():
    #Testing purposes
    living_room = LivingRoom("Living Room", "You find a bed and a locked closet.")
    print(living_room)

    #print(help(LivingRoom))

if __name__ == "__main__":
    main()