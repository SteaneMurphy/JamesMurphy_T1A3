class Menu():

    def __init__(self, user_logged):
        self.user_logged = user_logged

    def display_menu(self):
        if self.user_logged is False:
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
            self.process_menu_selection(selection)
        else:
            print("\n ******************************************* WELCOME ***")
            print(" *                                                     *")
            print(" *     Welcome to the Arcane Emporium marketplace!     *")
            print(" *                                                     *")
            print(" *******************************************************\n")
            print(" \n --MENU-------------------------------------------------")
            print(" 1. Log In With Exising Account")
            print(" 2. Sign Up For A New Account")
            print(" 3. Quit Application\n")

    def process_menu_selection(self, selection):
        print(selection)