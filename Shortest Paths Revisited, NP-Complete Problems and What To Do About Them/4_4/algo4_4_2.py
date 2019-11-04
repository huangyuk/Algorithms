#This program using Strongly Connected Components solving the 2SAT problem
filename='2sat6.txt'
file=open(filename)
for lines in file:
    lines=lines.split()
    if len(lines)==1:
        num_node=int(lines[0])

#Initialized a dictionary ready to store all the directed edges
raw_graph=dict()
j=-1*num_node
while j<=num_node:
    raw_graph[j]=[]
    j=j+1

#store all the directed edges
file=open(filename)
for lines in file:
    lines=lines.split()
    if len(lines)==2:
        first=int(lines[0])
        second=int(lines[1])
        raw_graph[-1*first].append(second)
        raw_graph[-1*second].append(first)

#Initialized the explored index and first round ending index
first_round_index=[0]*(num_node*2+1)
explored=dict()
j=-1*num_node
while j<=num_node:
    explored[j]=0
    j=j+1


explored[0]=1
current_label=1
def dfs_first_round(node):
    global current_label
    for i in raw_graph[node]:
        if explored[i]==0:
            explored[i]=1
            dfs_first_round(i)
    first_round_index[current_label]=node     #store the node number at the position of its ending order of the list.
    current_label=current_label+1

index=-1*num_node
while index<=num_node:
    if explored[index]==0:
        explored[index]=1
        dfs_first_round(index)
    index=index+1

######The following are the second round deph first search determing the SCC
raw_graph2=dict()

#create the inversed directed graph
j=-1*num_node
while j<=num_node:
    raw_graph2[j]=[]
    j=j+1
j=-1*num_node
while j<=num_node:
    for i in raw_graph[j]:
        raw_graph2[i].append(j)
    j=j+1


j=-1*num_node
while j<=num_node:
    explored[j]=0
    j=j+1
explored[0]=1
# use a dictionary to store the SCC leading index
SCC=dict()
SCC_index=0
def dfs_second_round(node):
    global SCC_index
    SCC[node]=SCC_index
    for i in raw_graph2[node]:
        if explored[i]==0:
            explored[i]=1
            dfs_second_round(i)

#beginning with the largest first round ending order
index=2*num_node
while index>=1:
    second_index=first_round_index[index]    #read the real node number from its ending order.
    if explored[second_index]==0:
        SCC_index=second_index
        explored[second_index]=1
        dfs_second_round(second_index)
    index=index-1


# Check if any index and its negative have the same SCC.
index=1
while index<=num_node:
    if SCC[index]==SCC[-1*index]:
        print('unsatisfied')
        break
    index=index+1
