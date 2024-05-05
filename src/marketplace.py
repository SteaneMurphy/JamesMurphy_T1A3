from menu import Menu

class Main():

    def sign_up(self):
        print(" To create an account, we will need some information from you")
        input(" What is your username? ")
        input(" What server is you character on? ")
        input(" What is your first name? ")
        input(" What is your lastname? ")
        input(" What is your email? ")
        print(" Please create a password. Passwords must be at least 8 characters, contain at leaat one of the following: uppercase, lowercase, number and special character")
        input(" Password: ")
        input(" Please confirm your password: ")

    def log_in(self):
        print("log in")

    def display_currency(self):
        print("display currency")

    def display_inventory(self):
        print("display inventory")

    def open_marketplace(self):
        print("open marketplace")

    def sell_item(self):
        print("sell item")

    def log_out(self):
        print("log out")

    def quit(self):
        print("quit")

main_instance = Main()
new_menu = Menu(False, main_instance)
new_menu.display_menu()