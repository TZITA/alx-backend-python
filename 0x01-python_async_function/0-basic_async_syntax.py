#!/usr/bin/env python3
""" Basic syntax of async fumctions in python """
import asyncio
import random


async def wait_random(max_delay: int = 10.0) -> float:
    """ Async function that awaits for arandom amount of seconds """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
