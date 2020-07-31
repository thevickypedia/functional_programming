from multiprocessing import Process
import os
import time
from threading import Thread

start_process = time.time()


def process_function():
    for _ in range(50000000):
        alpha = 0


processes = []

for _ in range(os.cpu_count()):
    processes.append(Process(target=process_function))

for process in processes:
    process.start()

for process in processes:
    process.join()

print(f'Process execution time: {round(float(time.time() - start_process), 2)}')


start_thread = time.time()


def thread_function():
    for _ in range(50000000):
        beta = 0


threads = []

for _ in range(os.cpu_count()):
    threads.append(Thread(target=thread_function))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f'Thread execution time: {round(float(time.time() - start_thread), 2)}')
