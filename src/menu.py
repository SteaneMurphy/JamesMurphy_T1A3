from termcolor import colored, cprint
from ascii_magic import AsciiArt


class Menu:
#this class displays menus and deals with user menu selections

    def __init__(self, main_instance):
        #reference to instance of the Main class
        self.main_instance = main_instance

    def display_menu(self, user_logged):
        #one of two menus displayed depending on whether the user is logged in or not
        if user_logged is False:
        #main menu - user not logged in
            header = """ 
               ___                                  ______                           _               
              /   |  ______________ _____  ___     / ____/___ ___  ____  ____  _____(_)_  ______ ___ 
             / /| | / ___/ ___/ __ `/ __ \/ _ \   / __/ / __ `__ \/ __ \/ __ \/ ___/ / / / / __ `__ \\
            / ___ |/ /  / /__/ /_/ / / / /  __/  / /___/ / / / / / /_/ / /_/ / /  / / /_/ / / / / / /
           /_/  |_/_/   \___/\__,_/_/ /_/\___/  /_____/_/ /_/ /_/ .___/\____/_/  /_/\__,_/_/ /_/ /_/ 
                                                               /_/                                   
        """
            print(colored(header, "red"))
            my_art = AsciiArt.from_image("header.jpg")
            my_art.to_terminal(columns=110, char="@")
            print(
                f"\n ******************************************* {colored('WELCOME', 'cyan')} ***"
            )
            print(" *                                                     *")
            print(
                f" *     {colored('Welcome to the Arcane Emporium marketplace!', 'red')}     *"
            )
            print(" *                                                     *")
            print(" *******************************************************\n")
            print(
                f" \n --{colored('MENU', 'cyan')}-------------------------------------------------"
            )
            print(f" {colored('1.', 'cyan')} Log In With Exising Account")
            print(f" {colored('2.', 'cyan')} Sign Up For A New Account")
            print(f" {colored('3.', 'cyan')} Quit Application\n")

            selection = input(f"\n {colored('>>>', 'red')} ")
            self.main_menu_selection(selection)
        else:
        #logged menu - user logged in
            print(
                f"\n ******************************************** {colored('LOGGED', 'cyan')} ***"
            )
            print(" *                                                     *")
            print(
                f" *      {colored('Welcome Back! What would you like to do?', 'red')}       *"
            )
            print(" *                                                     *")
            print(" *******************************************************\n")
            print(
                f" \n --{colored('MENU', 'cyan')}-------------------------------------------------"
            )
            print(f" {colored('1.', 'cyan')} Display Currency")
            print(f" {colored('2.', 'cyan')} Display Inventory")
            print(f" {colored('3.', 'cyan')} Open Marketplace")
            print(f" {colored('4.', 'cyan')} Sell Item")
            print(f" {colored('5.', 'cyan')} Log Out")

            selection = input(f"\n {colored('>>>', 'red')} ")
            self.logged_menu_selection(selection)

    def main_menu_selection(self, selection):
    #user main menu selection
        match selection:
            case "1":
                self.main_instance.log_in()
            case "2":
                self.main_instance.sign_up()
            case "3":
                self.main_instance.quit()
            case _:
            #all invalid input handled by default case
                print(
                    f"\n {colored('This is not a valid menu option, please select from the availble options', 'red', attrs=['reverse', 'blink'])}"
                )
                input(f"\n {colored('Press any key to return to the menu', 'blue')} \n")
                self.display_menu(False)

    def logged_menu_selection(self, selection):
    #user logged menu selection
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
            #all invalid input handled by default case
                print(
                    f"\n {colored('This is not a valid menu option, please select from the availble options', 'red', attrs=['reverse', 'blink'])}"
                )
                input(f"\n {colored('Press any key to return to the menu', 'blue')} \n")
                self.display_menu(True)

    def display_marketplace(self, verify):
    #displays the marketplace menu
        print(
            f" ---------------------------------------------{colored('ARCANE EMPORIUM - ITEMS FOR SALE', 'red')}---\n"
        )
        list_length = verify.display_marketplace_items()
        print(
            f"\n ---{colored('ARCANE EMPORIUM - ITEMS FOR SALE', 'red')}---------------------------------------------"
        )
        while True:
        #while loop handle invalid input, try/except raises the error and checks for correct typing
            print("\n Enter number to select item")
            try:
                selection = int(input(f"\n {colored('>>>', 'red')} "))
            except ValueError:
                print(
                    f"\n {colored('You must enter a number', 'red', attrs=['reverse', 'blink'])}"
                )
            else:
                break
        if selection == 0 or selection > list_length - 1:
            #check length of marketplace list, if user selects above that value, return invalid
            print(
                f"\n {colored('There is no item listed in that slot', 'red', attrs=['reverse', 'blink'])}"
            )
            self.select_another_item()
        else:
            return selection

    def select_another_item(self):
    #prompt user to select another item in marketplace
        print("\n Would you like to select another item?")
        confirm = input(f" {colored('(Y / Yes) >>>', 'red')} ")
        if confirm.lower() == "y" or confirm.lower() == "yes":
            self.main_instance.open_marketplace()
        else:
            self.display_menu(True)

    def sell_another_item(self):
    #prompt user to sell another item
        print("\n Would you like to sell another item?")
        confirm = input(f" {colored('(Y / Yes) >>>', 'red')} ")
        if confirm.lower() == "y" or confirm.lower() == "yes":
            self.main_instance.sell_item()
        else:
            self.display_menu(True)
