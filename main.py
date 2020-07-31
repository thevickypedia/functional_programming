from multiprocessing import Process
import os
import time
from threading import Thread

start_process = time.time()


def process_function():
    for _ in range(50000000):  # runs loops for 50 million times
        alpha = 0


processes = []  # creates an empty list for processes

# the loop below appends the processes of how many times the function should be executed (number of CPUs in this case).
for _ in range(os.cpu_count()):  # _ is a throw away variable here as I'm going to use it anywhere in the loop
    processes.append(Process(target=process_function))  # **
# ** Note that we just pass the function unexecuted as we do not want to execute the function without multiprocessing

# starts the function as many times as in the processes
for process in processes:
    process.start()  # starts each process in the processes list

# finishes all the processes
# without using join() here, the code will continue to execute without finishing all the processes
for process in processes:
    process.join()

# prints the run time using multiprocessing
print(f'Process execution time: {round(float(time.time() - start_process), 2)}')


start_thread = time.time()


def thread_function():
    for _ in range(50000000):  # runs loops for 50 million times
        beta = 0


threads = []  # creates an empty list for threads

# the loop below appends the threads of how many times the function should be executed (number of CPUs in this case).
for _ in range(os.cpu_count()):  # _ is a throw away variable here as I'm going to use it anywhere in the loop
    threads.append(Thread(target=thread_function))  # **
# ** Note that we just pass the function unexecuted as we do not want to execute the function without multithreading

# starts the function as many times as in the threads
for thread in threads:
    thread.start()  # starts each process in the processes list

# finishes all the threads
# without using join() here, the code will continue to execute without finishing all the threads
for thread in threads:
    thread.join()

# prints the run time using multithreading
print(f'Thread execution time: {round(float(time.time() - start_thread), 2)}')
