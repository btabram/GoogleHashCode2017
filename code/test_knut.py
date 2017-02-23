from liam import Cache, Video, Endpoint
from data import V, E, R, C, X, caches, videos, endpoints

for e in endpoints: 
    best_caches = e.get_best_cach()
    print(best_caches)
