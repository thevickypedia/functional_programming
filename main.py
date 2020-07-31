from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
from threading import Thread
import os
import time

'''

\\\\ThreadPoolExecutor: Spins up multiple threads and using these threads to perform tasks in a concurrent fashion.
By using multiple threads we can speed up applications which face an input/output based bottleneck during web crawling.
\\\\Multiprocessing: Runs a function code as different process. So if a multiprocess is set to run for 5 times, 
there will be 5 PIDs running where in general a code runs with a single PID.
\\\\Multithreading: Runs a function code as a single process but creates multiple threads within that process id. So
if a multithread is set to run for 5 times, there will still be one PID running but creates multiple threads within.

'''

# starts pool execution clock **************************************************************************************
start_pool = time.time()


# the loop runs for 50 million times
def thread_pool():
    for _ in range(50000000):  # _ is a throw away variable here as I'm going to use it anywhere in the loop
        beta = 0


# executor below initiates the thread pool workers of how many times the function should be executed in sequence
executor = ThreadPoolExecutor(max_workers=os.cpu_count())  # (number of CPUs in this case)
executor.submit(thread_pool())  # triggers the function here

print(f'ThreadPool execution time: {round(float(time.time() - start_pool), 2)} seconds')

# starts process execution clock **************************************************************************************
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
print(f'Process execution time: {round(float(time.time() - start_process), 2)} seconds')

# starts thread execution clock **************************************************************************************
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

# finishes threads, without using join() here, the code will continue to execute without finishing all the threads
for thread in threads:
    thread.join()

# prints the run time using multithreading
print(f'Thread execution time: {round(float(time.time() - start_thread), 2)} seconds')

# starts normal execution clock **************************************************************************************
start_general = time.time()


def normal_function():
    for _ in range(50000000):
        beta = 0


normal_function()
print(f'Normal execution time: {round(float(time.time() - start_general), 2)} seconds')
