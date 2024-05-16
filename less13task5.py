from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Addition(Strategy):
    def execute(self, a, b):
        return a + b

class Subtraction(Strategy):
    def execute(self, a, b):
        return a - b

class Multiplication(Strategy):
    def execute(self, a, b):
        return a * b

class Division(Strategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

class Calculator:
    def __init__(self, strategy=None):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def calculate(self, a, b):
        if self._strategy is None:
            raise ValueError("Strategy not set.")
        return self._strategy.execute(a, b)

if __name__ == "__main__":
    # Создаем объект калькулятора
    calculator = Calculator()

    # Устанавливаем стратегию сложения и выполняем операцию
    calculator.set_strategy(Addition())
    result = calculator.calculate(10, 5)
    print(f"10 + 5 = {result}")

    # Устанавливаем стратегию вычитания и выполняем операцию
    calculator.set_strategy(Subtraction())
    result = calculator.calculate(10, 5)
    print(f"10 - 5 = {result}")

    # Устанавливаем стратегию умножения и выполняем операцию
    calculator.set_strategy(Multiplication())
    result = calculator.calculate(10, 5)
    print(f"10 * 5 = {result}")

    # Устанавливаем стратегию деления и выполняем операцию
    calculator.set_strategy(Division())
    result = calculator.calculate(10, 5)
    print(f"10 / 5 = {result}")