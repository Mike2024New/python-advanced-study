def unique_elements(input_list: list, ignored_order_elements=False) -> list:
    """
    удаление дублей и возвращение списка с уникальными элементами с соблюдением порядка вхождений элементов
    (можно также проигнорировать порядок элементов указав ignored_order_elements)
    Пример:
    input: [1, 2, 3, 1, 2, 4, 5] -> output: [1, 2, 3, 4, 5]
    --------------------------
    :param input_list:
    :param ignored_order_elements:  игнорировать порядок элементов?
    :return:
    """
    if not isinstance(input_list, list):
        raise TypeError('на вход принимается только список')
    if ignored_order_elements:
        return list(set(input_list))
    output_list = []
    for element in input_list:
        if element not in output_list:
            output_list.append(element)
    return output_list


if __name__ == '__main__':
    print(unique_elements(input_list=[1, 2, 3, 1, 2, 4, 5]))  # output: [1, 2, 3, 4, 5]
    print(unique_elements(input_list=[2, 4, 5], ignored_order_elements=True))  # уникальн элементы в произвольн порядке
