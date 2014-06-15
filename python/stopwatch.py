import time

class StopWatch:
    def __init__(self):
        self.__start_time = 0
        self.__stop_time = 0

    def start(self):
        self.__start_time = time.time()

    def stop(self):
        self.__stop_time = time.time()

    def time(self):
        return self.__stop_time - self.__start_time

