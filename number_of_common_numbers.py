from correct_initialization import *
import logging
import threading
import queue
import time


# Задача №1
def rq_number_of_common_numbers(client_name, server_name, requests_queue: queue.Queue):
    """
    Функция реализующая перемещенение по меню задачи поиска кол-ва общих чисел в двух массивах.
    Каждое перемещение - ответ на запрос клиента.
    :param client_name: Имя клиента;
    :param server_name: имя сервера;
    :param requests_queue: очередь запросов клиента.
    """
    logger = logging.getLogger('lab9.FirstTask')
    logger.info(
        msg=f"Сервер \"{server_name}\" обработал запрос клиента \"{client_name}\" "
            f"в потоке \"{threading.current_thread().name}\"."
    )
    # Два массива в которых будет осуществляться поиск общих чисел
    first_array = []
    second_array = []
    # Количество общих чисел двух массивов
    num_of_common_numbers = None
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
                    'Входные данные: два массива с числами. Требуется проверить сколько у массивов общих чисел. '
                    'Также число будет считаться общим если оно входит в один массив, а в другом массиве находится '
                    'его перевернутая версия.'
                )

            # Ввод исходных данных
            case 2:
                logger.debug(
                    msg=f"Текущее местоположение - ввод исходных данных."
                )
                first_array = []
                second_array = []
                print('Инициализация первого массива.')
                auto_array_init(first_array)
                print('Инициализация второго массива.')
                auto_array_init(second_array)
                print('Инициализация массивов прошла успешно.')

            # Выполнение алгоритма
            case 3:
                logger.debug(
                    msg=f"Текущее местоположение - выполнение алгоритма."
                )
                if len(first_array) < 1 or len(second_array) < 1:
                    print(
                        'Невозможно выполнить алгоритм, так как один или оба массива пустые. '
                        'Заполните массивы и попробуйте еще раз.'
                    )
                else:
                    num_of_common_numbers = number_of_common_numbers(first_array, second_array)
                    print('Алгоритм успешно выполнен!')

            # Вывод результатов работы алгоритма
            case 4:
                logger.debug(
                    msg=f"Текущее местоположение - вывод результатов работы алгоритма."
                )
                if num_of_common_numbers is not None:
                    print(
                        f"Результат работы алгоритма.\n"
                        f"Первый массива: {' '.join(map(str, first_array))}\n"
                        f"Второй массив: {' '.join(map(str, second_array))}\n"
                        f"Количество общих чисел в обоих массивах: {num_of_common_numbers}"
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


def number_of_common_numbers(first_array, second_array):
    """
    Функция находит количество общих чисел в двух массивах.
    Также, число считается общим если оно входит в один массив, а в другом
    находится его перевернутая версия.
    :param first_array: Первый массив чисел;
    :param second_array: второй массив чисел.
    :return: Возвращает количество общих чисел двух массивов.
    """
    num_of_common_numbers = 0
    # Список в который будут добавляться общие числа
    list_of_common_numbers = []
    for elem in first_array:
        # Если число из первого массива или его обратная версия находятся во втором массиве
        # И это число еще не обрабатывалось прежде т. е. его нет в списке общих чисел
        # То оно добавляется в список и кол-во общих чисел увеличивается на 1
        if ((str(elem) in list(map(str, second_array)) or str(elem)[::-1] in list(map(str, second_array))) and
                elem not in list_of_common_numbers):
            num_of_common_numbers += 1
            list_of_common_numbers.append(elem)
    return num_of_common_numbers
