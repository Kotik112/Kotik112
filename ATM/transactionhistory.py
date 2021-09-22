# Contains all elements regarding TransactionHistory object.
# -- Arman Iqbal

from datetime import date

class TransactionHistory:
    """Transaction"""
    def __init__(self, first_transaction, first_date):
        if first_transaction != None and first_date != None:
            self.transaction_list = [first_transaction]
            self.date_list = [first_date]
        else:
            self.transaction_list = []
            self.date_list = []

    def transaction_count(self):
        return len(self.transaction_list)
    
    def __repr__(self):
        return f'Transactions: {self.transaction_list} / {self.date_list}'

def main():
    #Testing TransactionHistory
    test = TransactionHistory(None, None)
    print(test)

if __name__ == "__main__":
    main()