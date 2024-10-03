def task1():
    """задача от perplexity -> проверка строки на палиндром, мои два способа решения"""

    def is_palindrom(inp_string: str) -> bool:
        """
        проверка строки на палиндром
        :param inp_string: входная строка, например "Racecar" -> вернет True
        :return: True/False
        """
        if not isinstance(inp_string, str):
            raise TypeError('На вход принимается только строка')

        # выход если строка из 1 символа или пустая то это случай палиндрома
        if len(inp_string) == 0 or len(inp_string) == 1:
            return True

        inp_string = inp_string.lower()  # перевод всех символов в нижний регистер
        inp_string = inp_string.replace(' ', '')  # удаление пробелов

        def inner_recursion(string: str) -> bool:
            """
            рекурсивный способ решения задачи на палиндром (до 900 итераций)
            :param string: входная строка
            :return: True/False
            """
            if len(string) == 0 or len(string) == 1:
                return True
            if string[0] != string[-1]:  # точка выхода (первый символ не равен последнему) / строка не является палиндр
                return False
            return inner_recursion(string[1:-1])  # на каждую итерацию передаём строку минус первый и последний символ

        def inner(string: str) -> bool:
            """
            способ решения через all кол-во итераций не ограничено
            :param string: входная строка
            :return: True/False
            """
            return all(string[i] == string[(i * -1) - 1] for i in range(len(string)))

        if len(inp_string) < 1800:
            return inner_recursion(string=inp_string)  # запуск через рекурсию
        return inner(string=inp_string)  # запуск через all

    # res = is_palindrom(inp_string=[])  # TypeError
    # res = is_palindrom(inp_string='')  # output: True (рекурсия запущена не будет)
    # res = is_palindrom(inp_string='w')  # output: True (рекурсия запущена не будет)
    res = is_palindrom(inp_string='Racecar')  # output: True (рекурсия запущена не будет)
    # res = is_palindrom(inp_string='A man a plan a canal Panama')  # output: True
    # res = is_palindrom(inp_string='0' * 20000)  # output: True (реш будет через all так как превыш. глубина рекурсии)
    print(res)


def task2():
    """более крутой и короткий способ решения задачи
    способ основан на срезах строк и сравнении реверсивной строки
    """

    def is_palindrom(inp_string: str) -> bool:
        """
        проверка строки на палиндром
        :param inp_string: входная строка, например "Racecar" -> вернет True
        :return: True/False
        """
        if not isinstance(inp_string, str):
            raise TypeError('На вход принимается только строка')

        # выход если строка из 1 символа или пустая то это случай палиндрома
        if len(inp_string) == 0 or len(inp_string) == 1:
            return True

        inp_string = inp_string.lower().replace(' ', '')  # удаление пробелов

        return inp_string == inp_string[::-1]

    # res = is_palindrom(inp_string=[])  # TypeError
    # res = is_palindrom(inp_string='')  # output: True (рекурсия запущена не будет)
    # res = is_palindrom(inp_string='w')  # output: True (рекурсия запущена не будет)
    # res = is_palindrom(inp_string='Racecar')  # output: True (рекурсия запущена не будет)
    res = is_palindrom(inp_string='A man a plan a canal Panama')  # output: True
    # res = is_palindrom(inp_string='0' * 20000)  # output: True (реш будет через all так как превыш. глубина рекурсии)
    print(res)


if __name__ == '__main__':
    task2()
