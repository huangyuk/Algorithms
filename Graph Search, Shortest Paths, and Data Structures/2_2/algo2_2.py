
file=open('dijkstraData.txt','r')

#graph is a list of dictionaries storing all node's edges and their distances.
graph=[{} for i in range(201)]
for lines in file:
    line=lines.split()
    node_num=int(line[0])
    for i in range(1,len(line)):
        temp=line[i].find(',')
        graph[node_num][int(line[i][:temp])]=int(line[i][temp+1:])

# min_heap=[0,30,40,80,100,10,20]
#initialize the heap, ready to store the shortest distance ready to be taken out.
min_heap=[1000000]*201
min_heap[0]=0
min_heap[1]=0


#initialize two dict to search position of a node in the heap and vice versa.
node_to_position=dict()
for i in range(len(min_heap)):
    node_to_position[i]=i
position_to_node=dict()
for i in range(len(min_heap)):
    position_to_node[i]=i

#initialize a list storing the confirmed shortest distance
shortest=[1000000]*len(min_heap)
shortest[0]=0

#swap function swap two nodes in the heap according to their positions.
#the relevant information storing in dictionaries also swap.
def swap(position1,position2):
    temp_num=min_heap[position1]
    node_1=position_to_node[position1]
    node_2=position_to_node[position2]
    node_to_position[node_1]=position2
    node_to_position[node_2]=position1
    position_to_node[position1]=node_2
    position_to_node[position2]=node_1
    min_heap[position1]=min_heap[position2]
    min_heap[position2]=temp_num


#bubble_up and bubble down is using for heapify some node not following the heap properties.
def bubble_down(n):   #n is the position in the heap
    if 2*n<=len(min_heap)-1 and (2*n+1)<=len(min_heap)-1:
        if min_heap[2*n]<=min_heap[2*n+1] and min_heap[n]>min_heap[2*n]:
            swap(n,2*n)
            bubble_down(2*n)
        elif min_heap[2*n]>=min_heap[2*n+1] and min_heap[n]>min_heap[2*n+1]:
            swap(n,2*n+1)
            bubble_down(2*n+1)
    elif 2*n<=len(min_heap)-1 and (2*n+1)>len(min_heap)-1:
        if min_heap[2*n]<min_heap[n]:
            swap(n,2*n)
            bubble_down(2*n)

def bubble_up(n):    #n is the position in the heap
    if n>1:
        b=myhalf(n)
        if min_heap[b]<=min_heap[n]:
            return
        else:
            swap(b,n)
            bubble_up(b)


#delete_node is a function delete a node.
def delete_node(node_num):
    n=node_to_position[node_num]
    if n==len(min_heap)-1:                 # if the node is the last node, no swap needed
        node_to_position.pop(node_num)
        position_to_node.pop(len(min_heap)-1)
        del min_heap[len(min_heap)-1]
    elif n<len(min_heap)-1:                # if the node is not the last node
        swap(n,len(min_heap)-1)
        node_to_position.pop(node_num)
        position_to_node.pop(len(min_heap)-1)
        del min_heap[len(min_heap)-1]
        if n==1:                           # if the node is the first node
            bubble_down(n)
        else:                              # if the node is neither the first nor the last
            if min_heap[n]<min_heap[myhalf(n)]:
                bubble_up(n)
            else:
                bubble_down(n)


# def delete_node(node_num):
#     n=node_to_position[node_num]
#     last_distance=min_heap[len(min_heap)-1]
#     last_node=position_to_node[len(min_heap)-1]
#     min_heap[n]=min_heap[len(min_heap)-1]
#     position_to_node[n]=last_node
#     node_to_position.pop(node_num)
#     node_to_position[last_node]=n
#     position_to_node.pop(len(min_heap)-1)
#     del min_heap[len(min_heap)-1]
#     bubble_down(n)


#In python round(1.5)=2      round(2.5)=2, therefore we need the function
def myhalf(a):
    if a%2==1:
        return int((a-1)/2)
    else:
        return int(a/2)

#insert a node with their value to the heap.
def insert_node(node_num,key):
    min_heap.append(key)
    last_position=len(min_heap)-1
    node_to_position[node_num]=last_position
    position_to_node[last_position]=node_num
    bubble_up(last_position)


#main algorithm, refering to Dijkstra
while (min_heap[1]!=1000000):
    taking_out_node=position_to_node[1]
    shortest[taking_out_node]=min_heap[1]
    delete_node(taking_out_node)
    for i in graph[taking_out_node]:
        if i in node_to_position:
            position_temp=node_to_position[i]
            dist_temp=min_heap[position_temp]
            delete_node(i)
            dist_temp=min(dist_temp,shortest[taking_out_node]+graph[taking_out_node][i])
            insert_node(i,dist_temp)
    print(shortest)
    if len(min_heap)==1:
        break

print(min_heap)

a=[7,37,59,82,99,115,133,165,188,197]
for i in a:
    print(shortest[i])

def check_heap():
    for i in range(2,len(min_heap)):
        a=myhalf(i)
        if min_heap[i]<min_heap[myhalf(i)]:
            print('FALSE')

check_heap()

# while True:
#     c=input('the node you want to bubble_up')
#     bubble_up(int(c))
#     print(min_heap,node_to_position)



# print(min_heap,node_to_position,position_to_node)
