# This homework asks me to use dynamic programming to solve TSP problem

import numpy as np
import math
from itertools import combinations
file=open('tsp.txt','r')

# 25 cities, raw data include their coordinates
rawpoints=[]
for lines in file:
    lines=lines.split()
    if len(lines)==2:
        rawpoints.append((float(lines[0]),float(lines[1])))

distances=np.array([[0]*26]*26,dtype=np.float)
for i in range(1,26):
    for j in range(1,26):
        a=pow(rawpoints[i-1][0]-rawpoints[j-1][0],2)
        b=pow(rawpoints[i-1][1]-rawpoints[j-1][1],2)
        distances[i,j]=pow(a+b,0.5)
        # print(distances[i,j])

# Due to the large number of cities, I divide the cities to two seperate graph and then connect them manually.
# The first part is from city 1 to 13, the second part is from city 12 to 25
distance2=distances[11:,11:]

# I use a hash table (dictionary) to store traveling distances
# This is basically a updated version of two dimension array using the travelled "cities" as first index,
# and the second index is still the destination cities given those cities we passed.

a=dict()
num_points=13

# initialized the distances
for i in range(num_points):
    perm = combinations(range(2,num_points+1), i)
    # print(i)
    for j in list(perm):
        a[j]=[99999]*(num_points+1)

a[()][1]=0

# S is the set of travelled cities
# I use combinations to generate all possible travelling paths
for i in range(1,num_points):
    comb = combinations(range(2,num_points+1), i)   # as i increase, the number of travelled cities increase
    for S in list(comb):
        # print(S)
        for j in S:                  # for every city j in one combination S, we have to result to its last stage S_minus_j
            S_minus_j=S[:S.index(j)]+S[S.index(j)+1:]
            compare_set=[]
            for k in ((1,)+S):       # we have to include 1 as a possible last stage destination.
                if k!=j:             # k can be all possible last stage destination, k can't be j, but k can be 1.
                    compare_set.append(a[S_minus_j][k]+distances[k][j])
            a[S][j]=min(compare_set)    # compare the distance from all possible last stage destination.


# In the last round, all cities are travelled, we have to make one more comparison
comb = combinations(range(2,num_points+1),num_points-1)
compare=[]
temp=list(comb)[0]   # Let temp be the combination including all points
for j in range(2,num_points+1):
    compare.append(a[temp][j]+distances[j,1])   #compare the distances among all possible last stage destination which can be 2,3,...last.
print(compare,min(compare))

part1=min(compare)-distances[12][13]

#By graphical support, we connect 1 to 13, and then connect 12 to 25.
#then minus 2*distance(12,13)


###########################################################

distance2=distances[11:,11:]
a=dict()
num_points=14
for i in range(num_points):
    perm = combinations(range(2,num_points+1), i)
    # print(i)
    for j in list(perm):
        a[j]=[99999]*(num_points+1)
a[()][1]=0
for i in range(1,num_points):
    comb = combinations(range(2,num_points+1), i)
    for S in list(comb):
        # print(S)
        for j in S:
            S_minus_j=S[:S.index(j)]+S[S.index(j)+1:]
            compare_set=[]
            for k in ((1,)+S):
                if k!=j:
                    compare_set.append(a[S_minus_j][k]+distance2[k][j])
            a[S][j]=min(compare_set)

comb = combinations(range(2,num_points+1),num_points-1)
compare=[]
temp=list(comb)[0]
for j in range(2,num_points+1):
    compare.append(a[temp][j]+distance2[j,1])
print(compare,min(compare))
part2=min(compare)-distances[12][13]
print(part1+part2)
