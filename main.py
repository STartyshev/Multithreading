import queue
import msvcrt
import logging
from client import Client
from server import Server


def main():
    logger = logging.getLogger('lab9')
    FORMAT = '-----%(asctime)s _ %(name)s:%(lineno)s _ %(levelname)s _ %(message)s'
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)
    logger.addHandler(sh)

    requests_queue = queue.Queue(maxsize=5)
    Client('Боб', requests_queue).start()
    Server(1, requests_queue).start()

    print('Чтобы закончить выполнение программы нажмите любую клавишу.')
    msvcrt.getch()


if __name__ == '__main__':
    main()
