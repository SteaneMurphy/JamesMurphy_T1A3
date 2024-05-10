from termcolor import colored
import re
import json
from account import Account


class Verification:
#this class verifies and validates user information

    def character_exists(self, username, server):
    #checks that character and server exist on game server (character_server_list.json)
        with open("character_server_list.json", "r", encoding="utf-8") as file:
            accounts = json.load(file)
            for account in accounts:
                if account["username"].lower() == username.lower():
                    if account["server"].lower() == server.lower():
                        return True
            return False

    def validate_password(self, password):
    #checks against the regex pattern that the password entered meets the requirements:
    #1 uppercase, 1 lowercase, 1 number, 1 special character, min. 8 characters
        pattern = (
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$"
        )
        regex = re.compile(pattern)
        #load regex pattern
        p_match = re.search(regex, password)
        #compare password to pattern to find match
        if p_match:
            return True
        else:
            return False

    def confirm_password(self, password, c_password):
    #checks if the two password entered by the user match
        if password == c_password:
            return True
        else:
            return False

    def verify_account(self, login, password=None, skip_pass=False):
    #checks that the username/email and password exist and match an account profile
        with open("accounts.json", "r", encoding="utf-8") as file:
            accounts = json.load(file)
            for account in accounts:
                if (
                    account["username"].lower() == login.lower()
                    or account["email"].lower() == login.lower()
                ):
                    if account["password"] == password or skip_pass:
                        return True, Account(
                            account["username"],
                            account["server"],
                            account["email"],
                            account["firstname"],
                            account["lastname"],
                            account["password"],
                            account["currency"],
                            account["items"],
                        )
            return False, None

    def display_marketplace_items(self):
    #for each item in marketplace_items.json, display in the terminal
        with open("marketplace_items.json", "r", encoding="utf-8") as file:
            file_data = json.load(file)
            i = 1
            for account in file_data:
                print(f' | {i} >>> {account["name"]}')
                print(f' |      -  {account["price"]} glimmergold')
                print(f' |      -  {account["duration"]} days')
                i += 1
            return i

    def get_item(self, selection):
    #return the specific item details from marketplace
        with open("marketplace_items.json", "r", encoding="utf-8") as file:
            items = json.load(file)
            return (
                items[selection - 1]["name"],
                items[selection - 1]["price"],
                items[selection - 1]["username"],
            )

    def remove_item(self, selection):
    #remove the specific item from the marketplace
        with open("marketplace_items.json", "r", encoding="utf-8") as file:
            items = json.load(file)
            del items[selection - 1]

        with open("marketplace_items.json", "w", encoding="utf-8") as file:
            json.dump(items, file, indent=4)

    def add_item(self, username, account_items, item_name, price, duration):
    #add a specific item to the marketplace
        new_item = {
            "name": item_name,
            "price": price,
            "username": username,
            "duration": duration,
        }

        for item, value in account_items.items():
        #check if item is already listed
            print(item)
            if item == item_name:
                if account_items[item] != True:
                    account_items[item] = True
                    #mark item as listed

                    with open("marketplace_items.json", "r+", encoding="utf-8") as file:
                    #add item to marketplace_items.json
                        file_data = json.load(file)
                        file_data.append(new_item)
                        file.seek(0)
                        json.dump(file_data, file, indent=4)
                        return True
                else:
                    print(
                        f"\n {colored('Item is already listed on the marketplace', 'red', attrs=['reverse', 'blink'])}"
                    )
                    input(
                        f"\n {colored('Press any key to return to the menu', 'blue')} \n"
                    )
                    return False

        print(
            f"\n {colored('No such item exists in your inventory', 'red', attrs=['reverse', 'blink'])}"
        )
        input(f"\n {colored('Press any key to return to the menu', 'blue')} \n")
        return False
