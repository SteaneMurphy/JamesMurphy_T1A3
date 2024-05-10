from termcolor import colored
from menu import Menu
from verification import Verification
from account import Account
import time

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
                print(f"\n {colored('Character does not exist, please try again', 'red', attrs=['reverse', 'blink'])}\n")

        fname = input(" First Name: ")
        lname = input(" Last Name: ")
        email = input(" Email: ")

        while True:
            print("\n Please create a password. Must contain one of each of the following:")
            print(" Lowercase/uppercase letter, number and special character\n")
            password = input(" Password: ")
            if verify.validate_password(password) is False:
                print(f"\n {colored('Password did not meet requirements, please try again', 'red', attrs=['reverse', 'blink'])}\n")
                continue
            c_password = input(" Confirm Password: ")
            if verify.confirm_password(password, c_password) is False:
                print(f" {colored('Passwords do not match, please try again', 'red', attrs=['reverse', 'blink'])}")
            else:
                break

        new_account = Account(username, server, email, fname, lname, password)
        new_account.update_accounts(True)

        print(f" \n {colored('***Account Created - Returning to menu***', 'green', attrs=['reverse', 'blink'])}")
        time.sleep(2)
        menu.display_menu(False)

    def log_in(self):
        print("\n To log in, please provide your details\n")
        attempts = 3
        while True:
            login = input(" Username or email: ")
            password = input(" Password: ")
            valid, account = verify.verify_account(login, password)
            if valid:
                print(f"\n {colored('***Success! Logging you in***', 'green', attrs=['reverse', 'blink'])}\n")
                self.active_account = account
                time.sleep(2)
                break
            else:
                print(f"\n {colored('Account credentials do not match, try again', 'red', attrs=['reverse', 'blink'])}\n")
                print(f"\n {colored(f'ATTEMPTS REMAINING: {attempts -1}', 'yellow')}\n")
                if attempts <= 1:
                    print(f"\n {colored('To many failed attempts, returning you to the menu', 'red', attrs=['reverse', 'blink'])}\n")
                    time.sleep(2)
                    menu.display_menu(False)
                else:
                    attempts -= 1
     
        menu.display_menu(True)

    def display_currency(self):
        print(f'\n Your available balance is: ${self.active_account.currency}')
        input(f"\n {colored('Press any key to return to the menu', 'blue')} \n")
        menu.display_menu(True)

    def display_inventory(self):
        print("\n Your items: \n")
        for key, value in self.active_account.items.items():
            print(f" - {key} (Locked: {value})")
        input(f"\n {colored('Press any key to return to the menu', 'blue')} \n")
        menu.display_menu(True)

    def open_marketplace(self):
        selection = menu.display_marketplace(verify)
        item_name, item_price, seller_name = verify.get_item(selection)
        print(f"\n Confirm purchase: {item_name}, {item_price} glimmergold")
        confirm = input(" (Y / Yes) >>> ")
        if confirm.lower() == "y" or confirm.lower() == "yes":
            if self.active_account.currency - int(item_price) < 0:
                print(f"\n {colored('You do not have enough Glimmergold to purchase this item', 'red', attrs=['reverse', 'blink'])}")
                menu.select_another_item()
            else:
                self.active_account.currency = -item_price
                self.active_account.items[item_name] = False
                confim, seller_account = verify.verify_account(seller_name, skip_pass=True)
                seller_account.currency = item_price
                seller_account.items.pop(item_name)
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
                print(f"\n {colored('Invalid input, you must provide a number', 'red', attrs=['reverse', 'blink'])}\n")
            else:
                break

        if verify.add_item(self.active_account.username, self.active_account.items, name, price, duration):
            print(f"\n {colored('Success! Your item has been listed', 'green', attrs=['reverse', 'blink'])}")
            self.active_account.update_accounts()
            input(f"\n {colored('Press any key to return to the menu', 'blue')} \n")
        menu.display_menu(True)

    def log_out(self):
        self.active_account = None
        print(f"\n {colored('***Logging you out...***', 'yellow', attrs=['reverse', 'blink'])}\n")
        time.sleep(2)
        menu.display_menu(False)
        
    def quit(self):
        print(f"\n {colored('***Leaving application***', 'yellow', attrs=['reverse', 'blink'])}\n")
        time.sleep(2)
        exit()

main = Main()
menu = Menu(main)
verify = Verification()
menu.display_menu(False)