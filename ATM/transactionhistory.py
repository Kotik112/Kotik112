# Contains all elements regarding TransactionHistory object.
# -- Arman Iqbal

class TransactionHistory:
    def __init__(self, transaction_list=[], date_list=[]) -> None:
        self.transaction_list = transaction_list
        self.date_list = date_list

    def print_tran_history(self):
        pass
        #result_sets = set(zip(self.transaction_list, self.date_list))
        #for values in result_sets:
        #    print(values)