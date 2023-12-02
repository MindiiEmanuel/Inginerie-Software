# The BudgetFacade class provides a simplified interface to manage the budget,
# including operations like getting the budget, adding money, subtracting money, and displaying the budget for the client.
class BudgetFacade:
    def __init__(self):
        # Initialize the initial budget to 10000 euros
        self.budget = 10000

    def get_budget(self):
        # Get the current budget value
        return self.budget

    def add_money(self, amount):
        # Add a specified amount of money to the budget
        self.budget += amount

    def subtract_money(self, amount):
        # Subtract a specified amount of money from the budget
        self.budget -= amount

    def display_budget_client(self, user_budget):
        # Display the client's budget and provide options to go back
        print(f"Current budget: {user_budget.get_budget()} euros.")
        print("\nOptions:")
        print("B. Back")

        user_choice = input("Your choice: ")
        if user_choice.upper() == 'B':
            print("Going back.")
        else:
            print("Invalid choice. Please choose a valid option.")

# The UserBudget class represents the budget for a user, including operations like getting the budget, adding money, and subtracting money.
class UserBudget:
    def __init__(self, initial_budget):
        # Initialize the budget with the specified initial value
        self.budget = initial_budget

    def get_budget(self):
        # Get the current budget value
        return self.budget

    def add_money(self, amount):
        # Add a specified amount of money to the budget
        self.budget += amount

    def subtract_money(self, amount):
        # Subtract a specified amount of money from the budget
        self.budget -= amount

# The AddProductState class represents the state of adding a new product to the stock.
class AddProductState:
    def __init__(self, stock):
        # Initialize the state with a reference to the stock
        self.stock = stock

    def handle_input(self, user_input):
        # Handle user input during the process of adding a new product
        if user_input.upper() == 'S':
            # Save the product to the stock
            self.save_product()
            return None  # Move back to the previous state
        elif user_input.upper() == 'R':
            # Cancel and move back to the previous state
            return None
        elif user_input.upper() == 'ID':
            # Display the automatically assigned product ID
            print(f"Id Product: {len(self.stock.products) + 1}")
            return None  # Move back to the previous state
        elif user_input.upper() == 'NAME':
            # Set the name of the new product
            self.new_product["name"] = input("Name: ")
        elif user_input.upper() == 'PRICE':
            # Set the price of the new product
            self.new_product["price"] = float(input("Price: "))
        elif user_input.upper() == 'QUANTITY':
            # Set the quantity of the new product
            self.new_product["quantity"] = int(input("Quantity: "))
        else:
            print("Invalid choice. Please choose a valid option.")
        return user_input

    def save_product(self):
        # Save the new product to the stock
        new_product_id = len(self.stock.products) + 1
        self.stock.products[new_product_id] = {
            "name": self.new_product["name"],
            "price": self.new_product["price"],
            "quantity": self.new_product["quantity"],
        }
        print("Product saved.")

    def add_product(self):
        print("Adding new product:")
        # Initialize the state for adding products
        self.current_state = AddProductState(self.stock)

        while True:
            print("\nOptions:")
            print("ID: Id Product (automatically assigned)")
            print("NAME: Name of the product")
            print("PRICE: Price of the product")
            print("QUANTITY: Quantity of the product")
            print("S. Save")
            print("R. Revocation")
            print("CHOOSE: Choose (S/R)")

            user_input = input("Your choice: ")

            # Collect user input and update the state
            next_state = self.current_state.handle_input(user_input)

            if next_state is None:
                # Close the state and return to the main menu
                break


# Defining interfaces SellerInterface and ClientInterface to represent strategies for displaying options.
class SellerInterface:
    def show_options(self):
        pass

class ClientInterface:
    def show_options(self):
        pass

# Concrete implementation of interfaces for displaying options.
class SellerOptions(SellerInterface):
    def show_options(self):
        print("Options for Seller:")
        print("1. Stock")
        print("2. Add Product")
        print("3. Configure Promotion")
        print("4. Budget")
        print("5. Logout")

