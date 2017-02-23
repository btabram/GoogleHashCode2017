import numpy as np
from liam import Cache, Endpoint, Video, move_video
from data import V, E, R, C, X, videos, endpoints, caches

def find_max_request(reqs):
    """ find the largest request in a requests array
        return the video and endpoint
        and zero the request in the array for next time
    """
    mx = 0
    v_max = -1
    e_max = -1
    for e in range(0,E):
        for v in range(0,V):
            if reqs[e,v] > mx:
                mx = reqs[e,v]
                v_max = v
                e_max = e
    # zero the max element so we can find the next largest next time
    reqs[e_max,v_max] = 0
    return v_max, e_max

def get_requests():
    """ return an array of the requests
        first index is endpoints
        second is videos
    """
    reqs = np.zeros((E,V), dtype=int)
    for e in range(0,E):
        for v in range(0,V):
            reqs[e,v] = endpoints[e].get_requests(videos[v])
    return reqs

def do_the_stuff():
    # get array of requests
    requests = get_requests()

    # loop over all requests
    for i in range(0,R):

        # get the biggest request
        max_v, max_e = find_max_request(requests)

        # stopping criteria here because we're done all requests. Just a loop counter?
        if max_v == -1:
            print('dealt with all requests')

        # get the caches associated with the max endpoint, sorted in order of best-ness
        max_caches = endpoints[max_e].get_best_cache()

        # try and add the video to the best cache, and then the others
        for cache in max_caches:
            retn = cache.add_video(videos[max_v])
            if retn == True:
                break

def write():
    # assumption that we will be using all the caches
    
    count = 0
    for c in caches:
        if len(c.videos) != 0:
            count = count + 1
    print(count)

    it = 1
    for c in caches:
        # print(len(c.videos))
        print(caches.index(c), end='')
        for v in c.videos:
            # print out the video numbers on the same line, space separated
            print(' ' + str(videos.index(v)), end='')
        # print newline at the end
        print()
        # stop when we've done all the caches we're using
        if it == count:
            break
        it = it + 1

