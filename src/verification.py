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

    def verify_account(self, login, password):
        with open ("accounts.json", "r") as file:
            accounts = json.load(file)
            for account in accounts:
                if account["username"].lower() == login.lower() or account["email"].lower() == login.lower():
                    if account["password"] == password:
                        return True, Account(account["username"], account["server"], account["email"], account["firstname"], 
                                             account["lastname"], account["password"], account["currency"], account["items"])
            return False, None

    def add_account(self, username, server, fname, lname, email, password):
        new_account = {
            "username": username,
            "server": server,
            "email": email,
            "firstname": fname,
            "lastname": lname,
            "password": password,
            "currency": 1000,
            "items": [] 
            }
        serialised = json.dumps(new_account, indent=4)
        with open ("accounts.json", "r+") as file:
            file_data = json.load(file)
            file_data.append(new_account)
            file.seek(0)
            json.dump(file_data, file, indent=4)

    def check_balance(self, username):
        with open ("accounts.json", "r") as file:
            file_data = json.load(file)
            for account in file_data:
                if account["username"] == username:
                    return account["currency"]
                
    def display_items(self, username):
        with open ("accounts.json", "r") as file:
            file_data = json.load(file)
            for account in file_data:
                if account["username"] == username:
                    for key, value in account["items"][0].items():
                        print(f' - {key} (Can Sell: {value})')

    def display_marketplace_items(self):
        with open ("marketplace_items.json", "r") as file:
            file_data = json.load(file)
            i = 1
            for account in file_data:
                print(f' | {i} >>> {account["name"]}')
                print(f' |      -  {account["price"]} glimmergold')
                print(f' |      -  {account["duration"]} days')
                i += 1

    def confirm_sale(self, selection, active_account):
        with open ("marketplace_items.json", "r") as file:
            file_data = json.load(file)
            choice = input(f' Type "Y" or "Yes" to confirm purchase of {file_data[selection - 1]["name"]} for {file_data[selection - 1]["price"]} glimmergold')
            if choice.lower() == "y" or choice.lower() == "yes":
                self.adjust_seller(file_data[selection - 1]["name"], file_data[selection - 1]["username"], file_data[selection - 1]["price"])
                self.adjust_buyer(active_account, file_data[selection - 1]["name"], file_data[selection - 1]["price"])
                del file_data[selection - 1]
        
        with open ("marketplace_items.json", "w") as file:
            json.dump(file_data, file, indent=4)

    def adjust_seller(self, item_name, seller_name, amount):
        with open ("accounts.json", "r") as file:
            file_data = json.load(file)
            for account in file_data:
                if account["username"] == seller_name:
                    account["currency"] += amount
                    account["items"][0].pop(item_name)
                
        with open ("accounts.json", "w") as file:
            json.dump(file_data, file, indent=4)

    def adjust_buyer(self, buyer_name, item_name, amount):
        with open ("accounts.json", "r") as file:
            file_data = json.load(file)
            for account in file_data:
                if account["username"] == buyer_name:
                    account["currency"] -= amount
                    account["items"][0][item_name] = False
            
        with open ("accounts.json", "w") as file:
            json.dump(file_data, file, indent=4)

    def add_item(self, username, item_name, price, duration):
        new_item = {
            "name": item_name,
            "price": price,
            "username": username,
            "duration": duration
        }

        with open ("accounts.json", "r") as accounts:
            file_data = json.load(accounts)
            for account in file_data:
                if account["username"] == username:
                    if account["items"][0][item_name] != True:
                        account["items"][0][item_name] = True
                    else:
                        print("Item is already on marketplace!")
                        return

        with open ("accounts.json", "w") as over:
            json.dump(file_data, over, indent=4)

        with open ("marketplace_items.json", "r+") as file:
            file_data = json.load(file)
            file_data.append(new_item)
            file.seek(0)
            json.dump(file_data, file, indent=4)