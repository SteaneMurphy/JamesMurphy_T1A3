import json


class Account:
    def __init__(
        self,
        username,
        server,
        email,
        firstname,
        lastname,
        password,
        currency=0,
        items=None,
    ):
        self._username = username
        self._server = server
        self._email = email
        self._firstname = firstname
        self._lastname = lastname
        self._password = password
        self._currency = currency
        self._items = items

    @property
    def username(self):
        return self._username

    @property
    def server(self):
        return self._server

    @property
    def email(self):
        return self._email

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def password(self):
        return self._password

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, amount):
        self._currency += amount

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        self._items = new_items
        
    def update_accounts(self, new_account=False):
        updated_information = {
            "username": self._username,
            "server": self._server,
            "email": self._email,
            "firstname": self._firstname,
            "lastname": self._lastname,
            "password": self._password,
            "currency": self._currency,
            "items": self._items,
        }

        if new_account:
            with open("accounts.json","r+", encoding="utf-8") as file:
                accounts = json.load(file)
                accounts.append(updated_information)
                file.seek(0)
                json.dump(accounts, file, indent=4)
        else:
            with open("accounts.json", "r", encoding="utf-8") as file:
                accounts = json.load(file)
                for account in accounts:
                    if account["username"] == self._username:
                        account["currency"] = self._currency
                        account["items"] = self._items

            with open("accounts.json", "w", encoding="utf-8") as file:
                json.dump(accounts, file, indent=4)
