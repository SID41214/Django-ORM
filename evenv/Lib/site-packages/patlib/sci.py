"""Scientific tools."""

import numpy as np


def uniquish(a, rtol=1e-05, atol=1e-08):
    """Return unique elements of a.

    The ordering is kept, in the sense that
    the earliest appearance of an element is kept.

    Useful for example to eliminate equal roots (up to convergence)
    from `scipy.optimize.fsolve`.

    [Ref1](https://stackoverflow.com/a/37847116)
    [Ref2](https://stackoverflow.com/a/38653131)

    Examples:
    >>> uniquish([1, 2, 3, 1+1e-5])
    array([1., 2., 3.])
    >>> uniquish([1, 2, 3, 1+2e-5])
    array([1., 2., 3., 1.])
    """
    a = np.asarray(a)
    assert a.ndim == 1, "Unique only makes sense for 1d arrays."
    # NB: column vector (e.g.) yields wrong answer.
    equal = np.isclose(a, a[:, None], rtol, atol, equal_nan=True)
    return a[~(np.triu(equal, 1)).any(0)]
