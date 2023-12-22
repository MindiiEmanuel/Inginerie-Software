#stock

class StockListCommand:
    _stocks = {
        "MSFT": {"name": "Microsoft Corporation", "quantity": 20, "price": 300},
        "AAPL": {"name": "Apple Inc.", "quantity": 15, "price": 175},
        "AMZN": {"name": "Amazon.com Inc.", "quantity": 10, "price": 3200},
        "TSLA": {"name": "Tesla Inc.", "quantity": 5, "price": 800}
    }

    def execute(self):
        print("Stock List:")
        for stock_symbol, stock_data in self._stocks.items():
            print_stock(stock_data['name'], stock_symbol, stock_data['quantity'], stock_data['price'])

def print_stock(name, ticker, quantity, price):
    print(f"**{name} ({ticker})**")
    print(f"   - Number of Shares: {quantity}")
    print(f"   - Price: ${price}\n")

