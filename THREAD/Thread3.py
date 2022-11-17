import threading
import time

start = time.perf_counter()
t1 = threading.Thread(target=task, args=[1])
t1.start

t2 = threading.Thread(target=task, args=[2])
t2.start

t1.join()
t2.join()

finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")