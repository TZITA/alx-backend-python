# PYTHON ASYNC COMPREHENSION

## Task 0:
## Async Generator
A coroutine called async_generator that takes no arguments.
The coroutine loops 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10.

## Task 1:
## Async Comprehensions
A coroutine called async_comprehension that takes no arguments.
The coroutine collects 10 random numbers using an async comprehensing over async_generator then return the 10 random numbers.

## Task 2:
## Run time for four parallel comprehensions
A measure_runtime coroutine that executes async_comprehension four times in parallel using asyncio.gather.
measure_runtime measures the total runtime and return it.
