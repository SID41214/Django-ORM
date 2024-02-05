"""Provision commonly used math tools."""
import numpy as np
import numpy.random as rnd
# import scipy as sp  # useless
from scipy import linalg
from scipy import stats

from scipy.linalg import svd
from scipy.linalg import eig
# eig() of scipy.linalg necessitates using np.real_if_close().
from scipy.linalg import sqrtm, inv, eigh

# Don't shadow builtins: sum, max, abs, round, pow
from numpy import (
    pi, nan,
    floor, ceil,
    sqrt, log, log10, exp, sin, cos, tan,
    mean, prod, diff, cumsum,
    array, asarray, asmatrix,
    linspace, arange, reshape,
    eye, zeros, ones, diag, trace
)
