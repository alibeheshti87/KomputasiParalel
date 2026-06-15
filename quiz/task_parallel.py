import threading

def calculate_sum(data):
    print("Task 1: Sum =", sum(data))

def calculate_avg(data):
    print("Task 2: Average =", sum(data)/len(data))

def find_max(data):
    print("Task 3: Max =", max(data))

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]

    t1 = threading.Thread(target=calculate_sum, args=(data,))
    t2 = threading.Thread(target=calculate_avg, args=(data,))
    t3 = threading.Thread(target=find_max, args=(data,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("All tasks completed")
