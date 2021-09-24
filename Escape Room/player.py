class Player:
    def __init__(self, name, room) -> None:
        self._name = name
        self._room = room     #Vart spelaren befinner sig.
        self._has_key = False

    def update_location(self, room):
        """Updates Player room location. Returns True if successful, False if not."""
        if self.room != room:
            self.room = room
            return True
        else:
            print(f"You are already in {room}")
            return False

    def __repr__(self):
        return f"Name: {self._name}, Location: {self._room}, Key status: {self._has_key}"


def main():
    test = Player("Arman", "Bed Room")
    print(test)

if __name__ == "__main__":
    main()