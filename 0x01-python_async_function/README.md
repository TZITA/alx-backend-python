# PYTHON ASYNC FUNCTIONS

## Task 0:
## The basics of async
An asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

## Task 1:
## Let's execute multiple coroutines at the same time with async
An async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. wait_random runs n times with the specified max_delay.

wait_n returns the list of all the delays (float values). The list of the delays is in  ascending order without using sort().

## Task 2:
## Measure the runtime
A measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. The function should return a float and time module is used to measure an approximate elapsed time.

## Task 3:
## Tasks
A regular function task_wait_random that takes an integer max_delay and returns a asyncio.Task.

## Task 4:
## Tasks
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.
