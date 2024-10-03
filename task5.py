"""
Задача от Perplexity
найти в коллекции второй по величине элемент, сортировки использовать запрещено
Флаг reverse позволяет определить удалить второй по величине элемент относительно наименьшего или относительно
наибольшего, вот пример:
[3,4,6,7,1] (с reverse=False) -> второй по величине 6
[3,4,6,7,1] (с reverse=True) -> второй по величине 3
---------------------------------------------------
Решение:
1) нужно удалить первый по величине аргумент из списка (например [3,2,4,5]) удалить 5, остаётся коллекция [3,2,4]
2) вернуть первый по величине аргумент из оставшейся коллекции [3,2,4] -> 4
==> второй по величине аргумент 5
---------------------------------------------------
два плюс два равно три будет четыре (шутка🙂)
"""


def second_largest(collection: list | set | tuple, reverse=False):
    def second_largest_number(input_list: list | set | tuple) -> int:
        """
        поиск второго по величине элемента
        :param input_list: проверяемая коллекция
        :return: int
        """
        del_arg = min(input_list) if reverse else max(input_list)  # найти первый минимальный элемент
        input_list.remove(del_arg)  # удалить этот элемент из списка
        return min(input_list) if reverse else max(input_list)  # вернуть минимальный аргумент

    def second_largest_letter(input_list: list | set | tuple) -> str:
        """
        поиск второго по величине элемента
        :param input_list: проверяемая коллекция
        :return: str
        """
        input_list = [ord(i) for i in set(input_list)]
        del_arg = min(input_list) if reverse else max(input_list)
        input_list.remove(del_arg)
        return chr(min(input_list)) if reverse else chr(max(input_list))

    # проверка типов
    if not isinstance(collection, (list, tuple, set)):
        raise TypeError("На вход принимаются только коллекции list, tuple, set")

    collection = set(collection)  # оставить только уникальные элементы
    # менее 2 уникальных элементов, вернуть None
    if len(collection) < 2:
        return None
    # определение нужной функции (буквы или числа)
    if all(isinstance(element, int) for element in collection):
        return second_largest_number(input_list=collection)
    if all(isinstance(element, str) for element in collection):
        return second_largest_letter(input_list=collection)


if __name__ == '__main__':
    print(second_largest(collection=[4, 3, 2, 10, 4, 5, 8]))  # output: 8
    # print(second_largest(collection=[4, 3, 2, 10, 4, 5, 8], reverse=True))  # output 3
    # print(second_largest(collection=['q', 'w', 'f', 'a', 'b', 'd', 'e']))  # output q
    # print(second_largest(collection=['q', 'w', 'f', 'a', 'b', 'd', 'e'], reverse=True))  # output b
    # print(second_largest(collection=[3, 1]))  # output 1
    # print(second_largest(collection=[3, 1], reverse=True))  # output 3
    # print(second_largest(collection=[5, 5, 5]))  # output None
    # print(second_largest(collection=[5]))  # output None
    # print(second_largest(collection=[]))  # output None
    # print(second_largest(collection=2))  # TypeError
