from menu import Menu
from verification import Verification

class Main():
    def __init__(self):
        self.active_account = ""

    def sign_up(self):
        print(" To create an account, we will need some information from you\n")
        username = input(" Username: ")
        server = input(" Server: ")
        print(verify.check_credentials(username, server))
        fname = input(" First Name: ")
        lname = input(" Last Name: ")
        email = input(" Email: ")
        print("\n Please create a password. Must contain one of each of the following:")
        print(" Lowercase/uppercase letter, number and special character\n")
        while True:
            password = input(" Password: ")
            if verify.validate_password(password) is False:
                print("\nPassword did not meet requirements, please try again\n")
                continue
            c_password = input(" Confirm Password: ")
            if verify.confirm_password(password, c_password) is False:
                print("Passwords do not match, please try again")
            else:
                break
        verify.add_account(username, server, fname, lname, email, password)
        print(" \n***Account Created - Returning to menu***")
        menu.display_menu(False)

    def log_in(self):
        print(" To log in, please provide your details\n")
        login = input(" Username or email: ")
        password = input(" Password: ")
        print(verify.verify_account(login, password))
        self.active_account = login
        menu.display_menu(True)

    def display_currency(self):
        print(f'\n Your available balance is: ${verify.check_balance(self.active_account)}\n')
        menu.display_menu(True)

    def display_inventory(self):
        print("\n Your items: \n")
        verify.display_items(self.active_account)
        menu.display_menu(True)

    def open_marketplace(self):
        print(" ---------------------------------------------ARCANE EMPORIUM - ITEMS FOR SALE---\n")
        verify.display_marketplace_items()
        print("\n ---ARCANE EMPORIUM - ITEMS FOR SALE---------------------------------------------")
        selection = int(input("\n Enter number to select item: "))
        verify.confirm_sale(selection, self.active_account)

    def sell_item(self):
        print(" To sell an item, we need some information\n")
        input(" Item Name: ")
        input(" Sell Price: ")
        input(" Duration (days): ")

    def log_out(self):
        print(" ***Logging you out...***")

    def quit(self):
        print(" ***Leaving application***")

main = Main()
menu = Menu(main)
verify = Verification()
menu.display_menu(False)