class ClientOptions(ClientInterface):
    def show_options(self):
        print("Options for Client:")
        print("1. Place Order")
        print("2. Cart")
        print("3. Budget")
        print("4. Logout")

    # Method to handle user login and interaction for a client.
    def handle_user(self):
        user_username = input("Enter client username: ")
        user_password = input("Enter client password: ")

        # Authenticate the client using the auth_manager and obtain the user object.
        user = self.auth_manager.login(user_username, user_password, role="client")

        if user:
            print(f"Connected Client: {user.username}")

            while True:
                # Display client options and handle user choices.
                user_interface = ClientOptions()
                user_menu = UserMenu(user_interface)
                user_menu.show_menu()

                client_choice = input("Your choice: ")
                if client_choice == '1':
                    print("Option 1: Place Order")
                    self.client_actions.place_order()
                elif client_choice == '2':
                    print("Option 2: Cart")
                    self.client_actions.display_cart()
                elif client_choice == '3':
                    print("Option 3: Budget")
                    self.client_actions.display_budget()
                elif client_choice == '4':
                    print("Logging out.")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
        else:
            print("Invalid credentials for client.")

# Class representing various actions that a client can perform.
class ClientActions:
    def __init__(self, auth_manager, stock):
        self.auth_manager = auth_manager
        self.client_budget = UserBudget(1000)  # Initialize the client's budget to 1000 euros
        self.user = None
        self.stock = stock
        self.cart = {}

    # Method to handle client login and initialize client-related data.
    def login(self, user_username, user_password):
        self.user = self.auth_manager.login(user_username, user_password, role="client")

        if self.user:
            # Initialize the client's budget to 1000 euros upon login
            self.client_budget = UserBudget(1000)
            print(f"Connected Client: {self.user.username}")

    # Method to display the client's budget.
    def display_budget(self):
        while True:
            print(f"Current budget: {self.client_budget.get_budget()} euros.")
            print("\nOptions:")
            print("B. Back")

            user_choice = input("Your choice: ")
            if user_choice.upper() == 'B':
                print("Going back.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    # Method to place an order for products from the stock.
    def place_order(self):
        print("Displaying stock...")
        self.stock.show_stock()

        product_details = None  # Initialize with a default value

        while True:
            product_id = input("Choose Product (or type 'B' to go back): ")

            if product_id.upper() == 'B':
                break

            if product_id.isdigit() and int(product_id) in self.stock.products:
                product_details = self.stock.products[int(product_id)]  # Get details directly from the stock
                quantity = input("Choose the Quantity (max 100): ")

                if quantity.isdigit() and 0 < int(quantity) <= 100:
                    add_to_cart = input("Add to Cart? (y/n): ")
                    if add_to_cart.lower() == 'y':
                        self.cart[int(product_id)] = {
                            "name": product_details["name"],
                            "price": product_details["price"],
                            "quantity": int(quantity),
                        }
                        print("Product added to Cart.")
                    else:
                        print("Product not added to Cart.")
                else:
                    print("Invalid quantity. Please choose a number between 1 and 100.")
            else:
                print("Invalid product ID. Please choose a valid ID from the stock.")

        print("Order placed.")

    # Method to display the contents of the client's cart and handle payment.
    def display_cart(self):
        print("Cart:")
        total_price = 0
        for item_id, item_details in self.cart.items():
            quantity = item_details['quantity']
            product_price = item_details['price']
            print(f"{item_id}. {item_details['name']}: {product_price} euros/kg - {quantity} kg")
            total_price += product_price * quantity

        print(f"Total price: {total_price} euros")

        pay_choice = input("Pay? (y/n): ")
        if pay_choice.lower() == 'y':
            self.process_order(self.cart, total_price)
        else:
            print("Payment cancelled.")

    # Method to process the client's order, update stock and client budget.
    def process_order(self, cart, total_price):
        # Get the budget directly from ClientActions
        client_budget = self.client_budget  

        # Update the stock and seller's budget
        for product_id, item_details in cart.items():
            product_details = self.stock.products[product_id]
            product_name = product_details["name"]
            product_price = item_details["price"]
            total_product_price = item_details["quantity"] * product_price

            # Check if there is enough stock available
            if product_details["quantity"] < item_details["quantity"]:
                print(f"Error: Not enough stock available for {product_name}. Order cancelled.")
                return

            # Update stock
            self.stock.products[product_id]["quantity"] -= item_details["quantity"]

            # Update client's budget
            client_budget.subtract_money(total_product_price)

        # Clear the cart after processing the order
        cart.clear()

        # Display the confirmation message
        print("Order processed successfully.")
        print("Updated stock:")
        self.stock.show_stock()
        print(f"Current budget: {client_budget.get_budget()} euros.")

    # Method to handle user interaction for the client.
    def handle_user(self):
        user_username = input("Enter client username: ")
        user_password = input("Enter client password: ")

        self.user = self.auth_manager.login(user_username, user_password, role="client")

        if self.user:
            print(f"Connected Client: {self.user.username}")

            while True:
                user_interface = ClientOptions()
                user_menu = UserMenu(user_interface)
                user_menu.show_menu()

                client_choice = input("Your choice: ")
                if client_choice == '1':
                    print("Option 1: Place Order")
                    self.place_order()
                elif client_choice == '2':
                    print("Option 2: Cart")
                    self.display_cart()
                elif client_choice == '3':
                    print("Option 3: Budget")
                    self.display_budget()
                elif client_choice == '4':
                    print("Logging out.")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
        else:
            print("Invalid credentials for client.")


# Context using the strategies
class UserMenu:
    def __init__(self, user_interface):
        self.user_interface = user_interface

    def set_user_interface(self, user_interface):
        self.user_interface = user_interface

    def show_menu(self):
        self.user_interface.show_options()

# Utilizarea pattern-ului Singleton pentru autentificare
class AuthManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AuthManager, cls).__new__(cls)
            cls._instance.users = {"owner": "owner", "client": {"client": "client"}}  # Adaugare utilizator "client"
        return cls._instance

    def login(self, username, password, role):
        if role == "client" and username in self.users["client"] and self.users["client"].get(username) == password:
            # Obținem bugetul clientului sau îl setăm la 1000 dacă nu există încă
            initial_budget = self.users["client"].get(username, 1000)
            user_budget = UserBudget(initial_budget)
            user = User(username, role, user_budget)
            return user
        elif role != "client" and username in self.users and self.users[username] == password:
            return User(username, role, None)  # Pentru alți utilizatori, bugetul este None
        else:
            return None

