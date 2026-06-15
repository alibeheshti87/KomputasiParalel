from multiprocessing import Process, Queue
import time

def worker(queue, name):
    while not queue.empty():
        task = queue.get()
        print(f"{name} processing task: {task}")
        time.sleep(0.5)  # simulasi beban
    print(f"{name} finished")

if __name__ == "__main__":
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    queue = Queue()

    # Masukkan semua task ke queue
    for task in tasks:
        queue.put(task)

    p1 = Process(target=worker, args=(queue, "Worker 1"))
    p2 = Process(target=worker, args=(queue, "Worker 2"))
    p3 = Process(target=worker, args=(queue, "Worker 3"))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("All tasks completed")
