import random
import threading
import queue
import logging
import time


class Client(threading.Thread):
    """
    Класс клинента реализующий отправку запросов.
    """
    def __init__(self, name, requests_queue: queue.Queue):
        self.client_name = name
        self.logger = logging.getLogger('lab9.Client')
        threading.Thread.__init__(
            self,
            target=self.request,
            name='Поток клиента',
            args=(requests_queue,),
            daemon=True
        )
        self.logger.debug(
            msg=f"Клиент \"{self.client_name}\" успешно создан."
        )

    def request(self, requests_queue: queue.Queue):
        while True:
            requests_queue.put((random.randint(1, 5), self.client_name))
            self.logger.info(
                msg=f"Клиент \"{self.client_name}\" отправил запрос из потока \"{threading.current_thread().name}\"."
            )
            time.sleep(2)
