from functools import partial, reduce


# генераторы
def example1():
    """Повторение объекта генераторы ->
    генератор это функция которая порционно выдаёт данные по мере необходимости, что обеспечивает, что в единицу
    времени в памяти ПК находится только порция данных заданного размера. Генератор является одноразовым итерируемым
    объектом, на каждую итерацию предыдущие значения стираются из памяти, а те которые впереди ещё не загружены в
    память.
    Ключевое слово yeld позволяет замораживать текущее состояние генератора (то есть переменных указывающих на индексы
    текущих курсоров данных (в примере ниже это переменная i, которая будет обновляться на каждую итерацию и генератор
    yeld помнит это).
    Генератор позволяет обходить большие коллекции данных, например чтение базы данных в которой 2000000000 строк, такой
    объем нельзя будет загрузить в память приложения, но можно загружать его последовательно небольшими порциями
    например по 1000 строк (можно также для этой цели использовать асинхронность, что ускорит обработку).
    По сути база данных это огромная кастрюля, а генератор это половник которая перечерпывает данные из одной кастрюли в
    другую или разливает их по тарелкам.
    """

    def test(chunk_size: int):
        test_collect = [i for i in range(20)]  # некая коллекция с данными
        i = 0
        while i < len(test_collect):
            yield test_collect[i:i + chunk_size]  # получение небольшого куска данных из коллекции и выдача его
            i += chunk_size  # переход на следующую порцию

    result = test(chunk_size=5)
    for indx, value in enumerate(result):
        print(f"iteration:{indx} value: {value}")


# filter
def example2():
    """Функция filter - нужна для фильтрации объектов в последовательности, те объекты которые соответствуют
    функции условию будут возвращены в новую коллекцию. Другими словами берем на вход коллекцию (можно и генераторы)
    последовательно применяем к каждому элементу функцию-проверку условие, те элементы которые соответствуют возвращаем
    в новую коллекцию.
    Важно функция которая выступает в роли фильтра должна возвращать булево значение True / False.
    По умолчанию функция filter возвращает объект generator см. example1
    """

    def is_divided_by_num(x, div):
        return x % div == 0

    is_divided_by_2 = partial(is_divided_by_num, div=2)  # комбинация темы filter и partial (предустановить 2)

    collection = [4, 3, 2, 8, 2]
    result = list(filter(is_divided_by_2, collection))
    print(result)


# filter
def example3():
    """если в filter вместо функции передать None, то она вернет все непустые значения коллекции"""
    collect = ['0', 0, False, True, None, "", [], [[]]]
    result = list(filter(None, collect))
    print(result)


# map
def example4():
    """map - подобно функции filter позволяет применять функцию ко всем элементам коллекции, простейший пример
    использования функции map это приведение типов. map также по умолчанию возвращает генератор
    """

    def string_to_int_or_float(element):
        if not any(isinstance(element, i) for i in (int, str, float)):
            return element
        try:
            return int(element)
        except ValueError:
            try:
                return float(element)
            except Exception as err:
                print(f"Ошибка обработки значения {element} -> {err}")
                return element

    collect = ['fd', '1', 3, '2.5', []]
    # collect = ['2.5', 2, '4', ]
    result = list(map(string_to_int_or_float, collect))
    # result = list(map(int, collect)) # можно было бы и напрямую использ int, но поймаем исключение ValueError
    print(result)


# map
def example5():
    """
    Eщё один пример использования функции map: на этот раз функция применяется к вложенным словарям списка
    """

    def apply_discount(element, percent):
        """
        скидка на товар
        :param element: коллекция типа {...,"price":1000,...} (обязательно должен быть ключ price
        :param percent: процент применяемой скидки
        :return: исходная коллекция с измененным прайсом (с примененной скидкой)
        """
        if not any(isinstance(element["price"], i) for i in (int, float)):
            return element
        element["price"] = element["price"] - (element["price"] / 100) * percent
        return element

    price_discount_5 = partial(apply_discount, percent=5)

    collect = [
        {"model": "Nokia 3310", "price": 3000},
        {"model": "Siemens A60", "price": 1500},
        {"model": "Nokia N95", "price": 10000},
    ]
    result = list(map(price_discount_5, collect))
    print(result)


# zip
def example6():
    """функция zip -> сводит несколько коллекций в одну поиндексно (все индексы коллекции запираются в кортежи),
    возвращает итерируемый объект zip"""
    figures = ['rectangle', 'squart', 'circle']  # например эта коллекция получена из одного источника
    colors = ['red', 'green', 'black']  # эта коллекция получена из другого источника

    result = zip(figures, colors)  # нужно объединить эти две коллекции
    [print(row) for row in result]


