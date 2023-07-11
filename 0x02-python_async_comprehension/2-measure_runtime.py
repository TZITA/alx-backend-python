#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Async function to measure execution time """
    start = time.perf_counter()
    res = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*res)
    end = time.perf_counter()

    return end - start
