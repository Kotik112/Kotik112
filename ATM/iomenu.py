from transactionhistory import TransactionHistory
from account import *


# from account import construct_accounts
# from account import Account

# Contains all print related functions for the ATM.
# -- Arman Iqbal

def print_main_menu():
    """Prints the main menu"""
    print("""
    ***** Main Menu *****
    1.  Create a new account.
    2.  Account administration
    3.  Exit
    """)

def print_login_menu():
    """Prints the menu after logging in"""
    print("""
    ***** You are now logged in. *****
    1.  Withdraw money.
    2.  Deposit money.
    3.  Show balance and transaction history.
    4.  Log out.
    """)

def read_file(filename1, filename2):
    """"Reads two files and converts it back into Account objects."""

#   Read and split all accounts
    accounts_file = open(filename1, "r")
    account_contents = accounts_file.readlines()
    account_list = []
    for line in account_contents:
        account_values = line.split("|", 3)

        account_no = int(account_values[0])
        account_password = int(account_values[1])
        account_balance = int(account_values[2])

        account = Account(account_no, account_password, account_balance, None)
        account_list.append(account)

#   Read and split all transactions
    transactions_file = open(filename2, "r")
    transaction_contents = transactions_file.readlines()
    for line in transaction_contents:
        transaction_values = line.split("|")

        account_no = int(transaction_values[0])
        amount = int(transaction_values[1])
        date = transaction_values[2]

#       Add the transaction to the appropriate account.
        for account in account_list:
            if account.account_number == account_no:
                account.transaction_list.transaction_list.append(amount)
                account.transaction_list.date_list.append(date)
                
    return account_list

def save_to_file(filename1, filename2, account_list: Account):
    """Saves all accounts to file"""
    
    # Save accounts
    f1 = open(filename1, "w")
    for account in account_list:
        f1.write(str(account.account_number) + "|" + str(account.password) + "|" + str(account.balance) + "|\n")
    f1.close()
    
    # Save transactions
    f2 = open(filename2, "w")
    for account in account_list:
        for t in range(account.transaction_list.transaction_count()):
            amount = account.transaction_list.transaction_list[t]
            date = account.transaction_list.date_list[t]
            f2.write(str(account.account_number) + "|" + str(amount) + "|" + str(date) + "|\n")
    f2.close()

def take_login_input() -> int:
    """Takes two user inputs and checks them."""
    user_account = int(input("Enter your account number (6 digit): "))
    if len(str(user_account)) != 6 or str(user_account).isdigit() == False:
        print("You did not enter a 6 digit account number.")
        raise ValueError
    user_pin = int(input("Enter the PIN code (4 digits) : "))
    if len(str(user_pin)) != 4 or str(user_pin).isdigit() == False:
        print("You did not enter a 4 digit PIN.")
        raise ValueError
    return user_account, user_pin
  

def main():
    pass


if __name__ == "__main__":
    pass