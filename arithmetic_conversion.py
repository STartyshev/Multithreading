from correct_initialization import *
import queue
import logging
import threading
import time


# Задача №3
def rq_arithmetic_conversion(client_name, server_name, requests_queue: queue.Queue):
    """
    Функция реализующая перемещенение по меню следующей задачи:
    Требуется проверить можно ли получить число из 3-го массива, арифметическими преобразованиями
    с числами двух других массивов. Числа проверяются последовательно.
    :param client_name: Имя клиента;
    :param server_name: имя сервера;
    :param requests_queue: очередь запросов клиента.
    """
    logger = logging.getLogger('lab9.ThirdTask')
    logger.info(
        msg=f"Сервер \"{server_name}\" обработал запрос клиента \"{client_name}\" "
            f"в потоке \"{threading.current_thread().name}\"."
    )
    # Массивы с числами
    first_array = []
    second_array = []
    third_array = []
    # Список результатов
    list_of_results = []
    while True:
        main_menu_item, _ = requests_queue.get()
        time.sleep(1)
        logger.info(
            msg=f"Сервер \"{server_name}\" обработал запрос клиента \"{client_name}\" "
                f"в потоке \"{threading.current_thread().name}\"."
        )

        match main_menu_item:
            # Условие задачи
            case 1:
                logger.debug(
                    msg=f"Текущее местоположение - условие задачи."
                )
                print(
                    'Входные данные: три массива с числами. '
                    'Требуется проверить можно ли получить число из 3-го массива, '
                    'арифметическими преобразованиями с числами из двух других массивов. '
                    'Числа проверяются последовательно.'
                )

            # Ввод исходных данных
            case 2:
                logger.debug(
                    msg=f"Текущее местоположение - ввод исходных данных."
                )
                # При вводе новых данных все предыдущие обнуляются
                first_array = []
                second_array = []
                third_array = []
                list_of_results = []
                # Инициализация массивов точек случайным образом
                print('Инициализация первого массива.')
                auto_array_init(first_array)
                print('Инициализация второго массива.')
                auto_array_init(second_array)
                print('Инициализация третьего массива.')
                auto_array_init(third_array)
                print('Инициализация массивов прошла успешно.')

            # Выполнение алгоритма
            case 3:
                logger.debug(
                    msg=f"Текущее местоположение - выполнение алгоритма."
                )
                if len(first_array) < 1 or len(second_array) < 1 or len(third_array) < 1:
                    print(
                        'Невозможно выполнить алгоритм, так как один или несколько массивов пустые. '
                        'Заполните массивы и попробуйте еще раз.'
                    )
                else:
                    list_of_results = arithmetic_conversion(first_array, second_array, third_array)
                    print('Алгоритм успешно выполнен!')

            # Вывод результатов работы алгоритма
            case 4:
                logger.debug(
                    msg=f"Текущее местоположение - вывод результатов работы алгоритма."
                )
                if len(list_of_results) > 0:
                    print(
                        f"Результат работы алгоритма.\n"
                        f"Первый массив чисел: {' '.join(map(str, first_array))}\n"
                        f"Второй массив чисел: {' '.join(map(str, second_array))}\n"
                        f"Третий массив чисел: {' '.join(map(str, third_array))}\n"
                        f"Результат проверки: {' '.join(map(str, list_of_results))}"
                    )
                else:
                    print(
                        'Невозможно вывести результат работы алгоритма, так как алгоритм не был выполнен. '
                        'Запустите работу алгоритма и попробуйте еще раз.'
                    )

            # Выход в главное меню
            case 5:
                logger.debug(
                    msg=f"Текущее местоположение - выход в главное меню."
                )
                break

            case _:
                logger.debug(
                    msg=f"Текущее местоположение - ошибка выбора пункта меню."
                )
                print('В меню всего 5 пунктов. Попробуйте еще раз.')


def arithmetic_conversion(first_array, second_array, third_array):
    """
    Функция реализующая решение следующей задачи:
    Требуется проверить можно ли получить число из 3-го массива, арифметическими преобразованиями
    с числами двух других массивов. Числа проверяются последовательно.
    :param first_array: Первый массив чисел;
    :param second_array: второй массив чисел;
    :param third_array: третий массив чисел, который будет проверяться.
    :return: Список со строками в которых будет содержаться описание результатов проверки
    (можно или нельзя преобразовать).
    """
    list_of_results = ['' for i in range(len(third_array))]
    triples_of_numbers = enumerate(zip(first_array, second_array, third_array))
    for index, triple in triples_of_numbers:
        try:
            check_arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 % elem2, '%'
            )
            check_arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 / elem2, '/'
            )
            check_arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 ** elem2, '**'
            )
            check_arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 * elem2, '*'
            )
            check_arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 - elem2, '-'
            )
            check_arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 + elem2, '+'
            )
        except ZeroDivisionError:
            pass

    for i in range(len(list_of_results)):
        if list_of_results[i] == '':
            list_of_results[i] = f"Нет способов получить {i + 1}-й элемент."

    return list_of_results


def check_arithmetic_operation(index, elem1, elem2, elem3, list_of_results, func, function_symbol):
    """
    Функция реализующая проверку: можно ли получить число из 3-го массива, заданным арифметическим преобразованием
    с числами 2-ух других массивов. В случае положительного результата добавляет полученый способ в список результатов.
    :param index: Индекс проверяемого элемента;
    :param elem1: элемент из первого массива;
    :param elem2: элемент из второго массива;
    :param elem3: элемент из третьего массива (проверяемый элемент);
    :param list_of_results: список полученных результатов;
    :param func: функция которая будет применяться к elem1 и elem2 (арифметическая операция);
    :param function_symbol: строковое отображение арифметической операции (значок).
    """
    if func(elem1, elem2) == elem3:
        if list_of_results[index] == '':
            list_of_results[index] = (f"Способы получить {index + 1}-й элемент: "
                                      f"{elem1} {function_symbol} {elem2} = {elem3};")
        else:
            list_of_results[index] += f"\n{elem1} {function_symbol} {elem2} = {elem3};"
    elif func(elem2, elem1) == elem3:
        if list_of_results[index] == '':
            list_of_results[index] = (f"Способы получить {index + 1}-й элемент: "
                                      f"{elem2} {function_symbol} {elem1} = {elem3};")
        else:
            list_of_results[index] += f"\n{elem2} {function_symbol} {elem1} = {elem3};"
