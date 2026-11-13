from abc import ABC, abstractmethod

print("--- ЭТАП 4: SOLID и Заказы ---")

# [Интерфейсы и User]
class GreetingInterface(ABC):
    @abstractmethod
    def greet(self): pass
class User(ABC):
    def __init__(self, name: str): self._name = name
    @property
    def name(self): return self._name
    @abstractmethod
    def get_role(self): pass

# [Склад]
class Storage:
    def __init__(self): self._products = []
    def add_product(self, product, quantity):
        product.quantity += quantity
        if product not in self._products: self._products.append(product)
    def check_availability(self, product, requested_qty) -> bool:
        return product.quantity >= requested_qty

# [Товар]
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

# [Клиент и Менеджер]
class Client(User, GreetingInterface):
    def __init__(self, name: str, balance: float):
        super().__init__(name); self._balance = balance
    def get_role(self): return "Клиент"
    def greet(self): return f"Привет, я {self.name}."
class Manager(User, GreetingInterface):
    def __init__(self, name: str, warehouse: Storage):
        super().__init__(name); self._warehouse = warehouse
    def get_role(self): return "Менеджер"
    def greet(self): return f"Здравствуйте, я {self.name}."
    def add_product_to_warehouse(self, product, quantity):
        self._warehouse.add_product(product, quantity)

# --- НОВОЕ (Задание 10, 11): Класс Заказа (SRP - единственная ответственность) ---
class Order:
    def __init__(self, client: Client, product: Product, quantity: int):
        self.client = client
        self.product = product
        self.quantity = quantity
        self.status = "Ожидает проверки"

    # Логика подтверждения вынесена сюда (SOLID)
    def check_and_confirm(self, manager: Manager, storage: Storage):
        print(f"[Заказ] Менеджер {manager.name} проверяет заказ...")
        if storage.check_availability(self.product, self.quantity):
            self.status = "Подтвержден"
            self.product.quantity -= self.quantity
            print(f"[Заказ] Успешно! Куплено {self.quantity} шт.")
        else:
            self.status = "Отклонен"
            print("[Заказ] ОТКЛОНЕН. Нет в наличии.")

# Тест
storage = Storage()
manager = Manager("Алексей", storage)
client = Client("Иван", 5000)
phone = Product("Смартфон", 15000)
manager.add_product_to_warehouse(phone, 10)

order = Order(client, phone, 2)
order.check_and_confirm(manager, storage)