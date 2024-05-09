import re
import json
from account import Account

class Verification():

    def character_exists(self, username, server):
        with open ("character_server_list.json", "r") as file:
            accounts = json.load(file)
            for account in accounts:
                if account["username"].lower() == username.lower():
                    if account["server"].lower() == server.lower():
                        return True
            return False

    def validate_password(self, password):
        pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$"
        regex = re.compile(pattern)
        p_match = re.search(regex, password)
        if p_match:
            return True
        else:
            return False
        
    def confirm_password(self, password, c_password):
        if password == c_password:
            return True
        else:
            return False

    def verify_account(self, login, password = None, skip_pass = False):
        with open ("accounts.json", "r") as file:
            accounts = json.load(file)
            for account in accounts:
                if account["username"].lower() == login.lower() or account["email"].lower() == login.lower():
                    if account["password"] == password or skip_pass:
                        return True, Account(account["username"], account["server"], account["email"], account["firstname"], 
                                             account["lastname"], account["password"], account["currency"], account["items"])
            return False, None

    def display_marketplace_items(self):
        with open ("marketplace_items.json", "r") as file:
            file_data = json.load(file)
            i = 1
            for account in file_data:
                print(f' | {i} >>> {account["name"]}')
                print(f' |      -  {account["price"]} glimmergold')
                print(f' |      -  {account["duration"]} days')
                i += 1
            return i
    
    def get_item(self, selection):
        with open ("marketplace_items.json", "r") as file:
            items = json.load(file)
            return items[selection - 1]["name"], items[selection - 1]["price"], items[selection - 1]["username"]

    def remove_item(self, selection):
        with open ("marketplace_items.json", "r") as file:
            items = json.load(file)
            del items[selection - 1]
        
        with open ("marketplace_items.json", "w") as file:
            json.dump(items, file, indent=4)

    def add_item(self, username, account_items, item_name, price, duration):
        new_item = {
            "name": item_name,
            "price": price,
            "username": username,
            "duration": duration
        }

        for item, value in account_items[0].items():
            if item == item_name:
                if account_items[0][item] != True:
                    account_items[0][item] = True

                    with open ("marketplace_items.json", "r+") as file:
                        file_data = json.load(file)
                        file_data.append(new_item)
                        file.seek(0)
                        json.dump(file_data, file, indent=4)
                else:
                    print("\n Item is already listed on the marketplace")
                    return
            else:
                print("\n No such item exists in your inventory")
                return

        