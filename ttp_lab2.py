from number_of_common_numbers import *
from distance_between_points import *
from arithmetic_conversion import *
import queue
import time
import logging


def tasks_main_menu(requests_queue: queue.Queue, server_name):
    """
    Функция главного меню.
    """
    logger = logging.getLogger('lab9.MainMenu')
    while True:
        task_selection_item, client_name = requests_queue.get()
        time.sleep(1)

        match task_selection_item:
            case 1:
                logger.debug(
                    msg="Текущее положение - выбор пал на первую задачу."
                )
                rq_number_of_common_numbers(client_name, server_name, requests_queue)

            case 2:
                logger.debug(
                    msg="Текущее положение - выбор пал на вторую задачу."
                )
                rq_distance_between_points(client_name, server_name, requests_queue)

            case 3:
                logger.debug(
                    msg="Текущее положение - выбор пал на третью задачу."
                )
                rq_arithmetic_conversion(client_name, server_name, requests_queue)

            case 4:
                logger.debug(
                    msg="Текущее положение - выход к выбору новой задачи."
                )
                return

            case _:
                logger.debug(
                    msg="Текущее положение - ошибка выбора пункта главного меню."
                )
                print('В меню всего 4 пункта. Попробуйте еще раз.')
