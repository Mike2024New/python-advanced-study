"""
замыкания это функции которые позволяют сохранять свое окружение даже в тот момент когда они не используются.
То есть переменные внутри декоратора как бы закрепляются за функцией, достигается это за счёт того, что внешняя
функция возвращает объект функции а не вызов самой функции.
То есть замыкание создаёт внутри себя некую самостоятельную область видимости, которая запоминает состояние
переменных внутри себя.
"""


def example1():
    """
    пример использования замыкания, переданный в outer_function аргумент сохранится внутри объекта inner_function
    который вернет outer_function
    реализация этого примера похожа на partial
    """

    def outer_function(x):
        def inner_function(y):
            return x + y

        return inner_function  # вернуть объект функции (без её вызова)

    closure = outer_function(10)  # значение 10 "запечется" внутри замыкания
    print(closure(5))  # Вывод: 15
    print(closure(3))  # Вывод: 13


def example2():
    """
    функция partial модуля functools может быть реализована на замыкании?
    Чтобы лучше понять этот пример см. lesson9 -> там подробно объясняется работа функции partial модуля functools
    """

    # определение 1 пользовательской функции считает степерь числа
    def power(base, exponent):
        return base ** exponent

    # определение 2 пользовательской функции считает ставку НДС к сумме
    def apply_nds(summa, bet):
        return summa - (summa / 100) * bet

    def partial(func: callable, **kwargs) -> callable:
        """замыкание которое принимает на вход пользовательскую функцию и позволяет предустановить часть параметров"""

        def inner_function(*args, **kwargs2):
            return func(*args, **kwargs, **kwargs2)

        return inner_function  # вернуть объект функции (без её вызова)

    pow_square = partial(func=power, exponent=2)  # предустановка пользовательских параметров функции power
    pow_cube = partial(func=power, exponent=3)  # предустановка пользовательских параметров функции power

    # действие с предустановленными параметрами функции power
    res_square = pow_square(6)
    res_cube = pow_cube(base=3)
    print(res_square)
    print(res_cube)

    apply_nds_18 = partial(func=apply_nds, bet=18)  # предустановка пользовательских параметров функции apply_nds
    apply_nds_20 = partial(func=apply_nds, bet=20)  # предустановка пользовательских параметров функции apply_nds
    # действие с предустановленными параметрами функции apply_news
    res_nds_18 = apply_nds_18(summa=1000)
    res_nds_20 = apply_nds_20(summa=1000)
    print(res_nds_18)
    print(res_nds_20)


def example3():
    """
    пример использования замыкания в качестве счётчика
    возвращаемый объект inner_function будет хранить состояние всех переданных в неё и объявленных в ней переменных
    (на момент объявления объекта counter())
    """

    def counter(start=0):
        count = start  # исходное значение счётчика

        def inner_function():
            nonlocal count  # указать что count берется из пространства имён функции counter (на 1 уровень выше текущ)
            count += 1  # изменение функции на каждый вызов
            return count  # эта часть хранит текущее значение счётчика

        return inner_function

    user1 = counter(start=10)
    print(user1())
    print(user1())
    print(user1())


def example4():
    """пример управления счётчиком внутри функции"""

    def create_summator(start=0):
        a = start  # исходная сумма (можно и не с 0)

        def inner(b):
            nonlocal a  # взять a из внешней области видимости
            if b == 0:
                """обнуление счётчика"""
                a = 0
                return a

            a += b  # действие над a (a будет перезаписана в окружении inner)
            return a

        return inner

    summator = create_summator()
    print(summator(5))  # увеличение счётчика / output 5
    print(summator(0))  # обнуление счётчика / output 0
    print(summator(-3))  # уменьшение счётчика  / output -3
    print(summator(5))  # увеличение счётчика / output 2


if __name__ == '__main__':
    example4()
