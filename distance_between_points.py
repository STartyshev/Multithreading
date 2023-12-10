from correct_initialization import *
from math import sqrt
import queue
import threading
import logging
import random
import time


# Задача №2
def rq_distance_between_points(client_name, server_name, requests_queue: queue.Queue):
    """
    Функция реализующая перемещенение по меню задачи поиска точек расстояние между,
    которыми больше заданного числа.
    Каждое перемещение - ответ на запрос клиента.
    :param client_name: Имя клиента;
    :param server_name: имя сервера;
    :param requests_queue: очередь запросов клиента.
    """
    logger = logging.getLogger('lab9.SecondTask')
    logger.info(
        msg=f"Сервер \"{server_name}\" обработал запрос клиента \"{client_name}\" "
            f"в потоке \"{threading.current_thread().name}\"."
    )
    # Массивы с точками
    first_array_of_dots = []
    second_array_of_dots = []
    # Словарь в котором ключи - длины отрезков значения, которых больше заданного числа,
    # а значения - пары точек, которые эти отрезки образуют
    dict_of_segments_and_points = dict()
    # Заданное число с которым нужно сравнивать длину отрезков
    max_length = None
    # Флаг состояния
    algorithm_completed = False
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
                    'Входные данные: два массива с точками и число. '
                    'Требуется вывести точки из первого и второго массивов, '
                    'расстояния между которыми больше заданного числа. '
                    'Расстояния считаются только для соответствующих чисел.'
                )

            # Ввод исходных данных
            case 2:
                logger.debug(
                    msg=f"Текущее местоположение - ввод исходных данных."
                )
                # При вводе новых данных все предыдущие обнуляются
                first_array_of_dots = []
                second_array_of_dots = []
                dict_of_segments_and_points = dict()
                algorithm_completed = False
                max_length = random.randint(-20, 20)

                initialization_item, _ = requests_queue.get()
                time.sleep(1)
                logger.info(
                    msg=f"Сервер \"{server_name}\" обработал запрос клиента \"{client_name}\" "
                        f"в потоке \"{threading.current_thread().name}\"."
                )

                # Инициализация массивов точек случайным образом
                logger.debug(
                    msg=f"Текущее местоположение - выбор одного из трех пространств для точек."
                )
                while True:
                    space_selection, _ = requests_queue.get()
                    time.sleep(1)
                    logger.info(
                        msg=f"Сервер \"{server_name}\" обработал запрос клиента \"{client_name}\" "
                            f"в потоке \"{threading.current_thread().name}\"."
                    )
                    if space_selection in (1, 2, 3):
                        break

                print('Инициализация первого массива.')
                ui_auto_array_of_dots_init(first_array_of_dots, space_selection)
                print('Инициализация второго массива.')
                ui_auto_array_of_dots_init(second_array_of_dots, space_selection)
                print('Инициализация массивов прошла успешно.')

            # Выполнение алгоритма
            case 3:
                logger.debug(
                    msg=f"Текущее местоположение - выполнение алгоритма."
                )
                if len(first_array_of_dots) < 1 or len(second_array_of_dots) < 1:
                    print(
                        'Невозможно выполнить алгоритм, так как один или оба массива пустые. '
                        'Заполните массивы и попробуйте еще раз.'
                    )
                else:
                    dict_of_segments_and_points = distance_between_points(
                        first_array_of_dots,
                        second_array_of_dots,
                        max_length
                    )
                    algorithm_completed = True
                    print('Алгоритм успешно выполнен!')

            # Вывод результатов работы алгоритма
            case 4:
                logger.debug(
                    msg=f"Текущее местоположение - вывод результатов работы алгоритма."
                )
                if algorithm_completed:
                    if len(dict_of_segments_and_points.keys()) < 1:
                        print(
                            f"Алгоритм не нашел ни одной пары точек, которые образовали бы отрезок "
                            f"длиной больше {max_length}."
                        )
                    else:
                        print(
                            f"Результат работы алгоритма.\n"
                            f"Первый массив точек: {' '.join(map(str, first_array_of_dots))}\n"
                            f"Второй массив точек: {' '.join(map(str, second_array_of_dots))}\n"
                            f"Список точек расстояние между которыми больше {max_length}: "
                        )
                        for key in dict_of_segments_and_points.keys():
                            print(
                                f"Пара точек: {dict_of_segments_and_points[key]}; длина отрезка, "
                                f"который они образуют: {round(key, 1)}.\n"
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


def distance_between_points(first_array_of_dots, second_array_of_dots, distance):
    """
    Функция поиска точек расстояние между которыми больше заданного.
    :param first_array_of_dots: Первый массив точек;
    :param second_array_of_dots: второй массив точек;
    :param distance: заданное расстояние с которым будут сравниваться длины отрезков двух точек взятых
    из первого и второго массивов.
    :return: Возвращает словарь где ключи - длины отрезков которые больше заданного числа, а значения - пара точек,
    которые эти отрезки образуют.
    """
    return {
        segment_length(dot1, dot2): [dot1, dot2]
        for dot1, dot2 in zip(first_array_of_dots, second_array_of_dots)
        if segment_length(dot1, dot2) > distance
    }


def segment_length(dot1, dot2):
    """
    Функция вычисляющая длину отрезка образованного двумя точками.
    :param dot1: Первая точка;
    :param dot2: вторая точка.
    :return: Возвращает длину отрезка образованного двумя точками.
    """
    return sqrt(
        sum(
            (c1 - c2) ** 2 for c1, c2 in zip(dot1, dot2)
        )
    )
