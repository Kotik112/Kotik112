# Contains all ATM functions
# -- Arman Iqbal

from account import Account
from accountlogin import AccountLogin
from transactionhistory import TransactionHistory
from datetime import date
from printmenu import print_main_menu

def atm():
    try:
        test_trans = init_transaction_history(500)
        account_list = [Account((500), AccountLogin(1234), test_trans)]
        exit = False
        while exit != True:
            print_main_menu()
            menu_selection = int(input("Enter your choice (No. 1-3): "))
            if menu_selection < 1 or menu_selection > 3 or str(menu_selection).isdigit() == False:
                raise ValueError
            if menu_selection == 1:
                #Account creation code
                create_account_number()  
                
            elif menu_selection == 2:
                #Login menu code
                login_process(account_list)

            elif menu_selection == 3:
                #Exit out of program.
                raise SystemExit
    except: 
        print("You did something wrong!")   


def create_account_number(account_list : Account) -> AccountLogin:
    user_account = int(input("Enter your desired bank account (6 digits): "))
    if len(str(user_account)) != 6 or str(user_account).isdigit() == False:
        print("Error in create_account_number function") ## REMOVE LATER
        raise ValueError
    if user_account not in account_list.account_number:
        account_list.account_number = AccountLogin(user_account)
        print(f"Your password is {account_list.password}.") #DEBUG
        return account_list

def login_process(account_list):
    user_account = int(input("Enter your account number: "))
    if len(str(user_account)) != 6 or str(user_account).isdigit() == False:
        print("You did not enter a 6 digit account number.")
        raise ValueError
    else:
        if user_account in account_list:
            user_pin = int(input("Enter the PIN code (4 digits) : "))
            if len(str(user_pin)) != 4 or str(user_pin).isdigit() == False:
                print("Error at 35") ## REMOVE LATER
                raise ValueError
            else:
                pass
                #Check password

def init_transaction_history(welcome_bonus):
    """Creates a transaction history for new members"""
    if welcome_bonus != None:
        return TransactionHistory(welcome_bonus, date.today())

def main():
    atm()

if __name__ == "__main__":
    main()