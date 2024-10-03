def task1():
    """задача от Perplexity -> сортировка коллекций сортировка пузырьком."""

    def sort_collect(collect: list | tuple, increasing: bool = True) -> list | tuple:
        """
        Сортировка коллекции по возврастанию или убыванию в зависимости от increasing
        :param collect: исходная коллекция, например [4,1,2,0,8] или ['w','q','f','q']
        :param increasing: True - сортировка по возрастанию / False - сортировка по убыванию
        :return: отсортированная коллекция, например [1,2,3,4] или [4,3,2,1] в зависимости от increasing

        Принцип:
        collect -> 4,2,1,0,10
        1 такт внешнего цикла (итерации до предпоследнего эл-та):
        |4|,2,1,0,10
        2,|4|,1,0,10
        2,1,|4|,0,10
        2,1,0,|4|,10
        2 такт внешнего цикла:
        1,|2|,0,4,10
        1,0,|2|,4,10
        1,0,2,|4|,10
        ...
        """
        # проверка типов
        if not isinstance(collect, (list, tuple)):
            raise TypeError('Принимаются только списки или кортежи')
        # если коллекция пуста
        if not collect:
            return collect
        # проверка что типы в коллекции сравнимы
        first_type = type(collect[0])
        if not all(isinstance(i, first_type) for i in collect):
            raise TypeError(f'В коллекции "{collect}" присутствуют не сравнимые типы')

        for _ in range(len(collect) - 1):
            print(collect)
            for i in range(len(collect) - 1):
                if increasing:  # сортировка по возрастанию
                    if collect[i] > collect[i + 1]:
                        # поменять элементы местами (больший с меньшим)
                        collect[i], collect[i + 1] = collect[i + 1], collect[i]

                elif not increasing:  # сортировка по убыванию
                    if collect[i] < collect[i + 1]:
                        # поменять элементы местами (меньший с большим)
                        collect[i], collect[i + 1] = collect[i + 1], collect[i]
        return collect

    # res = sort_collect(collect={}) # TypeError
    # res = sort_collect(collect=2)  # TypeError
    # res = sort_collect(collect=[3, 1, 'a', 3])  # TypeError (так как напрямую 1 и 'a' не сравнимы).
    # res = sort_collect(collect=[])  # output: []
    # res = sort_collect(collect=[[10], [5], [3], [0]], increasing=True)  # output: [[0], [3], [5], [10]]
    # res = sort_collect(collect=['c', 'w', 'a', 'b', 'w'], increasing=False)  # output: ['w', 'w', 'c', 'b', 'a']
    res = sort_collect(collect=[4, 2, 1, 0, 10], increasing=True)  # output: [1, 1, 2, 3, 10]
    print(res)


def task2():
    """шейкерная сортировка пузырьком (с 2 сторон) алгоритм более производительный чем в 1 задаче"""

    def sort_collect(collect: list | tuple) -> list | tuple:
        """

        :param collect:
        :return:

        Принцип:
        collect -> 4,2,1,0,10
        1 такт внешнего цикла (итерации до предпоследнего эл-та):
        |4|,2,1,0,10
        2,|4|,1,0,10
        2,1,|4|,0,10
        2,1,0,|4|,10

        2,1,0,|4|,10
        2,0,|1|,4,10
        0,|2|,1,4,10

        """
        for _ in range(len(collect) - 1):
            print(collect)
            for i in range(len(collect) - 1):
                if collect[i] > collect[i + 1]:
                    # поменять элементы местами (больший с меньшим)
                    collect[i], collect[i + 1] = collect[i + 1], collect[i]
        return collect


if __name__ == '__main__':
    task2()
