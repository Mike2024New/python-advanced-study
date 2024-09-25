"""
Обработка исключений, конструкция try/except/finally/else.
Для того, чтобы гарантировать выполнение блока кода, используется обрбаботка исключений:
1).запускается блок try - попробовать, то есть выполнить требуемые действия,
2?).если возникнет ошибка, то код переместится в блок except, в этой точке можно отловить конкретные исключения,
например TypeError (неверый тип данных), можно также написать свои кастомные исключения и отлавливать их, в самом конце
ставится отлов исключений общего типа (для непредвиденных исключений), задача исключений прервать выполнение кода в
случае возникновения ошибок или обработки этих ошибок и продолжения кода.
3).finally - этот блок отработает в любом случае независимо от того будет выброшено исключение или блок try выполнится
корректно.
4).else - выполнится только в случае успешного срабатывания блока try

--------------------------------------
* Знак вопроса в пункте 2 обозначает, что этот блок не обязательно отработает, то есть если код в блоке try выполнится
без ошибок то блок except вызван не будет
"""


def example1():
    def devider(a, b):
        if not all(isinstance(i, (int, float)) for i in (a, b)):
            raise TypeError(f"Ошибка аргументов a={a} b={b},на вход принимаются int или float")
        if b == 0:
            raise ZeroDivisionError(f"Ошибка делить на 0 могут только монахи математики 6 дана с чёрным поясом")
        try:
            return a / b
        except Exception as err:
            raise Exception(f"Возникла непредвиденная ошибка при делении a={a}/b={b} -> {err}")

    print(devider(6, 2))  # output: 3.0 OK
    print(devider(6, 2.5))  # output: 2.4 OK
    print(devider(6, '10'))  # ValueError ошибка типов
    print(devider(6, 0))  # ZeroDivisionError ошибка деления на 0


def example2():
    def save(value):
        print(f"Значение '{value}' сохранено")

    def show_dict(view_dict):
        try:
            new_value = view_dict['test']
        # отслеживание неправильных типов данных
        except TypeError:
            raise TypeError(f"не верный тип данных")
        # отслеживание отсутстсвия нужного ключа
        except KeyError:  # возбудить исключение отсутствия ключа
            raise KeyError(f"не найден ключ")
        except Exception as err:  # если не одно исключение ранее не отработало то вызвать общее исключение
            raise Exception(f"Возникла не известная ошибка {err}")
        else:
            save(value=new_value)
        finally:
            print(f"Обработка '{view_dict}' завершена.")

    show_dict(view_dict={"test": 123})  # ОК
    # show_dict(view_dict=[])  # valueError
    # show_dict(view_dict={"key": 123}) # keyError -> так как отсутствует ключ test


def example3():
    """пример обработки исключенией при попытке прочитать файл"""

    def read_file(file_path, select_mode='r', encode='utf-8'):
        try:
            with open(file_path, mode=select_mode, encoding=encode) as file:
                return file.read()
        except UnicodeError:
            raise UnicodeError(f"Ошибка кодировки при чтении файла {file_path}")
        except ValueError:
            raise ValueError(f"Ошибка не правильно выбран режим чтения {select_mode}")
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл не найден '{file_path}'")
        except LookupError:
            raise LookupError(f"Ошибка не найдействителен ключ кодировки '{encode}'")
        except Exception as err:
            raise Exception(f"Возникла непредвиденная ошибка {err}")

    # print(read_file(file_path='descriptions.txt'))  # это корректно отработает так как файл по указанному пути есть
    # print(read_file(file_path='test.txt'))  # FileNotFoundError так как такого файла не существует
    # print(read_file(file_path='descriptions.txt', encode='utf-16'))  # UnicodeError ошибка кодировки
    # print(read_file(file_path='descriptions.txt', encode='####'))  # LookupError ошибка искомого ключа кодировки
    print(read_file(file_path='descriptions.txt', select_mode='xx', encode='utf-8'))  # ValueError


if __name__ == '__main__':
    example1()
