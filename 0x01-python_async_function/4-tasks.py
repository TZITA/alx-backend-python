#!/usr/bin/env python3
""" """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async fun that returns list of concurrently executed task_wait_random()
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    sorted_res = sorted(await asyncio.gather(*coroutines))
    return sorted_res
