from functools import reduce

"""
Функция reduce из модуля functools применяется для последовательного применения функции к элементам коллекции (например,
списку) с целью свести его к одному значению. Это достигается путем применения функции к первым двум элементам, затем 
к результату и следующему элементу, и так далее.
Если добавить третий аргумент в функцию reduce, то он будет работать как накопитель (аккумулятор значений предыдущих
элементов) см. example3.
"""


def example1():
    """использование функции reduce для получения суммы элементов коллекции"""
    collect = [1, 2, 5]  # входная коллекция
    result = reduce(lambda x, y: x + y, collect)  # reduce просуммирует элементы
    print(result)


def example2():
    """пример использования reduce для поиска минимального и максимального значения коллекции"""
    collect = [3, 1, 0, 6]
    min_value = reduce(lambda x, y: x if x < y else y, collect)
    max_value = reduce(lambda x, y: x if x > y else y, collect)
    print(f"min_value:{min_value}\nmax_value:{max_value}")


def example3():
    """пример использования функции reduce с 3 элементом, накопителем значений"""
    prices = [  # имитация БД товаров с ценами
        {"product": "Nokia 3310", "price": 3500, },
        {"product": "Siemens M55", "price": 6000, },
        {"product": "Nokia N95", "price": 10000, },
    ]
    # Используем reduce для суммирования цен
    # previous - это результат сложения предыдущих элементов (сюда будет добавляться значение из 3 аргумента reduce)
    # 0 - это начальное значение для аккумулятора (обновляемое на каждую итерацию значение)
    summ_price = reduce(lambda previous, product: previous + product['price'], prices, 0)
    print(summ_price)


if __name__ == '__main__':
    example3()
