from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
from threading import Thread
import os
import time


# starts pool execution clock **************************************************************************************
start_pool = time.time()


def thread_pool():
    for _ in range(50000000):
        beta = 0


executor = ThreadPoolExecutor(max_workers=os.cpu_count())
executor.submit(thread_pool())

print(f'ThreadPool execution time: {round(float(time.time() - start_pool), 2)} seconds')


# starts process execution clock **************************************************************************************
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

print(f'Process execution time: {round(float(time.time() - start_process), 2)} seconds')


# starts thread execution clock **************************************************************************************
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

print(f'Thread execution time: {round(float(time.time() - start_thread), 2)} seconds')


# starts normal execution clock **************************************************************************************
start_general = time.time()


def normal_function():
    for _ in range(50000000):
        beta = 0


normal_function()
print(f'Normal execution time: {round(float(time.time() - start_general), 2)} seconds')
