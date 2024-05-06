#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns wait_random tasks and
    returns delays in ascending order.

    Parameters:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay value for each task.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
