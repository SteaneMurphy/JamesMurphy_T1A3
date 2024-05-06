from menu import Menu
from verification import Verification

class Main():

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
        password = input(" Password: ")
        verify.validate_password(password)
        c_password = input(" Confirm Password: ")
        verify.confirm_password(password, c_password)
        verify.add_account(username, server, fname, lname, email, password)
        print(" \n***Account Created - Returning to menu***")
        menu.display_menu(False)

    def log_in(self):
        print(" To log in, please provide your details\n")
        login = input(" Username or email: ")
        password = input(" Password: ")
        print(verify.verify_account(login, password))
        menu.display_menu(True)

    def display_currency(self):
        print(" Your available currency: ")

    def display_inventory(self):
        print(" Items in your inventory: ")

    def open_marketplace(self):
        print("open marketplace")

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