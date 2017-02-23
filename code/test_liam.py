
from liam import *

v1 = Video(10)
v2 = Video(20)
v3 = Video(30)
v4 = Video(30)

E = Endpoint(1000)

C = Cache(100)

E.add_cache(C,1000)
E.add_video(v1,1500)
E.add_video(v2,5500)
E.add_video(v3,2500)

C.add_video(v2)

print( v2 in E.videos )
print( v4 in E.videos )
print( v2 in E.caches[E.caches.index(C)].videos )
print( v2 in C.endpoints
