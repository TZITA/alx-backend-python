#!/usr/bin/env python3
""" Asyncio Tasks """
import asyncio
from typing import Awaitable


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable:
    """ Returns asyncio.task of the wait_random() asyn function"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
