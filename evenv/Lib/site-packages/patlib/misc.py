"""Various tools
"""
import numpy as np

# TODO: include Bunch and NestedPrint?
# TODO: implement sort_keys choice

def aprint(A):
    """
    Array summary.

    TODO: Adjust edgeitems depending on int/float.
    """
    shape = A.shape
    opts  = np.get_printoptions()

    #lw = get_lw(do_compensate_prompt=False)
    #if len(shape)==1:
        #nitems = int((lw - 5)/(opts['precision'] + 1)) - 1
        #np.set_printoptions(linewidth=lw,edgeitems=3,threshold=nitems)

    AA = np.abs(A)
    mina = AA.min()
    maxa = AA.max()

    print_bold = lambda s: print('\033[94m', s, "\033[0m")

    # Common exponent
    p = opts['precision']
    expo = 1
    if maxa != 0:
        if mina > 10**(p-3):
            expo = int(np.log10(mina))
        elif maxa < 10**-(p-3):
            expo = int(np.log10(maxa))-1

    print_bold("array(")
    if expo==1:
        print(str(A))
        print_bold(")")
    else:
        print(str(A / 10**expo))
        print_bold(") * 1e" + str(expo))

    #
    ind2sub = lambda ind: np.unravel_index(ind, A.shape)
    min_sub  = ind2sub(np.argmin(A))
    max_sub  = ind2sub(np.argmax(A))
    amin_sub = ind2sub(np.argmin(AA))
    amax_sub = ind2sub(np.argmax(AA))
    mins = A[min_sub], min_sub, A[amin_sub], amin_sub
    maxs = A[max_sub], max_sub, A[amax_sub], amax_sub

    # Stats
    print("shape    :", shape)
    print("sparsity : {:d}/{:d}".format(A.size-np.count_nonzero(A),A.size))
    print("mean     : {: 10.4g}".format(A.mean()))
    print("std      : {: 10.4g}".format(A.std(ddof=1)))
    print("min (ij) : {: 10.4g} {!r:7},   amin (ij): {: 10.4g} {!r:7}".format(*mins))
    print("max (ij) : {: 10.4g} {!r:7},   amax (ij): {: 10.4g} {!r:7}".format(*maxs))


try:
    import pyperclip
    def paste_array(dtype=float, sep=" "):
        """Paste array from clipboard (plaintext) into python.

        NB: only works on Matlab matrices of size (1,length).
        But it should be easy to adapt this function for other shapes.

        In Matlab, to copy into clipboard, use:
        (Matlab)>>> clipboard('copy',myMatrix)
        """

        # Grab from clipboard
        d = pyperclip.paste()[1:-1]

        # Detect and trim brackets
        i0 =  1 if d[ 0]=='[' else None
        i1 = -1 if d[-1]==']' else None

        d = np.fromstring(d, dtype=dtype, sep=sep)
        return d
except ImportError:
    pass
