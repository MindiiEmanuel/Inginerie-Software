#user.py
from transaction import TransactionHistory, TransactionManager
from datetime import datetime

class AuthMemento:
    def __init__(self, user):
        self.name = user.name
        self.password = user.password
        self.amount = user.amount
        self.authenticated = user.authenticated

class User:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.name = None
        self.password = None
        self.amount = 0
        self.authenticated = False
        self.portfolio = []  # Adăugăm lista pentru portofoliu
        self.transaction_history = TransactionHistory()

    def reset_authentication(self):
        self.authenticated = False

    def create_memento(self):
        return AuthMemento(self)

    def restore_from_memento(self, memento):
        self.name = memento.name
        self.password = memento.password
        self.amount = memento.amount
        self.authenticated = memento.authenticated

    # Modifică metoda add_to_portfolio în clasa User pentru a adăuga informații în formatul specific
    def add_to_portfolio(self, stock_name, stock_symbol, quantity, price):
        transaction_info = {
            "name": stock_name,
            "symbol": stock_symbol,
            "quantity": quantity,
            "price": price
        }
        self.portfolio.append(transaction_info)

    def display_portfolio(self):
        print("\nPortfolio:")
        if not self.portfolio:
            print("Portfolio empty.")
            return

        for transaction in self.portfolio:
            print(f"Name: {transaction['name']} ({transaction['symbol']})")
            print(f"   - Number of Shares: {transaction['quantity']}")
            print(f"   - Price: ${transaction['price']}")
    
        print()

    def sell_transaction(self, transaction):
        symbol = transaction['symbol']
        quantity = int(input(f"Number of Shares to sell for {symbol}: "))
    
        stock = StockListCommand._stocks.get(symbol)
        if stock:
            stock['quantity'] += quantity
            print(f"You have successfully sold {quantity} shares of {symbol}.")
            print(f"Remaining {symbol} shares: {stock['quantity']}")
        
            # Actualizează portofoliul
            transaction['quantity'] -= quantity
        
            # Notifică observatorii despre acțiunea de vânzare
            event = TransactionEvent("Sell", symbol, quantity, stock['price'])
            TransactionManager.notify_observers(event)
        
            # Afiseaza portofoliul actualizat
            self.display_portfolio()
        else:
            print("Invalid symbol. Please check your input.")

def display_authenticated_menu():
    user = User.get_instance()
    print(f"Welcome, {user.name}!")
    print("1. Portfolio")
    print("2. Trading")
    print("3. Stock List")
    print("4. History")
    print("5. Logout")

def registration():
    user = User.get_instance()
    print("Registration")
    if user.authenticated:
        print("You are already registered and logged in.")
        return

    user.name = input("Name: ")
    user.password = input("Password: ")
    user.amount = float(input("Add Amount: "))
    print("Account saved successfully!")

def authentication():
    user = User.get_instance()
    print("Authentication")
    if user.authenticated:
        print("You are already logged in.")
        return

    name_input = input("Name: ")
    password_input = input("Password: ")

    if name_input == user.name and password_input == user.password:
        user.authenticated = True
        print("Authentication successful!")
        return True
    else:
        print("Authentication failed. Invalid credentials.")
        return False

def logout():
    user = User.get_instance()
    print("Logging out...")
    memento = user.create_memento()
    user.reset_authentication()
    print("Logout successful.")
    return memento
