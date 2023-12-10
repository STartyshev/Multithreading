import queue
import threading
import ttp_lab2
import logging


class Server(threading.Thread):
    """
    Класс сервера реализующий обработку запросов клиента.
    """
    def __init__(self, number, requests_queue: queue.Queue):
        self.server_name = f"Сервер №{number}"
        self.logger = logging.getLogger('lab9.Server')
        threading.Thread.__init__(
            self,
            target=self.response,
            name='Поток сервера',
            args=(requests_queue,),
            daemon=True
        )
        self.logger.debug(
            msg=f"Сервер \"{self.server_name}\" успешно создан."
        )

    def response(self, requests_queue: queue.Queue):
        while True:
            ttp_lab2.tasks_main_menu(requests_queue, self.server_name)

