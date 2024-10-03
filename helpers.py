from functools import wraps
from time import monotonic


def time_measure(func):
    """замер времени работы функций"""
    start_time = monotonic()  # стартовое время запуска функции

    @wraps(func)  # Сохраняем метаданные оригинальной функции
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        end_time = round(monotonic() - start_time, 2)
        print(f"времени прошло {end_time} секунд.")

    return inner
