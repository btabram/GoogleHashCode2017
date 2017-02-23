import sys
import numpy as np

def get_file(filename):

    f = open(filename, 'r')

    info = f.readline().split()
    V = int(info[0])
    E = int(info[1])
    R = int(info[2])
    C = int(info[3])
    X = int(info[4])

    info = f.readline().split()
    S = np.empty(V, dtype=int)
    for i,v  in enumerate(info):
        S[i] = int(v)

    latenc

#    A = np.empty((R, C), dtype=float)
#    for i in range(R):
#        row = f.readline()
#        for j in range(C):
#            if row[j] == 'T':
#                A[i,j] = 1.0
#            else:
#                A[i,j] = 0.0
#    f.close()
#
    return V, E, R, C, X, S

#""" $ python main.py input """
path = sys.argv[1]
path = '../input/' + path + '.in'
V, E, R, C, X, S = get_file(path)

""" 
    At the top of your file, write:
    from data import R, C, L, H
"""
