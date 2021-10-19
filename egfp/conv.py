#!/usr/bin/env python

import sys
import numpy as np
import math

if __name__ == '__main__':
    if (len(sys.argv) != 5):
        print( './conv.py excitations sigma(eV) min(eV) max(eV)', file=sys.stderr)
        sys.exit(-1)

    # load data
    exc = np.loadtxt(sys.argv[1])
    sigma = float(sys.argv[2])
    mine = float(sys.argv[3])
    maxe = float(sys.argv[4])

    #convolved spectra
    spec = np.zeros((math.ceil((maxe-mine)/0.01),2))
    i = 0
    for pt in np.arange(mine, maxe, 0.01):
        v = 0.0
        for tr in range (exc.shape[0]):
            v += exc[tr,1]* math.exp(-(pt-exc[tr,0])**2 / sigma**2)
        spec[i,0] = pt
        spec[i,1] = v
        i = i+1
    np.savetxt("spec.xvg", spec, delimiter='\t')
