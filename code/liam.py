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
        self.storage = storage

    def add_video(self, video):
        '''
        Add video. If succesful, return True. Otherwise False
        '''
        if storage>=video,memory:
            self.videos.append(video)
            self.storage -= video.memory
            return True
        return False

    def remove_video(self,video):
        '''
        Remove video. If succesful, returns true. Otherwise, false.
        '''
        if video in videos:
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
    def __init__(self, data_center_latency, caches, cache_latencies, videos, requests)
        '''
        data_center_latency : float, latency from data center, ms
        caches: array-like, contains connected caches
        cache_latencies : array-like, list of latencies from each connected cache
        videos: list of requested videos
        requests: list of number of requests per video
        '''
        self.data_center_latency = data_center_latency
        self.caches = caches
        self.cache_latencies = cache_latencies
        self.videos = videos
        self.requests = requests

    def get_requests(self,video):
        '''
        given video, find how many requests it has
        '''
        if video in videos:
            return requests.index(video)
        return 0

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

