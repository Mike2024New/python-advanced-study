"""функция map - даёт возможность применить функцию ко всем элементам находящимся внутри коллекции, по умолчанию
возвращает генератор (см уроки lesson1 и lesson2)
"""


def example1():
    """
    Допустим есть некоторый список цен и нужно эти цены пересчитать с учётом НДС, map позволяет применить функцию с НДС
    ко всем элементам коллекции не прибегая к отдельному циклу
    """
    nds = 1.2  # ставка НДС применяемая к товарам из price
    prices = [  # имитация БД товаров с ценами
        {"product": "Nokia 3310", "price": 3500, },
        {"product": "Siemens M55", "price": 6000, },
        {"product": "Nokia N95", "price": 10000, },
    ]
    prices_nds = map(lambda x: {"product": x["product"], "price": int(x['price'] * nds)}, prices)
    try:
        print(next(prices_nds))
        print(next(prices_nds))
        print(next(prices_nds))
        print(next(prices_nds))
        print(next(prices_nds))  # в этой точке возникнет исключение StopIteration
    except Exception as err:
        print(f"Все данные просмотрены. {err}")


def example2():
    """
    ещё один пример использования функции map это приведение типов данных, например по api пришли данные с номерами
    в виде строк, нужно преобразовать их в int, чтобы не писать отдельный цикл целесообразнее будет использовать
    map
    """
    numbers = ['100', '50', '10', '1']
    numbers_int = list(map(int, numbers))
    print(numbers_int)


if __name__ == '__main__':
    example2()
