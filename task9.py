"""
Задача: Управление запасами

Описание: Напишите класс для управления запасами товаров на складе. Класс должен поддерживать следующие функции:

Добавление товара: Возможность добавлять новый товар с указанием его названия, количества и цены.

Удаление товара: Возможность удалять товар со склада.

Обновление количества товара: Возможность обновлять количество существующего товара.

Получение информации о товаре: Возможность получать информацию о товаре (название, количество, цена).

Подсчет общей стоимости всех товаров на складе: Метод, который возвращает общую стоимость всех товаров на складе
(количество * цена для каждого товара).

Пример использования:
inventory = Inventory()

# Добавление товаров
inventory.add_product("Яблоки", 100, 10)  # 100 яблок по 10 рублей
inventory.add_product("Бананы", 50, 20)   # 50 бананов по 20 рублей

# Получение информации о товаре
print(inventory.get_product_info("Яблоки"))  # Вывод: {'name': 'Яблоки', 'quantity': 100, 'price': 10}

# Обновление количества товара
inventory.update_product_quantity("Яблоки", 120)

# Подсчет общей стоимости
print(inventory.total_value())  # Вывод: 2200 (120 * 10 + 50 * 20)

# Удаление товара
inventory.remove_product("Бананы")

Ограничения:
Убедитесь, что при добавлении товара с уже существующим названием количество и цена обновляются.
При попытке удалить несуществующий товар должно возникать соответствующее исключение.
Обрабатывайте случаи, когда пользователь пытается получить информацию о несуществующем товаре.
"""


class Inventory:
    def __init__(self) -> None:
        self.__products = {}  # имитация БД (здесь будут храниться все продукты)-> {'name': {"quantity":2, "price":100}}

    @property
    def products(self) -> dict:
        return self.__products

    @staticmethod
    def check_parametrs(name=None, quantity=None, price=None):
        """проверка входных данных"""
        if name is not None:
            if not isinstance(name, str):
                raise TypeError(f"Ошибка ключ должен быть строкой, введено -> {name}")
        if quantity is not None:
            if not isinstance(quantity, int):
                raise TypeError(f"Ошибка количество должно быть числом, введено -> {quantity}")
            if quantity < 0:
                raise ValueError(f"Ошибка количество должно быть больше 0, введено -> {quantity}")
        if price is not None:
            if not isinstance(quantity, (int, float)):
                raise TypeError(f"Ошибка цена должна быть числом или дробным числом, введено -> {price}")
            if price < 0:
                raise ValueError(f"Ошибка цена не может быть отрицательной, введено -> {price}")

    def add_product(self, name: str, quantity: int, price: int | float) -> None:
        """
        добавить новый продукт
        :param name: наименование товара
        :param quantity: количество товара
        :param price: актуальная цена товара
        """
        self.check_parametrs(name, quantity, price)  # проверка входных параметров
        if name in self.__products:
            self.__products[name]['quantity'] = self.__products[name]['quantity'] + quantity
            self.__products[name]['price'] = price
        else:
            self.__products[name] = {'quantity': quantity, 'price': price}

    def update_product_quantity(self, name: str, quantity: int) -> None:
        """обновление количества товара"""
        self.check_parametrs(name, quantity)  # указываются проверяемые параметры
        if name in self.__products:
            self.__products[name]['quantity'] = quantity

    def get_product_info(self, name: str) -> dict | None:
        """
        получение информации о продукте (если правильный ключ есть)
        :param name: название запрашиваемого товара
        :return:
        """
        self.check_parametrs(name)  # указываются проверяемые параметры
        if name in self.__products:
            return {'name': name, **self.__products[name]}
        print(f"В БД нет продукта с названием {name}")
        return None

    def total_value(self) -> int | float:
        """
        сумма всех товаров (подсчет стоимости)
        """
        count = 0
        for product in self.__products:
            count += self.__products[product]['price'] * self.__products[product]['quantity']
        return count

    def remove_product(self, name: str) -> None:
        """
        Удалить продукт
        :param name: название удаляемого продукта
        """
        self.check_parametrs(name)  # указываются проверяемые параметры
        if name in self.__products:
            self.__products.pop(name)
        else:
            print(f"Продукта {name} не существует в БД.")


if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_product(name='Яблоки', quantity=50, price=10)  # создание продукта, установка кол-ва и цены
    inventory.update_product_quantity(name='Яблоки', quantity=100)  # обновление кол-ва продуктов
    print(inventory.get_product_info(name='Яблоки'))  # получение информации о продукте
    inventory.add_product(name='Апельсины', quantity=30, price=5)
    inventory.remove_product(name='Апельсины')  # удаление продукта
    print(inventory.products)
    # получение стоимости всех товаров в БД
    all_price = inventory.total_value()
    print(all_price)