# zip
def example7():
    """если коллекции разные по длине, то суммарная длина коллекции будет по длине самой короткой коллекции"""
    figures = ['rectangle', 'squart', 'circle']  # например эта коллекция получена из одного источника
    colors = ['red', 'green', ]  # эта коллекция получена из другого источника
    result = zip(figures, colors)  # длина этой коллекции будет из 2 элементов, так как len(colors)=2
    [print(row) for row in result]


# zip
def example8():
    from itertools import zip_longest
    """
    если нужно чтобы длинна суммарной коллекции не зависила от длины отдельных списков, то можно использовать функцию
    zip_longest модуля itertools, указав в ней значение fillvalue для заполнения пустых элементов, тогда не достающие
    элементы короткой коллекции будут заполненны этими значениями и вся суммарная длина коллекции будет равна наиболее
    длинной входной коллекции.
    """
    figures = ['rectangle', 'squart', 'circle']  # например эта коллекция получена из одного источника
    colors = ['red', 'green', ]  # эта коллекция получена из другого источника
    result = zip_longest(figures, colors, fillvalue='white')
    [print(row) for row in result]


# zip
def example9():
    """для того, чтобы распаковать элементы из коллекции нужно использовать оператор распаковки *"""
    collect = [('rectangle', 'red'), ('squart', 'green')]
    figures, colors = zip(*collect)
    for indx, value in enumerate(figures):
        print(f"figures : {figures[indx]} | colors : {colors[indx]}")


# zip
def example10():
    """zip можно применять и для создания словарей функция dict может перевести список кортежей в словарь, важное
    условие, чтобы в этих кортежах было 2 элемента, пример: [('key1','val1'),('key2','val2')] """
    keys = ['key1', 'key2', 'key3']
    values = ['val1', 'val2', 'val3']
    new_dict = dict(zip(keys, values))
    print(new_dict)


# enumerate
def example11():
    """функция enumerate - служит для итерации по элементам, выдаёт значение текущей итерации и индекс, индексы
    можно смещать относительно нулевой позиции (но это влияет только на номер индекса). Она по сути является
    альтернативой функции range при итерации коллекций и также обеспечивает доступ к текущему индексу итерации"""
    collect = ['a', 'b', 'b', 'd']
    """в примере ниже в enumerate стартовая точка отображения индексов 1"""
    for indx, val in enumerate(collect, start=1):
        print(f"{indx} -> {val}")


# reduce
def example12():
    """функция reduce модуля functools, сводит все элементы коллекции в одно значение основываясь на логике переданной
    в неё функции"""
    collect = [4, 3, 10, 3]
    max_value = reduce(lambda x, y: x if x > y else y, collect)  # найти наибольший элемент
    min_value = reduce(lambda x, y: x if x < y else y, collect)  # найти наименьший элемент
    sum_value = reduce(lambda x, y: x + y, collect)  # найти сумму всех элементов
    print(max_value)  # output: 10
    print(min_value)  # output: 3
    print(sum_value)  # output: 20


# reduce
def example13():
    """функция reduce может также оперировать и с более сложными структурами данных, в данном примере, есть некая
    тестовая коллекция с товарами изделий, и здесь функция reduce будет подсчитывать общую сумм прайса цены всех изделий
    для чего будет использоваться третий аргумент функции reduce как накопитель, и аргумент acc внутри самой lambda
    функции который будет брать значение из внешнего накопителя
    """
    collect = [
        {"model": "Nokia 3310", "price": 3000},
        {"model": "Siemens A60", "price": 1500},
        {"model": "Nokia N95", "price": 10000},
    ]
    """в примере отправной точкой аргумента initial указана цена 100000 к ней будут добавляться остальные цены"""
    result = reduce(lambda acc, product: acc + product['price'], collect, 10000)
    print(result)


# partial
def example14():
    """partial (модуль functools) - инструмент для передачи части аргументов в существующую функцию и предопределения
    аргументов этой функции, то есть она создаёт объект, благодаря которому можно будет вызвать функцию с
    предустановленными параметрами, при этом сама функция остаётся также доступной напрямую.

    В этом примере приведен класс, чтобы было понятно, что работа partial может вестись и с экземлярами класса.
    """

    class Product:
        def __init__(self, name, price, count):
            self.name = name
            self.price = price
            self.count = count

        def get_price_discount(self, percent):
            price = self.price - (self.price / 100) * percent
            return f"Товар: {self.name} Цена: {price} Осталось на складе: {self.count}"

    product = Product(name='Siemens M55', price=3000, count=10)

    product_discount_5 = partial(product.get_price_discount, percent=5)  # предустановка значения скидки 5 %
    product_discount_10 = partial(product.get_price_discount, percent=10)  # предустановка значения скидки 5 %

    print(product_discount_5())  # использование функции get_price_discount через предопределенный фильтр 5%
    print(product_discount_10())  # использование функции get_price_discount через предопределенный фильтр 10%
    print(product.get_price_discount(percent=20))  # прямое обращение к функции get_price_discount


if __name__ == '__main__':
    example14()
