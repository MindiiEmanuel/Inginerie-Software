class Calculator:
    def __init__(self):
        # Inițializăm valoarea curentă a calculatorului și listele pentru istoric și viitor
        self.current_value = 0
        self.history = []
        self.future = []

    def handle_operation(self, operator, value):
        # Manipulează operațiile și valorile corespunzătoare și adaugă la istoricul valorii curente
        if operator == '+':
            self.history.append(self.current_value)
            self.current_value += value
            self.future = []  # Curăță lista pentru viitor
        elif operator == '-':
            self.history.append(self.current_value)
            self.current_value -= value
            self.future = []
        elif operator == '*':
            self.history.append(self.current_value)
            self.current_value *= value
            self.future = []
        elif operator == '/':
            self.history.append(self.current_value)
            self.current_value /= value
            self.future = []

    def undo(self):
        # Întoarce ultima valoare din istoric și adaugă valoarea actuală la viitor
        if self.history:
            self.future.append(self.current_value)
            self.current_value = self.history.pop()

    def redo(self):
        # Reface ultima valoare din viitor și adaugă valoarea actuală la istoric
        if self.future:
            self.history.append(self.current_value)
            self.current_value = self.future.pop()


if __name__ == '__main__':
    calc = Calculator()
    print("Calculator is on. Available operations: '+', '-', '*', '/', 'undo', 'redo', 'exit'.")

    while True:
        user_input = input("Enter operation: ")
        if user_input == 'exit':
            print("Exiting calculator.")
            break

        if user_input in ['+', '-', '*', '/']:
            operator = user_input
            value = float(input("Enter value: "))
            calc.handle_operation(operator, value)
            print("Current value:", calc.current_value)

        elif user_input == 'undo':
            calc.undo()
            print("After undoing:", calc.current_value)

        elif user_input == 'redo':
            calc.redo()
            print("After redoing:", calc.current_value)

        else:
            print("Invalid operation. Please try again.")
