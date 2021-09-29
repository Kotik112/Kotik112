############################
######    Imports   ########
############################

from cell import Cell

class Grid:
    def __init__(self, height, length) -> None:
        self.height = height
        self.length = length

    def gridify(self):
        grid = []
        for i in range(1, self.height+1):
            for j in range(1, self.length+1):
                grid.append(Cell(i * j))
        return grid



        
        
def main():
    battlefield = Grid(10, 10).gridify()
    print(battlefield)
    

if __name__ == "__main__":
    main()
