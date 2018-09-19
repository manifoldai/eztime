"""
This code was written by Ray in response to a stack overflow post.
We are simply packaging it up here for easy use and spreading to others.

Original Stack Overflow post:
https://stackoverflow.com/questions/5478351/python-time-measure-function
"""

import time
import logging
import functools
from contextlib import contextmanager

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def time_func(func):
    @functools.wraps(func)
    def timed_func(*args, **kwargs):
        startTime = time.time()
        out = func(*args, **kwargs)
        elapsedTime = time.time() - startTime
        elapsedTime_ms = int(elapsedTime * 1000)
        if elapsedTime_ms > 1000:
            logger.info('function [{}] finished in {} s'.format(
                func.__name__, round(elapsedTime_ms / 1000, 3)))
        else:
            logger.info('function [{}] finished in {} ms'.format(
                func.__name__, elapsedTime_ms))
        return out

    return timed_func


@contextmanager
def time_chunk(name):
    startTime = time.time()
    yield
    elapsedTime = time.time() - startTime
    elapsedTime_ms = int(elapsedTime * 1000)
    if elapsedTime_ms > 1000:
        logger.info('[{}] finished in {} s'.format(name, round(elapsedTime_ms / 1000, 3)))
    else:
        logger.info('[{}] finished in {} ms'.format(name, elapsedTime_ms))
