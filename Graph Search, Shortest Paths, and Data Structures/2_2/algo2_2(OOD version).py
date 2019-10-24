file=open('dijkstraData.txt','r')

#graph is a list of dictionaries storing all node's edges and their distances.
graph=[{} for i in range(201)]
for lines in file:
    line=lines.split()
    node_num=int(line[0])
    for i in range(1,len(line)):
        temp=line[i].find(',')
        graph[node_num][int(line[i][:temp])]=int(line[i][temp+1:])


#For each node, it contain a minimum distance from the explored nodes and its node number
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
    # the function of extract is replaced by delete(1)
    # def extract(self):
    #     temp=len(self.data)-1
    #     self.swap(1,temp)
    #     self.node_to_position.pop(self.data[temp].node_num)
    #     self.data.pop(temp)
    #     self.bubble_down(1)

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


#initiate the confirmed closest distance to be 1000000 except for 0.
closest=[1000000]*201
closest[0]=0

test=min_heap()

#initiate the so far closest distance as 1000000 except for 1, because this is the source node
for i in range(1,201):
    test.insert(1000000,i)
test.data[1].min_distance=0
print(graph[1])

for i in range(1,201):
    node_num=test.data[1].node_num                   #read the node number of the first node in the heap
    closest[node_num]=test.data[1].min_distance      #assign its distance as the confirmed minimun distance
    test.delete(1)                                   #delete the first node from the heap
    for j in graph[node_num]:
        if closest[j]==1000000:                      # for the nodes directed by the previous first node and whose min distance are not confirmed
            position=test.node_to_position[j]        # take them out from the heap and reinsert them with their new so far min distance
            distance=test.data[position].min_distance
            test.delete(position)
            distance=min(distance,closest[node_num]+graph[node_num][j])
            test.insert(distance,j)
print(closest)


for i in [7,37,59,82,99,115,133,165,188,197]:
    print(closest[i])

# print(test.node_to_position)
# test.print()


# test.delete(3)
# test.print()







#
