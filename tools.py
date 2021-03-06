import time
import random


class TimeTool:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = time.time()

    def get_time(self):
        self.end_time = time.time()
        return self.end_time - self.start_time


class ECalculator:
    def __init__(self):
        self.a = 0
        self.n = 0

    def get_e(self):
        return self.a / self.n

    def value_e(self, nn):
        a = 0.0
        for x in range(nn):
            s = 0
            turn = 0
            while s < 1:
                s += random.uniform(0, 1)
                turn += 1
            a += turn
        self.n = nn
        self.a = a
