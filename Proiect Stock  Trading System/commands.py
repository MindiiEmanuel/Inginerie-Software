# commands
from user import User
from stock import StockListCommand
from strategy import BuyStrategy
from transaction import TransactionEvent, TransactionManager, TransactionObserver, TransactionHistory
from datetime import datetime

class SearchCommand:
    def execute(self, transaction_manager):
        while True:
            print("Search by")
            print("1. Name")
            print("2. Symbol Ticker")
            print("3. Back")

            search_choice = input("Your choice: ")

            if search_choice == "1":
                search_by_name(transaction_manager)
            elif search_choice == "2":
                search_by_ticker(transaction_manager)
            elif search_choice == "3":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

search_command = SearchCommand()

# Această funcție gestioneaza căutarea
def search_by_name(transaction_manager):
    stock_names = ["Microsoft Corporation", "Apple Inc.", "Amazon.com Inc.", "Tesla Inc."]
    stock_tickers = ["MSFT", "AAPL", "AMZN", "TSLA"]

    while True:
        print("Enter the name of the stock:")
        for index, name in enumerate(stock_names, start=1):
            print(f"{index}. {name}")

        print(f"{len(stock_names) + 1}. Back")

        choice = input("Your choice: ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(stock_names):
                stock_name = stock_names[choice - 1]
                display_stock_info(stock_name)
            elif choice == len(stock_names) + 1:
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        else:
            print("Invalid choice. Please enter a valid option.")


def search_by_ticker(transaction_manager):
    stock_tickers = ["MSFT", "AAPL", "AMZN", "TSLA"]

    while True:
        print("Enter the symbol ticker of the stock:")
        for index, ticker in enumerate(stock_tickers, start=1):
            print(f"{index}. {ticker}")

        print(f"{len(stock_tickers) + 1}. Back")

        choice = input("Your choice: ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(stock_tickers):
                stock_ticker = stock_tickers[choice - 1]
                display_stock_info(stock_ticker)
            elif choice == len(stock_tickers) + 1:
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        else:
            print("Invalid choice. Please enter a valid option.")

def display_stock_info(stock_key):
    stock_data = {
        "MSFT": {"name": "Microsoft Corporation", "quantity": 20, "price": 300},
        "AAPL": {"name": "Apple Inc.", "quantity": 15, "price": 175},
        "AMZN": {"name": "Amazon.com Inc.", "quantity": 10, "price": 3200},
        "TSLA": {"name": "Tesla Inc.", "quantity": 5, "price": 800}
    }

    stock_info = stock_data.get(stock_key)
    if stock_info:
        print(f"**{stock_info['name']} ({stock_key})**")
        print(f"   - Number of Shares: {stock_info['quantity']}")
        print(f"   - Price: ${stock_info['price']}")
        print("B. Back\n")

class TradingCommand:
    def __init__(self):
        self.buy_strategy = BuyStrategy()

    def execute(self, transaction_manager):
        while True:
            print("1. Search")
            print("2. Buy")
            print("3. Sell")
            print("4. Back")

            trading_choice = input("Your choice: ")

            if trading_choice == "1":
                search_choice = input("Search by\n1. Name\n2. Symbol Ticker\n3. Back\nYour choice: ")
                if search_choice == "1":
                    search_by_name(transaction_manager)
                elif search_choice == "2":
                    search_by_ticker(transaction_manager)
                elif search_choice == "3":
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
            elif trading_choice == "2":
                self.buy_transaction()
            elif trading_choice == "3":
                self.sell_transaction(transaction_manager)
            elif trading_choice == "4":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def sell_transaction(self, transaction_manager):
        user = User.get_instance()
        user.display_portfolio()

        sell_choice = input("Sell: 1. Yes 2. No\nYour choice: ")

        if sell_choice == "1":
            symbol = input("Symbol: (e.g., MSFT, AAPL, AMZN, TSLA)\nYour choice: ")
            quantity = int(input("Number of Shares: (e.g., 1, 2, 3, ...)\nYour choice: "))

            for transaction in user.portfolio:
                if transaction['symbol'] == symbol and transaction['quantity'] >= quantity:
                    # Actualizăm portofoliul
                    transaction['quantity'] -= quantity

                    # Găsim acțiunea în Stock List
                    stock = StockListCommand._stocks.get(symbol)

                    if stock:
                        # Actualizăm Stock List cu acțiunile vândute
                        stock['quantity'] += quantity

                        # Notificăm observatorii despre acțiunea de vânzare
                        event = TransactionEvent("Sell", transaction['name'], symbol, quantity, stock['price'], datetime.now())
                        user.transaction_history.add_transaction(event)

                        # Afiseaza portofoliul actualizat
                        user.display_portfolio()

                        print(f"You have successfully sold {quantity} shares of {symbol}.")
                        print(f"Remaining {symbol} shares: {stock['quantity']}")
                        print(f"Sell {quantity} shares of {symbol} at ${stock['price']} each...")

                        break
            else:
                print("Insufficient quantity or invalid symbol. Please check your input.")
        elif sell_choice == "2":
            print("Sell canceled.")
        else:
            print("Invalid choice. Please enter a valid option.")

    def buy_transaction(self):
        while True:
            print("Symbol: (e.g., MSFT, AAPL, AMZN, TSLA)")
            symbol = input("Your choice: ")
            quantity = int(input("Number of Shares: (e.g., 1, 2, 3, ...)\nYour choice: "))
            strategy_sl = input("Strategy S/L (e.g., S for short, L for long):\nYour choice: ")

            # Verifică valoarea introdusă în strategy_sl
            if strategy_sl.upper() == 'S':
                print("Executing short-term buy transaction...")
            elif strategy_sl.upper() == 'L':
                print("Executing long-term buy transaction...")
            else:
                print("Invalid choice. Please enter S or L.")
                continue

            # Update Stock List
            stock = StockListCommand._stocks.get(symbol)
            if stock and stock['quantity'] >= quantity:
                stock['quantity'] -= quantity
                print(f"You have successfully bought {quantity} shares of {symbol}.")
                print(f"Remaining {symbol} shares: {stock['quantity']}")

                # Adaugăm tranzacția în portofoliu
                user = User.get_instance()
                user.add_to_portfolio(stock['name'], symbol, quantity, stock['price'])

                # Notificăm observatorii despre acțiunea de cumpărare
                event = TransactionEvent("Buy", stock['name'], symbol, quantity, stock['price'], datetime.now())
                TransactionManager.notify_observers(event)

                # Adăugăm tranzacția în istoric
                user.transaction_history.add_transaction(event)

                # Afiseaza portofoliul actualizat
                user.display_portfolio()

                break
            else:
                print("Insufficient quantity or invalid symbol. Please check your input.")
                break

    def is_valid_strategy(self, strategy_sl):
        import re
        pattern = re.compile(r"S\d+L\d+")
        return bool(pattern.match(strategy_sl))

trading_command = TradingCommand()

class BuyStrategy:
    def execute(self, symbol, quantity, price):
        pass


# Această clasă gestioneaza comanda History
class HistoryCommand:
    def execute(self):
        user = User.get_instance()
        user.transaction_history.display_history()
        while True:
            print("1. Back")

            history_choice = input("Your choice: ")

            if history_choice == "1":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

history_command = HistoryCommand()
