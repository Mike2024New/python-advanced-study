def find_missing_element(collection: list | tuple | set) -> int | str:
    """
    поиск недостающего в коллекции элемента работает только для чисел или для строк
    :param collection: проверяемая коллекция (данные в коллекции должны быть одного типа)
    :return: int/str или None если нет потерявшихся элементов
    """

    def find_missing_number(input_list: list | tuple) -> int:
        """
        Поиск недостающего в коллекции элемента (подходит только для чисел), находит только 1 отсутствующий
        элемент.
        :param input_list: коллекция чисел -> list | tuple
        :return: int/str (недостающий элемент)
        """
        min_element = min(input_list)  # начало диапазона
        max_element = max(input_list)  # конец диапазона
        diapason = range(min_element, max_element)  # проверяемый диапазон
        for num in diapason:
            if num not in input_list:
                return num

    def find_missing_letter(input_list: list | tuple) -> str:
        """
        поиск недостающего элемента буквы
        :param input_list: проверяемая коллекция
        :return: True/False
        """
        min_element = min(map(ord, input_list))  # начало диапазона
        max_element = max(map(ord, input_list))  # конец диапазона
        diapason = range(min_element, max_element)  # проверяемый диапазон
        for letter in diapason:
            if chr(letter) not in input_list:
                return chr(letter)

    if not isinstance(collection, (list, tuple, set)):
        raise TypeError("На вход принимаются только коллекции list, tuple, set")

    # Определение того какую функцию вызвать
    if all(isinstance(element, int) for element in collection):
        return find_missing_number(input_list=collection)
    elif all(isinstance(element, str) for element in collection):
        return find_missing_letter(input_list=collection)
    else:
        raise ValueError("В коллекции должны быть одинаковые типы данных")


if __name__ == '__main__':
    # print(find_missing_element(collection=[3, 7, 1, 2, 8, 4, 5]))  # output: 6
    print(find_missing_element(collection=[1, 4, 3, 2]))  # output: 6
    # print(find_missing_element(collection=[100, 103, 102])) # output: 101
    # print(find_missing_element(collection=['a', 'd', 'b'])) # output: c
    # print(find_missing_element(collection={'a', 'b', 'd'}))  # output: c
    # print(find_missing_element(collection=3)) # TypeError
    # print(find_missing_element(collection=['a', 1]))  # ValueError
