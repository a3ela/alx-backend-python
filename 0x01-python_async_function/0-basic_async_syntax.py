#!/usr/env python3

import asyncio
import random


async def wait_random(max_delay=10):
    i = random.random() * max_delay
    await asyncio.sleep(i)
    return i
