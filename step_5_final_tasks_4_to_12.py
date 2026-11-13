from abc import ABC, abstractmethod

print("--- ЭТАП 5: ФИНАЛЬНЫЙ КОД С ПАТТЕРНОМ ФАБРИКА ---")

# [Интерфейсы]
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

# [Заказ]
class Order:
    def __init__(self, client: Client, product: Product, quantity: int):
        self.client = client; self.product = product; self.quantity = quantity
        self.status = "Ожидает проверки"
    def check_and_confirm(self, manager: Manager, storage: Storage):
        if storage.check_availability(self.product, self.quantity):
            self.status = "Подтвержден"
            self.product.quantity -= self.quantity
            print(f"[Заказ] Успешно! Куплено {self.quantity} шт.")
        else:
            self.status = "Отклонен"
            print("[Заказ] ОТКЛОНЕН. Нет в наличии.")

# --- НОВОЕ (Задание 12): ПАТТЕРН ФАБРИКА ---
class UserFactory:
    @staticmethod
    def create_user(role: str, name: str, **kwargs):
        if role == "client":
            return Client(name, balance=kwargs.get('balance', 0.0))
        elif role == "manager":
            return Manager(name, warehouse=kwargs.get('warehouse'))
        else:
            raise ValueError("Неизвестная роль")

# --- ТЕСТИРОВАНИЕ С ИСПОЛЬЗОВАНИЕМ ФАБРИКИ ---
if __name__ == "__main__":
    print("--- ЭТАП 5: ФИНАЛЬНЫЙ КОД С ПАТТЕРНОМ ФАБРИКА ---")
    
    storage = Storage()
    
    # Создаем через фабрику!
    client = UserFactory.create_user("client", "Иван", balance=5000.0)
    manager = UserFactory.create_user("manager", "Алексей", warehouse=storage)
    
    # Проверяем интерфейс приветствия (Задание 8)
    print(client.greet())
    print(manager.greet())
    
    phone = Product("Смартфон", 15000)
    manager.add_product_to_warehouse(phone, 10)
    
    # Клиент делает успешный заказ
    order = Order(client, phone, 2)
    order.check_and_confirm(manager, storage)
    
    # --- ВОТ ЭТОГО У ТЕБЯ, СКОРЕЕ ВСЕГО, НЕТ ---
    # Клиент пытается заказать больше, чем есть (ошибка)
    print("\n--- Попытка заказать больше, чем есть ---")
    order2 = Order(client, phone, 100)
    order2.check_and_confirm(manager, storage)

    # Проверка ограничений (Инкапсуляция)
    print("\n--- Проверка ограничений (Сеттеры) ---")
    try:
        phone.price = -100
    except ValueError as e:
        print(f"Ошибка при изменении цены: {e}")    