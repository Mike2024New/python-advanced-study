"""
Задача: Анализ расходов
Описание: Напишите функцию, которая принимает список расходов и возвращает информацию о следующих аспектах:
Общая сумма расходов.
Средний расход.
Наибольший расход.
Наименьший расход.
Количество расходов, превышающих средний расход.
Пример:
python
expenses = [150, 200, 50, 300, 450, 100]
result = analyze_expenses(expenses)
print(result)

Ожидаемый вывод:
text
{
    "total": 1250,
    "average": 208.33,
    "max": 450,
    "min": 50,
    "above_average_count": 3
}

Ограничения:
Не используйте встроенные функции для подсчета суммы или среднего (например, sum() или mean() из библиотеки statistics).
Учтите, что список может содержать как положительные, так и отрицательные значения (например, возврат товаров).

Разрешено реализовать решение задачи на ООП
"""


class AnalizeExpenses:
    def __init__(self, expenses: list | tuple | set) -> None:
        self.__expenses = None
        self.__data = {"total": 0, "average": 0, "max": 0, "min": 0, "above_average_count": 0}
        self.started(expenses)  # запуск подсчёта всех данных

    def started(self, expenses: list | tuple | set) -> None:
        """запуск методов анализа расходов"""
        if not isinstance(expenses, (list | tuple | set)):
            raise TypeError(f"На вход принимается только список, множество или кортеж, передано {expenses}")
        if not len(expenses) or len(expenses) == 1:
            raise ValueError("Подсчёт пустого списка или списка из 1 элемента смысла не имеет")
        if not all(isinstance(arg, (int, float)) for arg in expenses):
            raise ValueError(f"Ошибка все аргументы в списке трат должны быть в виде чисел или десятичн дробей.")

        self.__expenses = expenses  # все проверки пройдены установка нового значения
        self.__data['total'] = self._get_total()
        self.__data['average'] = self._get_average()
        self.__data['max'] = self._get_max_or_min(mode='max')
        self.__data['min'] = self._get_max_or_min(mode='min')
        self.__data['above_average_count'] = self._above_average_count()

    def analize_expenses(self):
        """получение статистики о расходах пользователем в виде json"""
        return self.__data

    @property
    def expenses(self):
        return self.__expenses  # посмотреть expenses

    @expenses.setter
    def expenses(self, expenses):
        self.started(expenses)  # перезапустить анализ расходов (при изменении expenses)

    def _get_total(self) -> int | float:
        """получение суммы всех расходов"""
        x = 0
        for i in self.__expenses:
            x += i
        return x

    def _get_average(self) -> int | float:
        """возвращение среднего арифметического трат"""
        return round((self.__data['total'] / len(self.__expenses)), 2)

    def _get_max_or_min(self, mode: str) -> int | float:
        """
        максимальный элемент списка трат
        :param mode: 'min' or 'max' выбрать метод поиск максимального или минимального
        :return: минимальный или максимальный элемент в зависимости от значения mode (min or max)
        """
        value = self.__expenses[0]
        for expense in self.__expenses:
            if mode == 'min':
                value = expense if value > expense else value
            elif mode == 'max':
                value = expense if value < expense else value
        return value

    def _above_average_count(self):
        """
        получение количества расходов превышающих средний расход
        """
        count = 0
        average = self.__data['average']
        for expence in self.__expenses:
            if expence > average:
                count += 1
        return count


if __name__ == '__main__':
    analize = AnalizeExpenses(expenses=[360, 100, - 100, 61])
    print(analize.analize_expenses())
    analize.expenses = [10, 2, 3]
    print(analize.analize_expenses())
