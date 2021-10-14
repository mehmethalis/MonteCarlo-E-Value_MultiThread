from tools import TimeTool, ECalculator
from threading import Thread
import os

timer = TimeTool()
timer.start()
calculator = ECalculator()
n = 10000000
threads = []

for i in range(os.cpu_count()):
    threads.append(Thread(target=calculator.value_e(n), args=(n,)))
    print("Thread number :", i)
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

value_e = calculator.get_e()

print("E = %12.8f | A = %d | N = %d" % (value_e, calculator.a, calculator.n))
print("TIME = %.6f seconds" % (timer.get_time()))
