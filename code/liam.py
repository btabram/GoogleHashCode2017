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

    def add_video(self, video, requests):
        self.videos.append(video)
        self.requests.append(requests)

    def get_requests(self,video):
        '''
        given video, find how many requests it has
        '''
        if video in self.videos:
            return self.requests[self.videos.index(video)]
        return 0

    def get_best_cach(self):
        ''' 
        find the best cache - the one which has fewest other nodes
        '''
        ranking = [] * len(self.caches)
        for c in self.caches:

        return ranking


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
        for endpoints in caches.endpoints:
            request += endpoint.get_requests(video)
        requests.append[request]
    return requests
            
