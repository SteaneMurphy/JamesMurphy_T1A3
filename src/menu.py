from termcolor import colored, cprint
from ascii_magic import AsciiArt

class Menu():

    def __init__(self, main_instance):
        self.main_instance = main_instance

    def display_menu(self, user_logged):
        if user_logged is False:
            header = """ 
               ___                                  ______                           _               
              /   |  ______________ _____  ___     / ____/___ ___  ____  ____  _____(_)_  ______ ___ 
             / /| | / ___/ ___/ __ `/ __ \/ _ \   / __/ / __ `__ \/ __ \/ __ \/ ___/ / / / / __ `__ \\
            / ___ |/ /  / /__/ /_/ / / / /  __/  / /___/ / / / / / /_/ / /_/ / /  / / /_/ / / / / / /
           /_/  |_/_/   \___/\__,_/_/ /_/\___/  /_____/_/ /_/ /_/ .___/\____/_/  /_/\__,_/_/ /_/ /_/ 
                                                               /_/                                   
        """
            print(colored(header, 'red'))
            my_art = AsciiArt.from_image('header.jpg')
            my_art.to_terminal(columns=110, char="@")
            print(f"\n ******************************************* {colored('WELCOME', 'yellow')} ***")
            print(" *                                                     *")
            print(f" *     {colored('Welcome to the Arcane Emporium marketplace!', 'red')}     *")
            print(" *                                                     *")
            print(" *******************************************************\n")
            print(f" \n --{colored('MENU', 'yellow')}-------------------------------------------------")
            print(f" {colored('1.', 'yellow')} Log In With Exising Account")
            print(f" {colored('2.', 'yellow')} Sign Up For A New Account")
            print(f" {colored('3.', 'yellow')} Quit Application\n")

            selection = input(f"\n {colored('>>>', 'red')} ")
            self.main_menu_selection(selection)
        else:
            print(f"\n ******************************************** {colored('LOGGED', 'yellow')} ***")
            print(" *                                                     *")
            print(f" *      {colored('Welcome Back! What would you like to do?', 'yellow')}       *")
            print(" *                                                     *")
            print(" *******************************************************\n")
            print(f" \n --{colored('MENU', 'yellow')}-------------------------------------------------")
            print(f" {colored('1.', 'yellow')} Display Currency")
            print(f" {colored('2.', 'yellow')} Display Inventory")
            print(f" {colored('3.', 'yellow')} Open Marketplace")
            print(f" {colored('4.', 'yellow')} Sell Item")
            print(f" {colored('5.', 'yellow')} Log Out")

            selection = input(f"\n {colored('>>>', 'red')} ")
            self.logged_menu_selection(selection)

    def main_menu_selection(self, selection):
        match selection:
            case "1":
                self.main_instance.log_in()
            case "2":
                self.main_instance.sign_up()
            case "3":
                self.main_instance.quit()
            case _:
                print(f"\n {colored('This is not a valid menu option, please select from the availble options', 'red', attrs=['reverse', 'blink'])}")
                input(f"\n {colored('Press any key to return to the menu', 'blue')} \n")
                self.display_menu(False)

    def logged_menu_selection(self, selection):
        match selection:
            case "1":
                self.main_instance.display_currency()
            case "2":
                self.main_instance.display_inventory()
            case "3":
                self.main_instance.open_marketplace()
            case "4":
                self.main_instance.sell_item()
            case "5":
                self.main_instance.log_out()
            case _:
                print(f"\n {colored('This is not a valid menu option, please select from the availble options', 'red', attrs=['reverse', 'blink'])}")
                input(f"\n {colored('Press any key to return to the menu', 'blue')} \n")
                self.display_menu(True)

    def display_marketplace(self, verify):
        print(f" ---------------------------------------------{colored('ARCANE EMPORIUM - ITEMS FOR SALE', 'red')}---\n")
        list_length = verify.display_marketplace_items()
        print(f"\n ---{colored('ARCANE EMPORIUM - ITEMS FOR SALE', 'red')}---------------------------------------------")
        while True:
            print("\n Enter number to select item")
            try:
                selection = int(input(f"\n {colored('>>>', 'red')} "))
            except ValueError:
                print(f"\n {colored('You must enter a number', 'red', attrs=['reverse', 'blink'])}")
            else:
                break
        if selection == 0 or selection > list_length - 1:
            print(f"\n {colored('There is no item listed in that slot', 'red', attrs=['reverse', 'blink'])}")
            self.select_another_item()
        else:
            return selection

    def select_another_item(self):
        print("\n Would you like to select another item?")
        confirm = input(f" {colored('(Y / Yes) >>>', 'red')} ")
        if confirm.lower() == "y" or confirm.lower() == "yes":
            self.main_instance.open_marketplace()
        else:
            self.display_menu(True)

    def sell_another_item(self):
        print("\n Would you like to sell another item?")
        confirm = input(f" {colored('(Y / Yes) >>>', 'red')} ")
        if confirm.lower() == "y" or confirm.lower() == "yes":
            self.main_instance.sell_item()
        else:
            self.display_menu(True)