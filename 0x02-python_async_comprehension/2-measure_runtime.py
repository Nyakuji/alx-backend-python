#!/usr/bin/env python3
""""Runtime for four parallel comprehensions"""
import asyncio
import random
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that will execute async_comprehension four times in parallel
    using asyncio.gather.
    Returns:
        float: total runtime
    """
    t1 = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    t2 = time.time()
    return t2 - t1
