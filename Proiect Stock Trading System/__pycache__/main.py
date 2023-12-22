# main
from user import User, display_authenticated_menu, registration, authentication, logout
from transaction import TransactionEvent, TransactionManager, TransactionObserver, TransactionHistory
from stock import StockListCommand
from strategy import BuyStrategy
from observer import SearchObserver, BuyObserver, SellObserver
from commands import SearchCommand, TradingCommand, HistoryCommand

def main():
    user = User.get_instance()
    memento_stack = []
    stock_list_command = StockListCommand()
    transaction_manager = TransactionManager()

    # Observatorii necesari pentru tranzacții
    search_observer = SearchObserver()
    buy_observer = BuyObserver()
    sell_observer = SellObserver()

    transaction_manager.add_observer(search_observer)
    transaction_manager.add_observer(buy_observer)
    transaction_manager.add_observer(sell_observer)

    trading_command = TradingCommand()
    history_command = HistoryCommand()

    while True:
        if user.authenticated:
            display_authenticated_menu()
            choice = input("Your choice: ")

            if choice == "1":
                user.display_portfolio()
            elif choice == "2":
                trading_command.execute(transaction_manager)
            elif choice == "3":
                stock_list_command.execute()
                choice = input("B. Back\nYour choice: ")
                if choice.upper() == "B":
                    continue
            elif choice == "4":
                HistoryCommand().execute()
            elif choice == "5":
                memento = logout()
                memento_stack.append(memento)
            else:
                print("Invalid choice. Please enter a valid option.")
        else:
            print("Numele aplicatiei: Stock Trading System")
            print("1. Authentication")
            print("2. Registration")
            print("3. Exit")

            choice = input("Your choice: ")

            if choice == "1":
                if authentication():
                    continue
            elif choice == "2":
                registration()
            elif choice == "3":
                print("Exiting Stock Trading System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

            user.reset_authentication()

if __name__ == "__main__":
    main()