# Context using the strategies
class UserMenu:
    def __init__(self, user_interface):
        self.user_interface = user_interface

    def set_user_interface(self, user_interface):
        self.user_interface = user_interface

    def show_menu(self):
        # Display options based on the selected strategy (Seller or Client)
        self.user_interface.show_options()

# Implementation of the Singleton pattern for authentication
class AuthManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Create a new instance only if it doesn't exist
            cls._instance = super(AuthManager, cls).__new__(cls)
            cls._instance.users = {"owner": "owner", "client": {"client": "client"}}  # Adding a "client" user
        return cls._instance

    def login(self, username, password, role):
        if role == "client" and username in self.users["client"] and self.users["client"].get(username) == password:
            # Get the client's budget or set it to 1000 if not yet available
            initial_budget = self.users["client"].get(username, 1000)
            user_budget = UserBudget(initial_budget)
            user = User(username, role, user_budget)
            return user
        elif role != "client" and username in self.users and self.users[username] == password:
            # For other users, budget is set to None
            return User(username, role, None)
        else:
            return None

# User class representing a user with a username, role, and optional budget
class User:
    def __init__(self, username, role, user_budget):
        self.username = username
        self.role = role
        self.user_budget = user_budget

# Interface for the stock completion strategy
class StockCompletionStrategy:
    def complete_stock(self, stock):
        pass

