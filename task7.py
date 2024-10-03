def valid_parametr_for_fibonacci(func):
    def inner(x):
        if not isinstance(x, int):
            raise TypeError(f"на вход принимается только число, а введено {x}")

        if any(x == i for i in (0, 1)):  # простой случай, выйти не запуская
            return x

        if x < 0:
            raise ValueError(f"индекс 'x' не может быть меньше 0, а введен {x}")

        if x == 2:  # простой случай вернуть 1
            return 1
        return func(x)

    return inner


@valid_parametr_for_fibonacci
def fibonnacci1(x: int) -> int:
    """
    (задача от Perplexity) -> моё решение
    получить число Фибоначчи по индексу
    :param x: индекс
    :return: результат
    """
    fib_sequence = [0, 1]  # расчёт для простых случаев когда индексы равны 1 и 2
    i = 2  # стартовать с индекса 2
    while i < x + 1:
        add = (fib_sequence[i - 1]) + (fib_sequence[i - 2])
        fib_sequence.append(add)
        i += 1

    return fib_sequence[-1]


@valid_parametr_for_fibonacci
def fibonnacci2(x: int):
    """
    решение подсмотренное, более улучшенное с точки зрения производительности,
    для вычисления не нужно использовать весь список, а нужны лишь 2 последних элемента
    :param x: индекс числа
    :return:
    """
    a, b = 0, 1
    for _ in range(2, x + 1):
        a, b = b, a + b  # то есть сложение двух последних чисел
    return b


if __name__ == '__main__':
    print(fibonnacci2(x=6))
