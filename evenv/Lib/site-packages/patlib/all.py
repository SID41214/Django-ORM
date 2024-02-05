"""Import *contents* of all submodules.

This is a dynamic (run-time) versions of this:

    from .std  import *
    from .misc import *
    from .math import *
    ...

Don't want to put this in `patlib/__init__.py`,
(even if just using `__all__`, which won't yield submodule contents),
coz then I cannot selectively import a submodule (eg `patlib.math`)
without executing the others.
"""

# TODO: include imports from extras? Eg fig_layout.freshfig, AlignedDict, etc


# from importlib import import_module
from pathlib import Path as _Path # mangle to avoid cleaning up std.py:Path below.

def import_contents(f):
    """<https://stackoverflow.com/a/41991139/38281>"""

    module = __import__(__package__+"."+f.stem, fromlist=['*'])
    # module = import_module("."+f.stem, __package__)

    # Filter keys
    if hasattr(module, '__all__'):
        keys = module.__all__
    else:
        keys = [k for k in dir(module) if not k.startswith('_')]

    # Update globals
    globals().update({k: getattr(module, k) for k in keys})

# https://stackoverflow.com/a/60861023
for _file in _Path(__file__).parent.glob("*.py"):
    if _file!=_Path(__file__) and not _file.stem.startswith("_"):
        import_contents(_file)
# Recursive solution (if that's ever needed):
# https://stackoverflow.com/q/3365740
