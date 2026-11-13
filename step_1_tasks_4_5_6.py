print("--- ЭТАП 1: Классы, методы и инкапсуляция ---")

class Product:
    def __init__(self, name: str, price: float, quantity: int = 0):
        self._name = name
        self._price = None
        self._quantity = None
        self.price = price 
        self.quantity = quantity

    # Задание 6: Инкапсуляция (геттер и сеттер с проверкой)
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Цена должна быть больше нуля!")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if value < 0:
            raise ValueError("Количество не может быть отрицательным!")
        self._quantity = value

# Задание 4, 5: Создание объекта и вызов методов
phone = Product("Смартфон", 15000.0, 10)
print(f"Товар: {phone._name}, Цена: {phone.price}, Количество: {phone.quantity}")

try:
    phone.price = -100 # Проверка сеттера
except ValueError as e:
    print(f"Ошибка: {e}")