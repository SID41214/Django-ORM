"""Provision matplotlib. Used via `from patlib.all import *`."""
import matplotlib as mpl
from matplotlib import pyplot as plt

# Even though patlib is only meant for toying around,
# I don't think I should do this just yet.
# For example, for jupyter notebooks,
# it might be desirable to not do it.
# plt.ion()
