from room import Room

class LivingRoom(Room):
    def __init__(self, name) -> None:
        super().__init__(name)        #Inherits all variables and methods from Room
        self.name = "Living Room"