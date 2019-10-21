# The program is find maximum weight independent set of nodes from path.
# Achieving that the maxumun sum of weights of nodes but choosing two consecutive nodes is not allowed.

file=open('mwis.txt','r')

all_data=[0]
for lines in file:
    lines=int(lines)
    if lines!=1000:
        all_data.append(lines)

#create an list to storing the final solutions for all nodes.
mwis_node=[0 for i in range(1001)]

#create an list to storing the maximum sum of weight until some point.
#This question is like a second order recurrence relation.
#We initial the 0th to be 0 and 1th to be the weight of the first node.
mwis=[0]
mwis.append(all_data[1])

#Since the second node, compare choosing the current node(the previous mustn't chosen) with not choosing the current node.
#choosing the larger one
for i in range(2,1001):
    if mwis[i-1]>=mwis[i-2]+all_data[i]:
        mwis.append(mwis[i-1])
    else:
        mwis.append(mwis[i-2]+all_data[i])

j=1000

#When considering the individuals, we must begin the reconstruction with the last node (the whole problem).
# and consider the previous ones backwardly. If one is chosen, marked it as 1.
while j>=1:
    if mwis[j-1]>=mwis[j-2]+all_data[j]:
        j=j-1
    else:
        mwis_node[j]=1
        j=j-2

for i in [1, 2, 3, 4, 17, 117, 517, 997]:
    print(mwis_node[i])
