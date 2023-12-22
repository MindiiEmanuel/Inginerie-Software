# transaction.py

from datetime import datetime

# Această clasă gestioneaza evenimentele de tranzacții
class TransactionEvent:
    def __init__(self, action, stock_name, stock_symbol, quantity, price, timestamp):
        self.action = action
        self.stock_name = stock_name
        self.stock_symbol = stock_symbol
        self.quantity = quantity
        self.price = price
        self.timestamp = timestamp

# Această clasă gestioneaza observatorii (subscriitorii)
class TransactionObserver:
    def update(self, event):
        pass

# Această clasă gestioneaza tranzacțiile și notificarea observatorilor
class TransactionManager:
    _observers = []

    @classmethod
    def add_observer(cls, observer):
        cls._observers.append(observer)

    @classmethod
    def remove_observer(cls, observer):
        cls._observers.remove(observer)

    @classmethod
    def notify_observers(cls, event):
        for observer in cls._observers:
            observer.update(event)

class TransactionHistory:
    def __init__(self):
        self.history = []

    def add_transaction(self, event):
        self.history.append(event)

    def display_history(self):
        print("\nTransaction History:")
        if not self.history:
            print("No transactions in history.")
            return

        for index, transaction in enumerate(self.history, start=1):
            print(f"{index}. Action: {transaction.action}")
            print(f"   Stock: {transaction.stock_name} ({transaction.stock_symbol})")
            print(f"   Quantity: {transaction.quantity} shares")
            print(f"   Price per share: ${transaction.price}")
            print(f"   Timestamp: {transaction.timestamp}")
            print()
