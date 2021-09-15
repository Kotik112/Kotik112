# Contains all elements regarding AccountLogin objects.
# -- Arman Iqbal

from random import randint

class AccountLogin:
    def __init__(self, account_number) -> None:
        self.account_number = account_number
        self.password = self.set_password()

    def set_password(self) -> int:
        """Creates a 4 digit PIN and displays it to user upon account creation"""
        password = randint(1000, 9999)
        if __name__ != "__main__":
            print(password)
        return password

    def login(self, account):
        if self.account_number == account:
            return self.password

def main():
    # DEBUG AND TESTING PURPOSES ONLY
    new = AccountLogin(1234)
    print(new.password)

if __name__ == "__main__":
    main()