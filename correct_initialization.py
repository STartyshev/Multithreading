import random


def input_correct_num(left_value, right_value, input_message, error_message, type_of_number):
    """
    Функция реализующая ввод пользователем корректного числа входящего в заданный диапазон.
    :param left_value: Левая граница диапазона;
    :param right_value: правая граница диапазона;
    :param input_message: сообщение-приглашение на ввод числа;
    :param error_message: сообщение в случае не корректного ввода;
    :param type_of_number: тип числа, которое нужно вводить пользователю.
    :return: Возвращает корректное число введенное пользователем.
    """
    while True:
        while True:
            try:
                num = type_of_number(input(input_message))
                break
            except ValueError:
                print('Введенное значение должно являться числом! '
                      'Попробуйте еще раз.')

        if num < left_value or num > right_value:
            print(error_message)
        else:
            return num


def ui_array_init(array):
    """
    Функция для инициализации массива числами вручную.
    :param array: Массив для инициализации.
    """
    while True:
        elem_or_exit = input('Введите число, которое хотите добавить в массив (для выхода введите - выход): ')
        if elem_or_exit.upper() == 'ВЫХОД':
            return
        else:
            try:
                elem_or_exit = float(elem_or_exit)
                array.append(elem_or_exit)
            except ValueError:
                print('Введенное значение не является числом или ключевым словом "выход". '
                      'Попробуйте еще раз.')


def auto_array_init(array):
    """
    Функция для инициализации массива случайными числами.
    :param array: Массив для инициализации.
    """
    n = random.randint(1, 50)
    for i in range(n):
        array.append(round(random.random() * 10 * ((-1) ** random.randint(1, 2)), 1))


def ui_array_of_dots_init(array_of_dots):
    """
    Функция реализующая пользовательский интерфейс в консоли для инициализации массива точек вручную.
    :param array_of_dots: Массив точек для инициализации.
    """
    print('В каком пространстве будут находиться точки?\n'
          '1. На прямой.\n'
          '2. На плоскости.\n'
          '3. В трехмерном пространстве.')

    space_selection = input_correct_num(
        left_value=-float('inf'),
        right_value=float('inf'),
        input_message='Выберите пункт меню: ',
        error_message='В меню всего 3 пункта. Попробуйте еще раз.',
        type_of_number=int
    )
    while True:
        point_coordinates = []
        for i in range(space_selection):
            point_coordinates.append(
                input_correct_num(
                    left_value=-float('inf'),
                    right_value=float('inf'),
                    input_message=f"Введите {i + 1}-ю координату {len(array_of_dots) + 1}-й точки: ",
                    error_message='Координата должна быть числом. Попробуйте еще раз.',
                    type_of_number=float
                )
            )
        array_of_dots.append(tuple(point_coordinates))
        add_or_exit = input('Хотите добавить еще одну точку? Да / Нет: ')
        add_or_exit = add_or_exit.upper()
        while add_or_exit != 'ДА' and add_or_exit != 'НЕТ':
            print('Есть только два варианта ответа. '
                  'Попробуйте еще раз.')
            add_or_exit = input('Хотите добавить еще одну точку? Да / Нет: ')
            add_or_exit = add_or_exit.upper()

        if add_or_exit == 'НЕТ':
            return


def ui_auto_array_of_dots_init(array_of_dots, space_selection):
    """
    Функция реализующая пользовательский интерфейс в консоли для инициализации массива случайными точками.
    :param array_of_dots: Массив точек для инициализации;
    :param space_selection: размерность пространства в котором будут находиться точки.
    """
    size_of_array = random.randint(1, 50)

    for i in range(size_of_array):
        array_of_dots.append(
            tuple(
                round(random.random() * 10 * ((-1) ** random.randint(1, 2)), 1) for j in range(space_selection)
            )
        )
