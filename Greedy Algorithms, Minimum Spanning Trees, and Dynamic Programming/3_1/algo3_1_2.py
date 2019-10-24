#This homework is the prim's algorithm. We need to include the node with the shortest distance from the explored set(MST) into the explored set(MST).
#Therefore, heap is the most appropriate data structure
# Something about this heap:
# When insert a node to the heap, we plug in both the data and the number of node.
# But when deletion, we need plug in the position of a nodes.
# There is a distionary "node to position" which is used to find the position.

import random

class node:
    min_distance=0
    node_num=0
    def __init__(self,min_distance,node_num):
        self.min_distance=min_distance
        self.node_num=node_num

class min_heap:
    data=list()
    node_to_position=dict()
    def __init__(self):
        self.data.append(node(0,0))
        self.node_to_position[0]=0
    def print(self):
        for i in range(len(self.data)):
            print(self.data[i].min_distance,self.data[i].node_num)
    def swap(self,position1,position2):
        self.node_to_position[self.data[position1].node_num]=position2
        self.node_to_position[self.data[position2].node_num]=position1
        temp=self.data[position1]
        self.data[position1]=self.data[position2]
        self.data[position2]=temp
    def insert(self,min_distance,node_num):
        self.data.append(node(min_distance,node_num))
        self.node_to_position[node_num]=len(self.data)-1
        self.bubble_up(len(self.data)-1)
    def bubble_up(self,position):
        if position>1:
            up_position=self.half(position)
            if self.data[position].min_distance<self.data[up_position].min_distance:
                self.swap(position,up_position)
                self.bubble_up(up_position)
    def half(self,n):
        if n%2==1:
            return int((n-1)/2)
        else:
            return int(n/2)
    def bubble_down(self,position):
        if 2*position+1<=len(self.data)-1:
            if self.data[2*position].min_distance<self.data[2*position+1].min_distance and self.data[position].min_distance>self.data[2*position].min_distance:
                self.swap(position,2*position)
                self.bubble_down(2*position)
            elif self.data[2*position].min_distance>self.data[2*position+1].min_distance and self.data[position].min_distance>self.data[2*position+1].min_distance:
                self.swap(position,2*position+1)
                self.bubble_down(2*position+1)
        elif 2*position>len(self.data)-1:
            return
        else:
            if self.data[position].min_distance>self.data[2*position].min_distance:
                self.swap(position,2*position)
                self.bubble_down(2*position)
    def delete(self,position):
        last_node=len(self.data)-1
        if position==last_node:
            self.node_to_position.pop(self.data[last_node].node_num)
            self.data.pop(last_node)
            return
        else:
            self.swap(position,last_node)
            self.node_to_position.pop(self.data[last_node].node_num)
            self.data.pop(last_node)
        if position==1:
            self.bubble_down(position)
        elif position>1:
            if self.data[position].min_distance<self.data[self.half(position)].min_distance:
                self.bubble_up(position)
            else:
                self.bubble_down(position)



file=open('edges.txt','r')


adjacent_list=[{} for i in range(501)]

# create a mapping between nearby nodes and their distance
for lines in file:
    temp=lines.split()
    if len(temp)==3:
        adjacent_list[int(temp[0])][int(temp[1])]=int(temp[2])
        adjacent_list[int(temp[1])][int(temp[0])]=int(temp[2])

#print(adjacent_list[500])

heap=min_heap()
length=0
explored_node=[0]*len(adjacent_list)

# initialize the distance of those node still NOT in the MST
for i in range(1,len(adjacent_list)):
    heap.insert(10000,i)

#randomly pick one node as the source node,
source=random.randrange(1,len(adjacent_list))

#Initialize the shortest distances from the nearby nodes
heap.delete(heap.node_to_position[source])
explored_node[source]=1
for i in adjacent_list[source]:
    heap.delete(heap.node_to_position[i])
    heap.insert(adjacent_list[source][i],i)

#since the second round, we run this for loop
for i in range(1,len(adjacent_list)-1):
    source=heap.data[1].node_num              #get the node number currently has the shortest distance
    explored_node[source]=1                   #mark it as to be explored
    length=length+heap.data[1].min_distance   #add its length to the length of MST
    heap.delete(1)                            # delete it from the heap
    for j in adjacent_list[source]:           # for every nearby node not in our MST
        if explored_node[j]==0:
            distance=heap.data[heap.node_to_position[j]].min_distance
            heap.delete(heap.node_to_position[j])             # record their distance, take them out of the heap
            distance=min(distance,adjacent_list[source][j])   # calculate their new shortest distances, then place them back to the heap.
            heap.insert(distance,j)
    print(length)

heap.print()
print(length)
