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

    # Movie sizes in MB
    movie_sizes = np.zeros(V, dtype=int)
    info = f.readline().split()
    for i,v  in enumerate(info):
        movie_sizes[i] = int(v)

    # Data centre latencies per endpoint
    latencies = np.zeros((E, C+1), dtype=int)
    # Caches per endpoint
    num_caches = np.zeros(E, dtype=int)

    for e in range(E):
        info = f.readline().split()
        latencies[e, -1] = int(info[0])
        num_caches[e] = int(info[1])
        for c in range(num_caches[e]):
            info = f.readline().split()
            latencies[e, int(info[0])] = int(info[1])

    # Requests 
    requests = np.zeros((V, E), dtype=int)
    for line in f.readlines():
        info = line.split()
        requests[int(info[0]), int(info[1])] = int(info[2])

    f.close()
    return V, E, R, C, X, movie_sizes, latencies, num_caches, requests

""" $ python main.py PATHTOPIZZA """
path = sys.argv[1]
path = '../input/' + path + '.in'
V, E, R, C, X, movie_sizes, latencies, num_caches, requests = get_file(path)

""" 
    At the top of your file, write:
    from data import V, E, R, C, X, movie_sizes, ...
"""
