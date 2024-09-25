from functools import partial

"""
partial - это надстройка к функции, которая даёт возможность предустанавливать часть аргументов,
создавая новую функцию, через которую можно будет вызвать исходную функцию с предустановленными аргументами.
При этом основная функция также остаётся доступной. То есть это шаблон с предустановленными аргументами.
"""


def example1():
    def power(base, exponent):
        return base ** exponent

    """предустановим значение exponent для функции power"""
    square = partial(power, exponent=2)  # теперь эта функция всегда будет возводить значение в квадрат
    cube = partial(power, exponent=3)  # теперь эта функция всегда будет возводить значение в куб

    print(square(base=3))  # output: 9
    print(cube(base=3))  # output: 27
    print(power(base=4, exponent=5))  # но также можно обращаться к функции power напрямую задавая произвольн. аргументы


def example2():
    """чуть более практичный пример чем в example1, """

    def apply_nalog(summa, bet):
        return summa - (summa / 100) * bet

    # пользовательская предустановка значений
    summ_nalog_6_percent = partial(apply_nalog, bet=6)  # предустановленное значение для ставки 6%
    summ_nalog_13_percent = partial(apply_nalog, bet=13)  # предустановленное значение для ставки 13%

    print(summ_nalog_6_percent(summa=10000))  # использ. функции apply_nalog с предустановленным значением
    print(summ_nalog_13_percent(summa=10000))  # использ. функции apply_nalog с предустановленным значением
    print(apply_nalog(summa=10000, bet=10))  # использование функции apply_nalog напрямую с произвольным значением


def example3():
    """применение функции partial к экземляру класса"""

    class CalcBudjet:
        @staticmethod
        def apply_nalog(summa, bet):
            return summa - (summa / 100) * bet

    # пользовательская предустановка значений
    summ_nalog_ip = partial(CalcBudjet.apply_nalog, bet=6)
    summ_nalog_simple_man = partial(CalcBudjet.apply_nalog, bet=13)

    print(summ_nalog_ip(summa=10000))
    print(summ_nalog_simple_man(summa=10000))


if __name__ == '__main__':
    example3()
