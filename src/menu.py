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
            print(header)
            print("\n ******************************************* WELCOME ***")
            print(" *                                                     *")
            print(" *     Welcome to the Arcane Emporium marketplace!     *")
            print(" *                                                     *")
            print(" *******************************************************\n")
            print(" \n --MENU-------------------------------------------------")
            print(" 1. Log In With Exising Account")
            print(" 2. Sign Up For A New Account")
            print(" 3. Quit Application\n")

            selection = input(" >>> ")
            self.main_menu_selection(selection)
        else:
            print("\n ******************************************** LOGGED ***")
            print(" *                                                     *")
            print(" *      Welcome Back! What would you like to do?       *")
            print(" *                                                     *")
            print(" *******************************************************\n")
            print(" \n --MENU-------------------------------------------------")
            print(" 1. Display Currency")
            print(" 2. Display Inventory")
            print(" 3. Open Marketplace")
            print(" 4. Sell Item")
            print(" 5. Log Out")

            selection = input(" >>> ")
            self.logged_menu_selection(selection)

    def main_menu_selection(self, selection):
        match selection:
            case "1":
                self.main_instance.log_in()
            case "2":
                self.main_instance.sign_up()
            case "3":
                self.main_instance.quit()

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