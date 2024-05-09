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
        attempts = 3
        while True:
            login = input(" Username or email: ")
            password = input(" Password: ")
            valid, account = verify.verify_account(login, password)
            if valid:
                print("\n Success! Logging you in!\n")
                self.active_account = account
                break
            else:
                print("\n Account credentials do not match, try again\n")
                print(f"\n ATTEMPTS REMAINING: {attempts -1}\n")
                if attempts <= 1:
                    print("\n To many failed attempts, returning you to the menu\n")
                    menu.display_menu(False)
                else:
                    attempts -= 1
     
        menu.display_menu(True)

    def display_currency(self):
        print(f'\n Your available balance is: ${self.active_account.currency}\n')
        menu.display_menu(True)

    def display_inventory(self):
        print("\n Your items: \n")
        for key, value in self.active_account.items[0].items():
            print(f" - {key} (Locked: {value})")
        menu.display_menu(True)

    def open_marketplace(self):
        selection = menu.display_marketplace(verify)
        item_name, item_price, seller_name = verify.get_item(selection)
        print(f"\n Confirm purchase: {item_name}, {item_price} glimmergold")
        confirm = input(" (Y / Yes) >>> ")
        if confirm.lower() == "y" or confirm.lower() == "yes":
            if self.active_account.currency - int(item_price) < 0:
                print("\n You do not have enough Glimmergold to purchase this item")
                menu.select_another_item()
            else:
                self.active_account.currency = -item_price
                self.active_account.items[0][item_name] = False
                confim, seller_account = verify.verify_account(seller_name, skip_pass=True)
                seller_account.currency = item_price
                seller_account.items[0].pop(item_name)
                self.active_account.update_accounts()
                seller_account.update_accounts()
                verify.remove_item(selection)
                print("\n Item purchased")
                menu.select_another_item()
        else:
            menu.select_another_item()

    def sell_item(self):
        print(" To sell an item, we need some information\n")
        name = input(" Item Name: ")

        while True:
            try:
                price = int(input(" Sell Price: "))
                duration = int(input(" Duration (days): "))
            except ValueError:
                print("\n Invalid input, you must provide a number")
            else:
                break

        verify.add_item(self.active_account.username, self.active_account.items, name, price, duration)
        print("\n Your item has been listed")
        self.active_account.update_accounts()
        menu.display_menu(True)

    def log_out(self):
        self.active_account = None
        menu.display_menu(False)
        print(" ***Logging you out...***")

    def quit(self):
        print(" ***Leaving application***")
        exit()

main = Main()
menu = Menu(main)
verify = Verification()
menu.display_menu(False)