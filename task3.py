from helpers import time_measure


def example1():
    """
    задача на анограммы от perplexiti,
    решение базируется на сортировке передаваемых строк, так чтобы обе проверяемые строки были отсортированы
    таким образом их уже можно сравнить и вернуть True/False в зависимости от результата
    """

    # @time_measure # декоратор для замера времени выполнения функции на примере больших анаграмм
    def is_anagram(string1: str, string2: str) -> bool:
        """
        Проверка двух строк (может быть расширена и до приёма коллекций)
        :param string1: строка1
        :param string2: строка2
        :return: True/False
        """
        if not all(isinstance(string, str) for string in (string1, string2)):
            raise TypeError('На вход принимается только строка')
        return sorted(string1) == sorted(string2)

    # запуск:
    # Тестовый запуск функции и замер времени (декоратор @time_measure) output: True (2.5 секунд)
    # print(is_anagram(string1=f"test{'*' * 100000000}@123", string2=f"test{'*' * 100000000}@456"))
    print(is_anagram(string1='listen', string2='silent'))  # output: True
    # print(is_anagram(string1=[1, 2], string2=[3, 1]))


"""задача от Perplexity, проверка анаграм (решение без сортировок)"""


def are_anagrams(string1: str, string2: str, ignor_register=False, ignor_space=False) -> bool:
    """
    решение через подсчет элементов в коллекции и сравнение через множества (еще один способ)
    можно также для того, чтобы достичь времени работы O(n) использовать Counter модуля Collections
    :param string1: строка 1
    :param string2: строка 2
    :param ignor_register: учитывать регистер
    :param ignor_space: игнорировать пробелы (удалить все пробелы в строке)
    :return: True/False
    """
    if not all(isinstance(string, str) for string in (string1, string2)):
        raise TypeError("на вход принимаются только строки")
    if ignor_register:
        string1 = string1.lower()
        string2 = string2.lower()
    if ignor_space:
        string1 = string1.replace(' ', '')
        string2 = string2.replace(' ', '')
    set_a = {(litter, string1.count(litter)) for litter in string1}
    set_b = {(litter, string1.count(litter)) for litter in string2}
    return set_a == set_b


if __name__ == '__main__':
    print(are_anagrams(string1='listen', string2='silent'))  # output: True
    print(are_anagrams(string1='listen', string2='Silent'))  # output: False
    print(are_anagrams(string1='listen', string2='Silent', ignor_register=True))  # output: True

if __name__ == '__main__':
    example1()
