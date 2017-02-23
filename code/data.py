import sys
import numpy as np
from liam import Cache, Video, Endpoint

def get_file(filename):

    f = open(filename, 'r')

    info = f.readline().split()
    V = int(info[0])
    E = int(info[1])
    R = int(info[2])
    C = int(info[3])
    X = int(info[4])

    caches = [Cache(X) for c in range(C)]
    videos = []
    endpoints = []


    info = f.readline().split()
    for v in info:
        videos.append(Video(int(v)))

    for e in range(E):
        info = f.readline().split()
        network_latency = int(info[0])
        num_caches = int(info[1])
        endpoints.append(Endpoint(network_latency))
        for c in range(num_caches):
            info = f.readline().split()
            endpoints[e].add_cache(caches[int(info[0])], int(info[1]))

    # Requests 
    for line in f.readlines():
        info = line.split()
        v = int(info[0])
        e = int(info[1])
        nr = int(info[2])
        endpoints[e].add_video(videos[v], nr)

    f.close()
    return V, E, R, C, X, caches, videos, endpoints

""" $ python main.py PATHTOPIZZA """
path = sys.argv[1]
path = '../input/' + path + '.in'
V, E, R, C, X, caches, videos, endpoints = get_file(path)

""" 
    At the top of your file, write:
    from data import V, E, R, C, X, movie_sizes, ...
"""
