# liam.py
# Google hashcode 2017

class Cache(object):
    def __init__(self, storage, endpoints, latencies):
        '''
        storage : float, num megabytes of available storage
        endpoints : array-like, list of endpoints connected to cache
        latencies : array-like, latency in ms for each endpoint
        '''
        self.total_storage = storage
        self.endpoints = endpoints
        self.latencies = latencies
        self.num_endpoints = len(endpoints)
        self.videos = []
        self.remaining_storage = storage

    def add_video(self, video, requests):
        self.videos.append(video)
        remaining_storage -= video.memory

class Video(object):
    def __init__(self,memory):
        '''
        memory : float, memory usage of video, Mb
        '''
        self.memory = memory

class Endpoint(object):
    def __init__(self, data_center_latency, caches, cache_latencies):
        '''
        data_center_latency : float, latency from data center, ms
        caches: array-like, contains connected caches
        cache_latencies : array-like, list of latencies from each connected cache
        '''
        self.data_center_latency = data_center_latency
        self.caches = caches
        self.cache_latencies = cache_latencies
