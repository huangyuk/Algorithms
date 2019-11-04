#This program use depth first search to calculate the strongly connected component with the most amount of nodes
import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(171088640)

file=open('SCC.txt')
rawgraph1=list()
rawgraph2=list()

i=0
for line in file:
    a=line.split()
    a[0]=int(a[0])
    a[1]=int(a[1])
    rawgraph1.append(a[0])
    rawgraph2.append(a[1])

total_node=max(max(rawgraph1),max(rawgraph2))

# A function for create a forward graph or inverse graph
def create_graph(graph1,graph2):
    newgraph=[[] for i in range(total_node+1)]
    for i in range(len(graph1)):
        newgraph[graph1[i]].append(graph2[i])
    return newgraph

t=0
s=0

def DFS1(graph,node):
    global t;
    global s;
    global leader;
    leader[node]=s
    for i in graph[node]:
        if leader[i]==0:
            DFS1(graph,i);
    t=t+1;
    finish_order[t]=node;

def DFS2(graph,node):
    global s;
    global leader;
    leader[node]=s
    for i in graph[node]:
        if leader[i]==0:
            DFS2(graph,i);

newgraph=create_graph(rawgraph1,rawgraph2)
newgraph_reverse=create_graph(rawgraph2,rawgraph1)
leader=[0]*(total_node+1)
finish_order=[0]*(total_node+1)

def main():
    global s;
    global leader;
    i=total_node;
# Run the first round of DFS
    while i>0:
        s=i;
        if leader[i]==0:
            DFS1(newgraph_reverse,i)
        i=i-1
    leader=[0]*(total_node+1)
    i=total_node;
# Run the second round of DFS
    while i>0:
        s=finish_order[i];
        if leader[s]==0:
            DFS2(newgraph,s)
            # print(s)
        i=i-1
    count=[0]*(total_node+1)
    for i in leader[1:]:
        count[i]=count[i]+1
    count.sort()
    print(count)
    # a=0
    # for i in range(1,875715):
    #     a=count[i]+a
    # print(a)
thread = threading.Thread(target=main)
thread.start()