# Concrete strategy: Automatically complete stock to 100 kg for each product
class AutomaticCompletionStrategy:
    def complete_stock(self, stock, budget_facade):  # Remove the first argument 'self'
        for product_id, details in stock.products.items():
            if details['quantity'] < 100:
                quantity_to_add = 100 - details['quantity']
                total_cost = details['price'] * quantity_to_add

                # Update the budget
                budget_facade.subtract_money(total_cost)

                # Update the quantity in stock
                stock.products[product_id]['quantity'] += quantity_to_add

        print("Automatic completion complete.")

# Concrete strategy: Update the budget based on stock
class BudgetUpdateStrategy(StockCompletionStrategy):
    def complete_stock(self, stock, budget_facade):
        total_cost = 0
        for product_id, details in stock.products.items():
            if details["quantity"] != 100:
                quantity_to_buy = 100 - details["quantity"]
                total_cost += quantity_to_buy * details["price"]

        if total_cost > 0:
            budget_facade.subtract_money(total_cost)
            print(f"Stock updated. Budget decreased by {total_cost} euros.")
        else:
            print("Stock full. No budget changes.")

# Stock class representing a list of products
class Stock:
    def __init__(self):
        # Initial products in stock
        self.products = {
            1: {"name": "Carrot", "price": 1, "quantity": 100},
            # ... (other products)
        }

        self.completion_strategy = None

    def set_completion_strategy(self, completion_strategy):
        # Set the strategy for completing the stock
        self.completion_strategy = completion_strategy

    def show_stock(self):
        # Display the details of products in stock
        for product_id, details in self.products.items():
            print(f"{product_id}. {details['name']}: {details['price']} euros/kg - {details['quantity']} kg")

    def complete_stock(self, budget_facade):
        # Use the selected strategy to complete the stock
        if self.completion_strategy:
            self.completion_strategy.complete_stock(self, budget_facade)
        else:
            print("Error: No completion strategy set.")

# State class for adding a new product to the stock
class AddProductState:
    def __init__(self, stock):
        self.stock = stock

    def handle_input(self, user_input):
        if user_input.upper() == 'S':
            # Save the product to the stock
            self.save_product()
            return None  # Move back to the previous state
        elif user_input.upper() == 'R':
            # Cancel and return to the previous state
            return None
        else:
            # Continue collecting information
            return user_input

    def save_product(self):
        # Save the product to the stock (implementation may vary based on needs)
        new_product_id = len(self.stock.products) + 1
        new_product_name = input("Name: ")
        new_product_price = float(input("Price: "))
        new_product_quantity = int(input("Quantity: "))

        self.stock.products[new_product_id] = {
            "name": new_product_name,
            "price": new_product_price,
            "quantity": new_product_quantity,
        }

        print("Product saved.")


