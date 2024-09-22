"""
Генератор в python - это такой объект который не хранит все данные в себе сразу а является ленивой функцией, то есть
он будет выдавать значения только по мере необходимости.
Например создадим переменную counter с функцией coutn_up_to(3), это значит, что этот объект counter будет понимать, что
ему нужно выдать 3 результата, но выдавать он их будет только при использовании ключевого слова next (итератора) либо
при итерации в цикле. На каждый next, функция coutn_up_to будет производить новое действие, при этом старые значения
будут затираться.
Проход по генератору возможен только заданное кол-во итераций (то есть его ограничение) после получим ошибку
stop iterration

СМ LESSON2, ЧТОБЫ УВИДЕТЬ ПРАКТИЧЕСКИЙ ПРИМЕР ИСПОЛЬЗОВАНИЯ ГЕНЕРАТОРА
"""


def coutn_up_to(n):
    print(f'инициализация генератора с ограничением в {n} итераций')
    count = 1
    while count <= n:
        print('отработка цикла функции генератора count_up_to')
        yield count
        count += 1


if __name__ == '__main__':
    try:
        counter = coutn_up_to(3)  # эта точка провоцирует инициализацию генератора
        print(next(counter))  # на каждый next происходит вызов count_up_to (то есть обработка данных)
        print(next(counter))
        print(next(counter))
        print(next(counter))  # это вызовет stop iteration (так как мы запрашивали всего три значения в counter)
    except StopIteration:
        print('Все значения были просмотрены')
