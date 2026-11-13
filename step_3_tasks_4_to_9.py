from abc import ABC, abstractmethod

print("--- ЭТАП 3: Композиция и Делегирование ---")

# [Код интерфейсов и User из Файла 2 без изменений]
class GreetingInterface(ABC):
    @abstractmethod
    def greet(self): pass

class User(ABC):
    def __init__(self, name: str): self._name = name
    @property
    def name(self): return self._name
    @abstractmethod
    def get_role(self): pass

# --- НОВОЕ (Задание 9): Класс Склад (композит) ---
class Storage:
    def __init__(self):
        self._products = []
    def add_product(self, product, quantity):
        product.quantity += quantity
        if product not in self._products: self._products.append(product)
        print(f"[Склад] Добавлено {quantity} шт. '{product._name}'.")

# [Код Product из Файла 2 без изменений]
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

# --- ОБНОВЛЕННЫЙ Manager (Задание 9: Композиция + Делегирование) ---
class Manager(User, GreetingInterface):
    def __init__(self, name: str, warehouse: Storage): # Композиция
        super().__init__(name)
        self._warehouse = warehouse

    def get_role(self): return "Менеджер"
    def greet(self): return f"Здравствуйте, я {self.name}."
    
    # Делегирование
    def add_product_to_warehouse(self, product, quantity):
        self._warehouse.add_product(product, quantity)

class Client(User, GreetingInterface):
    def __init__(self, name: str, balance: float):
        super().__init__(name)
        self._balance = balance
    def get_role(self): return "Клиент"
    def greet(self): return f"Привет, я {self.name}."

# Тест
storage = Storage()
manager = Manager("Алексей", storage)
phone = Product("Смартфон", 15000)
manager.add_product_to_warehouse(phone, 10) # Работает через делегирование