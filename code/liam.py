# liam.py
# Google hashcode 2017

class Cache(object):
    def __init__(self, storage):
        '''
        storage : float, num megabytes of available storage
        '''
        self.total_storage = storage
        self.storage = storage
        self.videos = []
        self.endpoints = []
        self.endpoint_latencies = []

    def add_video(self, video):
        '''
        Add video. If succesful, return True. Otherwise False
        '''
        if not (video in self.videos):
            if self.storage >= video.memory:
                self.videos.append(video)
                self.storage -= video.memory
                return True
        return False

    def add_endpoint(self,endpoint,endpoint_latency):
        self.endpoints.append(endpoint)
        self.endpoint_latencies.append(endpoint)

    def remove_video(self,video):
        '''
        Remove video. If succesful, returns true. Otherwise, false.
        '''
        if video in self.videos:
            self.videos.remove(video)
            self.storage += video.memory
            return True
        return False


class Video(object):
    def __init__(self,memory):
        '''
        memory : float, memory usage of video, Mb
        '''
        self.memory = memory

class Endpoint(object):
    def __init__(self, data_center_latency):
        '''
        data_center_latency : float, latency from data center, ms
        '''
        self.data_center_latency = data_center_latency
        self.caches = []
        self.cache_latencies = []
        self.videos = []
        self.requests = []

    def add_cache(self, cache, latency):
        self.caches.append(cache)
        self.cache_latencies.append(latency)
        cache.add_endpoint(self,latency)

    def add_video(self, video, request):
        if video in self.videos:
            self.requests[self.videos.index(video)] += request
        else:
            self.videos.append(video)
            self.requests.append(request)

    def get_requests(self,video):
        '''
        given video, find how many requests it has
        '''
        if (video in self.videos):
            result = self.requests[self.videos.index(video)]
            if  result <= 0:
                print(result)
            return result
        return 0

    def get_best_cache(self):
        ''' 
        find the best cache - the one which has fewest other nodes
        '''
        num_endpoints = []
        for i,c in enumerate(self.caches):
            num_endpoints.append(len(c.endpoints))

        ranking = sorted(range(len(num_endpoints)), key=lambda k: num_endpoints[k])
        sorted_caches = [self.caches[r] for r in ranking]
        return sorted_caches

    def get_fastest_cache(self,video):
        '''
        find caches with the least latency
        '''
        requests = requests_per_cache( self.caches, video)
        latencies = latency_per_cache( self.caches, self)
        requests_by_latencies = [ requests[i]/latencies[i] for i in range(len(requests)) ]
        ranking = sorted(range(len(requests_by_latencies)), key=lambda k: -requests_by_latencies[k])
        sorted_caches = [self.caches[r] for r in ranking]
        return sorted_caches
                


# misc functions

def move_video( video, from_point, to_point):
    '''
    move video from from_point to to_point.
    If succesful, returns True.
    Otherwise, nothing happens, returns False
    '''
    if from_point.remove_video(video):
        if not to_point.add_video(video):
            from_point.add_video(video)
            return False
        return True
    return False

def requests_per_cache( caches, video):
    requests = []
    for cache in caches:
        request = 0
        for endpoint in cache.endpoints:
            request += endpoint.get_requests(video)
        requests.append(request)
    return requests

def latency_per_cache( caches, endpoint):
    latencies = []
    for cache in caches:
        latencies.append( endpoint.cache_latencies[ endpoint.caches.index(cache) ])
    return latencies

#def greedy_sort_requests_per_cache( caches, videos):
#    for video in videos:
#        requests = requests_per_cache( caches, video)
#        for request,idx in enumerate(requests):
#            if caches[idx].add_video(video):
#                break
#    return caches
