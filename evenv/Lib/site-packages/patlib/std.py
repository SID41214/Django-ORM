"""Tools that go with the standard lib."""

import sys
import os
from pathlib import Path
import json
import logging
import time
import re
# import dataclasses as dcs
# from typing import Optional, Any

import builtins
import warnings
import contextlib
import subprocess

# Profiling, via `(bash)$ kernprof -l -v myprog.py > profile.txt`
# for any function that have been decorated with @profile.
try:
    profile = builtins.profile  # type: ignore
except AttributeError:
    def profile(func): return func


@contextlib.contextmanager
def nonchalance(*exceptions):
    """Like `contextlib.suppress()`, but ignores (almost) all by default.

    For example, `KeyboardInterrupt` is not suppressed.
    """
    if not exceptions:
        exceptions = (Exception, )
    with contextlib.suppress(*exceptions):
        yield


def do_once(fun):
    """Decorator to function to tell it to only run once.

    A frequent use is to replace the stdlib `warnings` module because it

    - has [this severe bug](https://stackoverflow.com/questions/66388579)
    - also prints the source line where the warning was produced,
      which is ugly (although a formatter can be provided to fix this).
    """
    def new(*args, **kwargs):
        if new._ALREADY_DONE:
            return None  # do nothing
        else:
            new._ALREADY_DONE = True
            return fun(*args, **kwargs)
    new._ALREADY_DONE = False
    return new


def create_logger(name,
                  screen_level=logging.INFO,
                  file_level=logging.DEBUG,
                  filename="mylog", mode="w"):
    """Create logger (this is surprisingly complicated).

    NB: Changing the parameters only works at start-up.

    Note: if running in IPython, log messages get appended,
    even when `mode` is "w".

    - Log-levels above `scree_level` get printed to the terminal.
    - Other messages to to the file `filename`.
    - `NOTSET` messages get passed to the root level,
      and discarded (unless the root level logger is instantiated).

    [Ref](https://stackoverflow.com/a/29087645/38281)

    Example:
    >>> logger = create_logger(__name__)
    >>> logger.log(logging.DEBUG, "Debug message")
    >>> logger.info("Info message")
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    fh = logging.FileHandler(filename, mode)
    fh.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(screen_level)

    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        '[%(asctime)s] %(filename)20s:%(lineno)-4s '
        '%(levelname)8s: %(message)s ', datefmt='%H:%M:%S')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # If called multiple times (eg in the same IPython session)
    # then the messages will duplicate, unless we check this
    # https://stackoverflow.com/a/17745953/38281
    if not logger.hasHandlers():
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger


@contextlib.contextmanager
def rewrite(fname):
    """File-editor contextmanager.

    Example:

    >>> with rewrite("myfile.txt") as lines:
    >>>     for i, line in enumerate(lines):
    >>>         lines[i] = line.replace("old","new")
    """
    with open(fname, 'r') as f:
        lines = [line for line in f]

    yield lines

    with open(fname, 'w') as f:
        f.write("".join(lines))


class Timer():
    """Timer context manager.

    Example::

    >>> with Timer('<description>'):
    >>>     time.sleep(1.23)
    [<description>] Elapsed: 1.23
    """

    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        # pass # Turn off timer messages
        if self.name:
            print('[%s]' % self.name, end=' ')
        print('Elapsed: %s' % (time.time() - self.tstart))


def sub_run(*args, check=True, capture_output=True, text=True, **kwargs):
    """`subprocess.run`, with changed defaults, returning stdout.

    Example:
    >>> gitfiles = sub_run(["git", "ls-tree", "-r", "--name-only", "HEAD"])
    >>> # Alternatively:
    >>> # gitfiles = sub_run("git ls-tree -r --name-only HEAD", shell=True)
    >>> # Only .py files:
    >>> gitfiles = [f for f in gitfiles.split("\n") if f.endswith(".py")]
    """

    x = subprocess.run(*args, **kwargs,
                       check=check, capture_output=capture_output, text=text)

    if capture_output:
        return x.stdout



@contextlib.contextmanager
def set_tmp(obj, attr, val):
    """Temporarily set an attribute.

    Example:
    >>> class A:
    >>>     pass
    >>> a = A()
    >>> a.x = 1  # Try deleting this line
    >>> with set_tmp(a,"x","TEMPVAL"):
    >>>     print(a.x)
    >>> print(a.x)

    Based on
    http://code.activestate.com/recipes/577089/
    """

    was_there = False
    tmp = None
    if hasattr(obj, attr):
        try:
            if attr in obj.__dict__:
                was_there = True
        except AttributeError:
            if attr in obj.__slots__:
                was_there = True
        if was_there:
            tmp = getattr(obj, attr)
    setattr(obj, attr, val)

    try:
        yield  # was_there, tmp
    except BaseException:
        raise
    finally:
        if not was_there:
            delattr(obj, attr)
        else:
            setattr(obj, attr, tmp)


# https://stackoverflow.com/a/2669120
def sorted_human(lst):
    """Sort the given iterable in the way that humans expect."""
    def convert(text): return int(text) if text.isdigit() else text
    def alphanum_key(key): return [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(lst, key = alphanum_key)


def find_1st_ind(xx):
    """Same as `np.nonzero(xx)[0][0]`, but lazy, so maybe faster.

    Why might this be faster, even though it's pure python?
    Because Numpy is "fundamentally a non-lazy computing platform"
    [Ref](https://github.com/numpy/numpy/issues/2269)

    This (and related stuff) being of frequent use, but located here
    (in this obscure library), you might consider vendorising this.
    Also consider:
    >>> list(xx).index(val)
    >>> np.arange(len(xx))[xx==val]

    [Ref](https://stackoverflow.com/a/36837176)
    """
    try:
        return next(k for k, x in enumerate(xx) if x)
    except StopIteration:
        return None
