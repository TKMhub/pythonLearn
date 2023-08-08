import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    logging.debug('start')
    # 何か処理
    logging.debug('end')


def worker2(x, y=1):
    print(threading.current_thread().name, 'start')
    logging.debug(x)
    logging.debug(y)
    # 何か処理
    print(threading.current_thread().name, 'end')


if __name__ == '__main__':
    # スレッドの実行
    t1 = threading.Thread(name='rename worker1', target=worker1)
    t2 = threading.Thread(target=worker2, args=(100, ), kwargs={'y': 200})

    t1.start()
    t2.start()

    t1.join()
    t2.join()