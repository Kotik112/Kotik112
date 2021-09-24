from room import Room

class Bedroom(Room):
    def __init__(self):
        self._name = "Bedroom"
        self._bed = False
        self._closet = False
        self._side_table = False

    
    # def search(self, item): 
    #     """Return True if key is found. False if not"""
    #     if item == "closet":
    #         if self.closet == True:
    #             return True
    #         elif self.closet == True:
    #             return True
    #         elif self.table == True:
    #             return True
    #         else:
    #             return False