import re
import json

class Verification():

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
        
    def validate_email(self, email):
        pattern = """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21
                        \\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+
                        [a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\\.){3}(?:(2(5[0-5]|
                        [0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x 0c\\x0e-\\x1f\\x21-\\x5a\\x53-
                        \\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"""
        regex = re.compile(pattern)
        p_match = re.search(regex, email)
        if p_match:
            return True
        else:
            return False
        
    def check_credentials(self, username, server):
        with open ("accounts.json", "r") as file:
            accounts = json.load(file)
            for account in accounts:
                if account["username"].lower() == username.lower():
                    if account["server"].lower() == server.lower():
                        return True
            return False

    def verify_account(self, login, password):
        with open ("accounts.json", "r") as file:
            accounts = json.load(file)
            for account in accounts:
                if account["username"].lower() == login.lower() or account["email"].lower() == login.lower():
                    if account["password"] == password:
                        return True
            return False
        
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

        with open ("accounts.json", "w") as file:
            file.append(serialised)


