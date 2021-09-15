# Contains all elements regarding Account object
# -- Arman Iqbal

from accountlogin import AccountLogin
from transactionhistory import TransactionHistory
#from atmfunctions import init_transaction_history

class Account:
    def __init__(self, balance, account_login : AccountLogin, transaction_history : TransactionHistory) -> None:
        self.balance = balance
        self.account_number = account_login.account_number
        self.password = account_login.password
        self.transaction_list = transaction_history.transaction_list
        self.date_list = transaction_history.date_list

def main():
    pass
    # history = init_transaction_history(500)
    # test = Account(500, 123456, history)
    # print(test)

if __name__ == "__main__":
    main()    