import time

def task(i):
    print(f"Task {i} started")
    time.sleep(1)
    print(f"Task {i} finished")

if __name__ == "__main__":
    start = time.perf_counter()

    task(1)

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)")