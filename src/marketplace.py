from menu import Menu
from verification import Verification
from account import Account

class Main():
    def __init__(self):
        self.active_account = None

    def sign_up(self):
        print(" To create an account, we will need some information from you\n")

        while True:
            username = input(" Username: ")
            server = input(" Server: ")
            if verify.character_exists(username, server) is True:
                break
            else:
                print("\n Character does not exist, please try again\n")

        fname = input(" First Name: ")
        lname = input(" Last Name: ")
        email = input(" Email: ")

        while True:
            print("\n Please create a password. Must contain one of each of the following:")
            print(" Lowercase/uppercase letter, number and special character\n")
            password = input(" Password: ")
            if verify.validate_password(password) is False:
                print("\nPassword did not meet requirements, please try again\n")
                continue
            c_password = input(" Confirm Password: ")
            if verify.confirm_password(password, c_password) is False:
                print("Passwords do not match, please try again")
            else:
                break

        new_account = Account(username, server, email, fname, lname, password)
        new_account.update_accounts(True)

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
        name = input(" Item Name: ")
        price = input(" Sell Price: ")
        duration = input(" Duration (days): ")
        verify.add_item(self.active_account, name, price, duration)
        menu.display_menu(True)

    def log_out(self):
        self.active_account = ""
        menu.display_menu(False)
        print(" ***Logging you out...***")

    def quit(self):
        print(" ***Leaving application***")
        exit()

    def test(self):
        items = { "hammer", "tongs", "beer" }
        new_account = Account("Wilma", "Grotto", "test@test.com", "Wilma", "Flintstone", "howdyABC123!", 1000, items)
        print(new_account.username)
        print(new_account.server)
        print(new_account.email)
        print(new_account.firstname)
        print(new_account.lastname)
        print(new_account.password)
        new_account.currency = -50
        print(new_account.currency)
        new_items = { "hammer", "tongs", "beer", "pong" }
        new_account.items = new_items
        print(new_account.items)

main = Main()
menu = Menu(main)
verify = Verification()
menu.display_menu(False)