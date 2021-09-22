# Contains all elements regarding Account object
# -- Arman Iqbal

from transactionhistory import TransactionHistory
from random import randint

class Account:
    def __init__(self, account_number, password, balance, transaction_history: TransactionHistory):        
        self.account_number = account_number
        self.password = password
        self.balance = balance
        if transaction_history == None:
            self.transaction_list = TransactionHistory(None, None)
        else:
            self.transaction_list = transaction_history

    def __repr__(self):
        return f"Account: {self.account_number}, {self.password}, {self.balance}, \n{self.transaction_list}"

    def login(self, password) -> bool:
        """Returns True/False depending on wether or not the login was successful."""
        return self.password == password
      

def main():
    #Testing Account object
    test = Account(999999, 9999, 9999, TransactionHistory(None, None))
    print(test)

if __name__ == "__main__":
    main()    