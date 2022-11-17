import time
import threading
import multiprocessing

def task(i):
    print(f"Task {i} started")
    time.sleep(1)
    print(f"Task {i} finished")

if __name__ == "__main__":
    start = time.perf_counter()

    t1 = threading.Thread(target=task, args=(1,))
    t1.start()
    t1.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)")