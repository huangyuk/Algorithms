# This program creates 4 clusters among data using an approach of maximizing the intercluster distance.
# Equivalently, beginning with including data with smallest distance into one set.
# This idea is similar with Kruskal's algorithm for MST.

file=open('clustering1.txt','r')

all_node=[]
for lines in file:
    lines=lines.split()
    if len(lines)==3:               # The first two arguments are the node numbers of a edge, the last argument is its length
        data=(int(lines[0]),int(lines[1]),int(lines[2]))
        all_node.append(data)



#To perform the union find algorithm, we need two list
#"leader" shows the current cluster name of every node
#"cluster" shows all the node belongs to the same cluster.
# We know that there are 500 data, initiating them into different sets.

cluster=list()
leader=list()
for i in range(501):
    cluster.append([i])
    leader.append(i)

#We have to sort the edges by their lengths,then beginning to merge from the shortest edge.
def sort(tup):
    return tup[2]
all_node.sort(key=sort)
# print(all_node[:10])

k=500
i=0

# This part is an old version of union find algorithm
# while True:
#     first_node=all_node[i][0]
#     second_node=all_node[i][1]
#     if leader[first_node]!=leader[second_node]:
#         if len(cluster[first_node])<=len(cluster[second_node]):
#             for j in cluster[first_node]:
#                 leader[j]=leader[second_node]
#         elif len(cluster[first_node])>len(cluster[second_node]):
#             for j in cluster[second_node]:
#                 leader[j]=leader[first_node]
#         temp1=cluster[first_node]
#         temp2=cluster[second_node]
#         temp1.extend(temp2)
#         for j in temp1:
#             cluster[j]=temp1
#         k=k-1
#     i=i+1
#     if k==4:
#         break

# k represent the current number of clusters. We keep combine sets until k=4
k=500
i=0       #beginn with the shortest edge
while True:
    first_node=all_node[i][0]
    second_node=all_node[i][1]
    leader1=leader[first_node]
    leader2=leader[second_node]
    if leader1!=leader2:         #compare the leader of the two vertices of the shortest edge. If unequal, merge them
        if len(cluster[leader1])<=len(cluster[leader2]):         # the smaller group is absorbed to another.
            for j in cluster[leader1]:                           # "cluster" record all the member of the these two group
                leader[j]=leader2                                # update the leaders of all members in the smaller group
            cluster[leader2].extend(cluster[leader1])            # update the members of the leader of the larger
        elif len(cluster[leader1])>len(cluster[leader2]):
            for j in cluster[leader2]:
                leader[j]=leader1
            cluster[leader1].extend(cluster[leader2])
        k=k-1
    i=i+1
    if k==4:
        break


# Becaue the question asks for the smaller distance among different clusters.
# I keep using the "edge index" i to search for the next edge crossing different clusters
while True:
    first_node=all_node[i][0]
    second_node=all_node[i][1]
    if leader[first_node]!=leader[second_node]:
        break
    i=i+1

print(all_node[i])
