"""
This code was written by Ray in response to a stack overflow post.
We are simply packaging it up here for easy use and spread for others.

Original Stack Overflow post:
https://stackoverflow.com/questions/5478351/python-time-measure-function
"""

import time
import functools
from contextlib import contextmanager


def time_func(func):
    @functools.wraps(func)
    def timed_func(*args, **kwargs):
        startTime = time.time()
        out = func(*args, **kwargs)
        elapsedTime = time.time() - startTime
        print('function [{}] finished in {} ms'.format(
            func.__name__, int(elapsedTime * 1000)))
        return out

    return timed_func


@contextmanager
def time_chunk(name):
    startTime = time.time()
    yield
    elapsedTime = time.time() - startTime
    print('[{}] finished in {} ms'.format(name, int(elapsedTime * 1000)))
