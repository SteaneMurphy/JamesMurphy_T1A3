class Account():

    def __init__(self, username, server, email, firstname, lastname, password, currency, items):
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

    