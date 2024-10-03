def example1():
    """
    пример простого пользовательского исключения, достаточно просто объявить класс наследуемый от базового класса
    Exception, внутреняя логика внутри класса может отсутстсвовать, но это исключение все равно остановит выполнение
    кода.
    """

    class InvalidAgeException(Exception):
        pass

    def check_age(age):
        if age < 18:
            raise InvalidAgeException(f"Возраст {age} лет, не позволяет устроиться на работу.")
        return True

    res = check_age(10)
    print(res)


def example2():
    class SalaryNotInRangeError(Exception):
        def __init__(self, salary, message="ЗП вне допустимого диапазона"):
            self.salary = salary
            self.message = message
            super().__init__(self.message)

    def set_salary(salary):
        if not (5000 <= salary <= 15000):
            raise SalaryNotInRangeError(salary)

    try:
        set_salary(3000)  # Это вызовет исключение
    except SalaryNotInRangeError as e:
        print(f"Ошибка: {e.message}, введено: {e.salary}")


if __name__ == '__main__':
    example2()
