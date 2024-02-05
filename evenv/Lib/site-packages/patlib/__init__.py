"""A small, personal, `pylab`.

Its purpose is to provide shorthands,
and so should not be used in production code.
It may be loaded with wildcard, eg:

- from patlib.all import *  # executes all submodules
- from patlib.math import * # won't execute the other submodules
"""

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata  # type: ignore

# https://github.com/python-poetry/poetry/pull/2366#issuecomment-652418094
__version__ = importlib_metadata.version(__name__)
