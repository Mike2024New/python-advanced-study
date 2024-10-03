"""
задача из финансового журнала, накопление денег путём откладывания такого кол-ва, какой день сегодня
"""


def validate_parametrs_summ_days(func):
    """
    Проверка значения введенного в summ_days
    :param func: номер дня
    :return:
    """

    def wrapper(days: int):
        if not isinstance(days, int):
            raise TypeError("Количество дней должно быть указано целым числом")

        if days > 1:
            return func(days)
        raise ValueError(f"Количество дней должно быть в диапазоне от 1 до + бесконечности а введено {days}")

    return wrapper


@validate_parametrs_summ_days
def summ_days(days: int) -> int:
    """
    накопления мини-игра. Суть: каждый день откладывать столько рублей какой по счёту сегодня день
    сумма за 1 год будет равна 66 795 руб.
    :param days: день сумму в котором нужно увидеть
    :return: сумма
    """
    summ = 0
    previous = 0  # сумма за предыдущий день
    for i in range(days + 1):
        summ += previous
        previous = i  # сохранение суммы за предыдущий день
    return summ + previous


if __name__ == '__main__':
    day = 1460
    res = summ_days(days=day)
    print(f"На {day} день, отложено {res} руб., сегодня нужно отложить {day} руб.")
