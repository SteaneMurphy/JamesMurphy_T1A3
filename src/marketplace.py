from menu import Menu

class Main():

    def sign_up(self):
        print("sign up")

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