#This program is used to do all pairs shortest distances for three different graph, g1,g2, and g3
# I implemented Floyd-Washall algorithm to establish a three dimension array to solve it.
# I include numpy to better munipulate the three dimension array better.

import numpy as np
file1=open('g1.txt','r')
file2=open('g2.txt','r')
file3=open('g3.txt','r')

all_data=[0]
for lines in file3:
    lines=lines.split()
    if len(lines)>2:          #There is one line in the original file irrelevent to the graph. I only involve the meaningful data.
        all_data.append((int(lines[0]),int(lines[1]),int(lines[2])))


#There are 1000 nodes, typically this algorithm need 1000^3 spaces to store values.
#If the memeory is insufficient, we can replace the third dimension with 2
#Then iterate between 0 and 1 in the third dimension to memeorize the latest shortest path.
num_node=1000
all_distance = np.array([[[9999]*2]*1001]*1001)     #set the distance between points still without a path to be a large number 9999.

# To initialize the matrix, let the initial shortest distance between nearby points to be the length of edges.
for i in range(1,len(all_data)):
    tail_node=all_data[i][0]
    head_node=all_data[i][1]
    length=all_data[i][2]
    all_distance[tail_node,head_node,0]=length

# To initialize the matrix, let the distance of the same point to be 0
for i in range(1,1001):
    all_distance[i,i,0]=0


for k in range(1,1001):
    for i in range(1,1001):
        for j in range(1,1001):
            k_not_in=all_distance[i,j,0]                   #Calculate the shortest path, if the current kth node is not in.
            k_in=all_distance[i,k,0]+all_distance[k,j,0]   #Calculate the shortest path, if the current kth node is in.
            all_distance[i,j,1]=min(k_not_in,k_in)         # for each pair of i,j, Set the shortest path to be the smaller one
    all_distance[:,:,0]=all_distance[:,:,1]                # After a whole round for node k, replace the k-1 level with the kth level
    print(k)
    if sum(np.diag(all_distance[:,:,0])<0)>0:              # If any self-distance is negative, there is a negative cycle and break
        print("negative cycle detected.")
        break

#The question asked us to find the minimum of shortest paths among all different nodes,
#I first add 9999 to self distances in case 0 is the shortest distance.
#Then use np.amin to find the minimum of the last i,j matrix when k=1000.
new=np.eye(1001)*9999+all_distance[:,:,1]
print(np.amin(new))
