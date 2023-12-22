# observer
from transaction import TransactionObserver

# Această clasă gestioneaza observatorul de căutare
class SearchObserver(TransactionObserver):
    def update(self, event):
        if event.action == "Search":
            print("Performing search for stocks...")

# Această clasă gestioneaza observatorul de cumpărare
class BuyObserver(TransactionObserver):
    def update(self, event):
        if event.action == "Buy":
            print(f"Buying {event.quantity} shares of {event.stock_name} at ${event.price} each...")

# Această clasă gestioneaza observatorul de vânzare
class SellObserver(TransactionObserver):
    def update(self, event):
        if event.action == "Sell":
            user = User.get_instance()
            user.display_portfolio()

