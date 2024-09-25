"""
Декораторы - обёртка функции, внешней функцией которая позволяет выполнять дополнительные действия перед (или после)
срабатывания передаваемой в декоратор (обёртку) функции. По сути декоратор является модификацией переданной в него, без
изменения кода передаваемой функции. Декораторов к функции может быть несколько, их порядок значения не имеет (если это
не обусловлено логикой приложения).

декоратор wraps модуля functools -> позволяет сохранить имя переданной функции (так как по умолчанию декораторы изменяют
названия объектов генерируя новые имена).
"""
from time import monotonic, sleep
from functools import wraps


def example1():
    """
    краткое объяснение концепции декораторов, есть некая пользовательская функция test_func, по умолчанию она
    печатает 'run test_func', но если на неё навесить декоратор outer_func, то он выполнит некоторую свою логику до
    срабатывания функции test_func и после (в данном случае это просто печать сообщений).
    """

    def outer_func(func):
        @wraps(func)  # Сохраняем метаданные оригинальной функции
        def inner_func(*args, **kwargs):
            print("start func")  # это действие будет выполнено перед функцией func
            func(*args, **kwargs)  # выполнение переданной в декоратор функции
            print("finish func")  # это действие будет выполнено перед функцией func

        return inner_func

    @outer_func
    def test_func():
        print("\trun test_func")

    test_func()


def example2():
    """пример функции обёртки для замера времени выполнения кода"""

    def time_measure(func):
        start_time = monotonic()  # стартовое время запуска функции

        @wraps(func)  # Сохраняем метаданные оригинальной функции
        def inner(*args, **kwargs):
            func(*args, **kwargs)
            end_time = monotonic() - start_time
            print(f"времени прошло {end_time} секунд.")

        return inner

    @time_measure
    def test_func():
        """функция имитирует продолжительную работу"""
        sleep(3.2)

    test_func()


def example3():
    """
    Пример комбинации из нескольких декораторов
    пример передачи параметров в декоратор
    """

    def time_measure(func):
        start_time = monotonic()  # стартовое время запуска функции

        @wraps(func)  # Сохраняем метаданные оригинальной функции
        def inner(*args, **kwargs):
            func(*args, **kwargs)
            end_time = round(monotonic() - start_time, 2)
            print(f"времени прошло {end_time} секунд.")

        return inner

    def mark_function(char_fill='=', len_fill=50, *args_tracking, **kwargs_tracking):
        def external(func):
            nonlocal len_fill
            # вычисление равномерных отступов от заголовков вначале и в конце строки
            len_fill = len_fill - 2  # удалить пробелы в выводе
            fill_start = (int((len_fill - len(func.__name__)) / 2) * char_fill)
            fill_end = (int((len_fill - len(f"END {func.__name__}")) / 2) * char_fill)

            @wraps(func)  # Сохраняем метаданные оригинальной функции
            def inner(*args, **kwargs):
                print(f"\n{fill_start} {func.__name__} {fill_start}")
                # вывод отслеживаемых аргументов
                print(f"args_tracking: {args_tracking}")
                print(f"kwargs_tracking: {kwargs_tracking}\n{'-' * 40}\n")
                func(*args, **kwargs)
                print(f"\n{fill_end} END {func.__name__} {fill_end}")

            return inner

        return external

    x = 100
    y = 200

    # навешивание нескольких декораторов
    @mark_function(char_fill='+', len_fill=100, x=x, y=y)
    @time_measure
    def test_func(msg):
        nonlocal x
        sleep(0.1)
        x = 55
        print(msg)

    test_func(msg='run test func')


if __name__ == '__main__':
    example3()