# SellerActions class with modifications to the show_stock and stock_filling methods
class SellerActions:
    def __init__(self):
        self.current_state = None

    def show_stock(self):
        # Display stock and options for the seller
        while True:
            print("Displaying stock...")
            self.stock.show_stock()
            print("\nOptions:")
            print("C. Complete the stock")
            print("B. Back")

            user_choice = input("Your choice: ")
            if user_choice.upper() == 'C':
                self.stock_filling()
            elif user_choice.upper() == 'B':
                print("Going back.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

        print("Stock displayed.")

    def stock_filling(self):
        # Choose a strategy to complete the stock and execute it
        print("Completing the stock...")
        self.stock.show_stock()
        print("\nOptions:")
        print("1. Automatic Completion")
        print("2. Budget-Dependent Completion")
        print("B. Back")

        user_choice = input("Your choice: ")
        if user_choice == '1':
            self.stock.set_completion_strategy(AutomaticCompletionStrategy())
            self.stock.complete_stock(self.budget_facade)
        elif user_choice == '2':
            self.stock.set_completion_strategy(BudgetUpdateStrategy())
            self.stock.complete_stock(self.budget_facade)
        elif user_choice.upper() == 'B':
            print("Going back.")
        else:
            print("Invalid choice. Please choose a valid option.")

    # Other methods for adding a product, configuring promotion, and displaying budget

    def handle_user(self):
        # Authentication and menu handling for the seller
        self.auth_manager = AuthManager()
        self.budget_facade = BudgetFacade()
        self.stock = Stock()

        user_username = input("Enter seller username: ")
        user_password = input("Enter seller password: ")

        user = self.auth_manager.login(user_username, user_password, role="seller")

        if user:
            print(f"Connected Seller: {user.username}")

            while True:
                user_interface = SellerOptions()
                user_menu = UserMenu(user_interface)
                user_menu.show_menu()

                seller_choice = input("Your choice: ")
                if seller_choice == '1':
                    print("Option 1: Stock")
                    self.show_stock()
                # ... (other options)
                elif seller_choice == '5':
                    print("Logging out.")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
        else:
            print("Invalid credentials for seller.")

# eShopPlatform class with modifications to the handle_user method
class eShopPlatform:
    def __init__(self):
        # Initialization of authentication, budget, stock, and user actions
        self.auth_manager = AuthManager()
        self.budget_facade = BudgetFacade()
        self.stock = Stock()
        self.seller_actions = SellerActions()
        self.client_actions = ClientActions(self.auth_manager, self.stock)

        # Variable to track if the user has logged out
        self.logged_out = False

    def run(self):
        # Main loop for the eShop platform
        print("eShop Platform")
        while True:
            if self.logged_out:
                self.logged_out = False
            else:
                print("\nChoose the role:")
                print("1. Seller")
                print("2. Client")
                print("3. Exit")
                
                choice = input("Your choice: ")

                if choice == '1':
                    self.seller_actions.handle_user()
                elif choice == '2':
                    self.client_actions.handle_user()
                elif choice == '3':
                    print("Exiting eShop Platform. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")

    def handle_user(self, role):
        # Authentication and menu handling for both seller and client
        user_username = input(f"Enter {role} username: ")
        user_password = input(f"Enter {role} password: ")

        user = self.auth_manager.login(user_username, user_password, role=role)

        if user:
            print(f"Connected {role.capitalize()}: {user.username}")

            if role == "seller":
                while True:
                    user_interface = SellerOptions()
                    user_menu = UserMenu(user_interface)
                    user_menu.show_menu()

                    seller_choice = input("Your choice: ")
                    if seller_choice == '1':
                        print("Option 1: Stock")
                        self.seller_actions.show_stock()
                    # ... (other options)
                    elif seller_choice == '5':
                        print("Logging out.")
                        self.logged_out = True  # Set the flag to return to the role choice
                        break
                    else:
                        print("Invalid choice. Please choose a valid option.")

            elif role == "client":
                while True:
                    user_interface = ClientOptions()
                    user_menu = UserMenu(user_interface)
                    user_menu.show_menu()

                    client_choice = input("Your choice: ")
                    if client_choice == '1':
                        print("Option 1: Place Order")
                        # Add logic for the Place Order option
                    elif client_choice == '2':
                        print("Option 2: Budget")
                        self.client_actions.display_budget()
                    elif client_choice == '3':
                        print("Logging out.")
                        self.logged_out = True  # Set the flag to return to the role choice
                        break
                    else:
                        print("Invalid choice. Please choose a valid option.")
        else:
            print(f"Invalid credentials for {role}.")

# Example of usage
if __name__ == "__main__":
    eshop_platform = eShopPlatform()
    eshop_platform.run()

