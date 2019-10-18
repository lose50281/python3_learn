import time
import logging


def log():
    def wrapper(func):
        logging.warning("%s is hello" %func)






def fuck():
    a = time.time()
    print(a)
    return a


fuck()














