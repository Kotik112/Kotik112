# Contains all ATM functions
# -- Arman Iqbal

from account import Account
from transactionhistory import TransactionHistory
from datetime import datetime as dt
from iomenu import save_to_file, print_main_menu, print_login_menu, read_file, take_login_input


WELECOME_BONUS = 500

def atm():
    """Main function that controls everything else."""

    #Reads two files and constructs a list of Acccount objects
    account_list = read_file("accounts.txt", "transactions.txt")  
    exit = False
    while exit != True:
        print_main_menu()
        menu_selection = int(input("Enter your choice (No. 1-3): "))
        input_error_check(menu_selection, 4)
        if menu_selection == 1:
            #Account creation code 
            account_list.append(create_account_number(account_list))                  
        elif menu_selection == 2:
            #Login menu code
            attempt_login(account_list)
        elif menu_selection == 3:
            #Exit out of program.
            save_to_file("accounts.txt", "transactions.txt", account_list)
            raise SystemExit

def create_account_number(account_list):
    """Creates and returns an Account object if the account number doesn't already exist."""

    user_account, user_pin = take_login_input()
    duplicate_flag = False
    for account in account_list:
        if user_account == account.account_number:
            duplicate_flag = True
    if duplicate_flag == False:
        return Account(user_account, user_pin, WELECOME_BONUS, TransactionHistory(WELECOME_BONUS, format_date()))
    else:
        print("The account already exists.")

def attempt_login(account_list : Account):
    """Checks if user account doesn't already exist in account_list and compares the passwords"""

    login_state = False
    user_account, user_pin = take_login_input()
    #Go through all account numbers and 
    for account in account_list:
        if user_account == account.account_number:
            login_state = account.login(user_pin)
            if login_state == True:
                print(f"Login Successful! Login State: {login_state}")
                logged_in(account)  #Proceed to login menu and all functions therein.
            else:
                print(f"Login failed. Login State: {login_state}")

def logged_in(account : Account):
    """Account administration menu"""

    menu_selection = None
    while menu_selection != 4:
        print_login_menu()
        menu_selection = int(input("Enter your choice (No. 1-4): "))
        input_error_check(menu_selection, 5)
        if menu_selection == 1:
            #Withdraw money from the account
            print("\n***** WITHDRAW MENU *****")
            withdraw = int(input("How much would you like to withdraw?: "))
            transaction_input_check(withdraw)
            if withdraw > account.balance:
                print(f"You cannot withdraw more than {account.balance}.")    
            else:
                account.balance -= withdraw
                print(f"Blip blop: Here is your {withdraw} SEK.\nYour remaining balance is: {account.balance}")
                #Create record of the withdrawal
                account.transaction_list.transaction_list.append(-withdraw)
                account.transaction_list.date_list.append(format_date())

        elif menu_selection == 2:
            #Deposit money.
            print("\n***** DEPOSIT MENU *****")
            deposit = int(input("How much would you like to deposit?: "))
            transaction_input_check(deposit)
            account.balance += deposit
            print(f"Blip blop: You fed me {deposit} SEK. Tasty....\nYour new balance is: {account.balance}")
            #Create a record of the deposit
            account.transaction_list.transaction_list.append(deposit)
            account.transaction_list.date_list.append(format_date())

        elif menu_selection == 3:
            #Display current balance.            
            for i in range(len(account.transaction_list.transaction_list)):
                print(f"{i+1} -> Transaction amount: {account.transaction_list.transaction_list[i]} SEK, Time and date: {account.transaction_list.date_list[i]}.")
            print(f"\nBlip blop: Your current balance is: {account.balance} SEK")

        elif menu_selection == 4:
            #Log out
            print("You logged out!")
            break

def format_date():
    """"Formats today's date to the desired format"""
    string_format = "%H:%M %b %d-%Y"
    return dt.now().strftime(string_format)

def input_error_check(menu_selection, input_max_limit):
    """Checks the menu selection input for faulty input. "input_max_limit" is the upper limit on check, non-inclusive"""

    if menu_selection <= 0 or menu_selection >= input_max_limit:
        print(f"You must choose between 1 and {input_max_limit}.")
        raise ValueError 
    elif str(menu_selection).isdigit() == False:
        print("You must strictly input digits.")
        raise ValueError
    elif str(menu_selection).isalpha() == True:
        print("You cannot enter alphabets.")
        raise ValueError
        

def transaction_input_check(transaction_input):
    """Checks the deposit/withdrawal input for faulty input."""
    if str(transaction_input).isdigit() == False:
        print("You must strictly input digits.")
        raise ValueError
    elif str(transaction_input).isalpha() == True:
        print("You cannot enter alphabets.")
        raise ValueError

def main():
    atm()  #Runs the atm without any exception handling.

if __name__ == "__main__":
    main()


    #Hur kontrollerar jag så att rätt account skickas när användaren loggar in?