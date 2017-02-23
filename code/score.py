import numpy as np
import sys
from data import V, E, R, C, X, movie_sizes, latencies, num_caches, requests

filename = str(sys.argv[1])
out_file = filename + '.out'

fout = open(out_file, 'r')
lines = fout.readlines()

for i in range(0,len(lines)):
    lines[i] = lines[i].replace("\n","")

print(lines)

for l in lines[1:]:
    print(l.split())

# data = np.loadtxt(filename, skiprows=1)
# score = np.sum((data[:,2]+1-data[:,0]) * (data[:,3]+1-data[:,1]))
# print(score / (R * C))

