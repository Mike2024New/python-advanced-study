"""
функция enumerate -> позволяет итерироваться по коллекции выводя значение и индекс. По сути это является альтернативой
функции range при итерации по спискам. Отображаемые индексы можно смещать относительно стартовой позиции (см. example2)
"""


def example1():
    prices = [  # имитация БД товаров с ценами
        {"product": "Nokia 3310", "price": 3500, },
        {"product": "Siemens M55", "price": 6000, },
        {"product": "Nokia N95", "price": 10000, },
    ]

    for indx, value in enumerate(prices):
        if value['product'] == 'Nokia 3310':
            prices[indx]['price'] = 100

    print(prices)


def examle2():
    """
    пример использования функции enumerate но используется второй аргумент который отвечает за смещение отображаемых
    индексов
    """
    collect = ['a', 'b', 'c', 'd']
    for indx, value in enumerate(collect, -2):
        print(f"indx : {indx} | value : {value}")


if __name__ == '__main__':
    examle2()
