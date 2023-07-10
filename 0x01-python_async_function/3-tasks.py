#!/usr/bin/env python3
""" Asyncio Tasks """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Returns asyncio.task of the wait_random() asyn function"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
