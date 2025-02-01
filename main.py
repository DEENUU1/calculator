class Calculator:
    def add(self, x: float, y: float) -> float:
        return x + y

    def subtract(self, x: float, y: float) -> float:
        return x - y

    def multiply(self, x: float, y: float) -> float:
        return x * y

    def divide(self, x: float, y: float) -> float:
        try:
            return x / y
        except ZeroDivisionError:
            print("Nie dziel przez 0!")


def get_number_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number!")


def main():
    calc = Calculator()

    operations = {
        '1': ('Dodawanie', calc.add),
        '2': ('Odejmowanie', calc.subtract),
        '3': ('Mnożenie', calc.multiply),
        '4': ('Dzielenie', calc.divide)
    }

    while True:
        print("Operacje:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("5. Wyjdź")
        print("=" * 20)

        choice = input("Wybierz opcję: (1-5): ")

        if choice == '5':
            break

        if choice not in operations:
            print("Wybierz opcję: (1-5)")
            continue

        operation_name, operation = operations[choice]

        num1 = get_number_input("Liczba A: ")
        num2 = get_number_input("Liczba B: ")

        try:
            result = operation(num1, num2)
            print(f"\nWynik: {result}")
        except ValueError as e:
            print(f"Błąd: {e}")


if __name__ == "__main__":
    main()