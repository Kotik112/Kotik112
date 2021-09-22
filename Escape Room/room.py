class Room:
    def __init__(self, name) -> None:
        self.name = name
        self.door = True
        self.way_out = False

    def __repr__(self) -> str:
        return f"Door: {self.door}\nWay out: {self.way_out}"

class LivingRoom(Room):
    def __init__(self, name, description) -> None:
        super().__init__(name)        #Inherits all variables and methods from Room
        #Inget syfte, testar subclass variabel
        self.description = description
        
class Bedroom(Room):
    def __init__(self, bed, bathroom, drawer, table, tv):
        self.bed = bed
        self.bathroom = bathroom
        self.drawer = drawer
        self.table = table
        self.tv = tv

    def __repr__(self) -> str:
        return f"Door: {self.door}\nWay out: {self.way_out}\nDescription: {self.description}"

def main():
    #Testing purposes
    living_room = LivingRoom("Living Room", "You find a bed and a locked closet.")
    print(living_room)

    #print(help(LivingRoom))

if __name__ == "__main__":
    main()
