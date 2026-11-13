from abc import ABC, abstractmethod

print("--- ЭТАП 2: Наследование и Абстракции ---")

# --- НОВОЕ (Задание 8): Интерфейсы и абстракции ---
class GreetingInterface(ABC):
    @abstractmethod
    def greet(self): pass

class User(ABC):
    def __init__(self, name: str):
        self._name = name
    
    @property
    def name(self): return self._name
    
    @abstractmethod
    def get_role(self): pass

# --- НОВОЕ (Задание 7): Наследование ---
class Client(User, GreetingInterface):
    def __init__(self, name: str, balance: float):
        super().__init__(name)
        self._balance = balance

    def get_role(self): return "Клиент"
    def greet(self): return f"Привет, я {self.name}."

class Manager(User, GreetingInterface):
    def __init__(self, name: str):
        super().__init__(name)

    def get_role(self): return "Менеджер"
    def greet(self): return f"Здравствуйте, я {self.name}."

# --- СТАРОЕ ИЗ ФАЙЛА 1 (Задания 4, 5, 6) ---
class Product:
    def __init__(self, name: str, price: float, quantity: int = 0):
        self._name = name
        self._price = None
        self._quantity = None
        self.price = price 
        self.quantity = quantity

    @property
    def price(self): return self._price
    @price.setter
    def price(self, value: float):
        if value <= 0: raise ValueError("Цена должна быть больше нуля!")
        self._price = value

    @property
    def quantity(self): return self._quantity
    @quantity.setter
    def quantity(self, value: int):
        if value < 0: raise ValueError("Количество не может быть отрицательным!")
        self._quantity = value

# Тестируем новое
client = Client("Иван", 5000)
manager = Manager("Алексей")
print(client.greet())
print(manager.greet()) 