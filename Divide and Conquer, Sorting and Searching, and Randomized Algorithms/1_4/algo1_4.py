import random
xfile=open('kargerMinCut.txt')
graph=list();
for lines in xfile:
    t=lines.split();
    graph.append(t);

# print(len(graph))
# print(graph[len(graph)-1])
# print(graph[1])
# temp=len(graph[1])
#
# for i in range(temp):
#     if graph[1][i] == '3':
#             print(i)
#             print(graph[1][i])
# print(graph[1]);

# print(graph)

# for i in range(len(graph)):
#     print(graph[i],'\n\n\n')


def findidx(graph,x):
    for i in range(len(graph)):
        if x==graph[i][0]:
            length=len(graph[i])
            # print('The node number is',x,'\nThe node is',graph[i],'\nIts length is',length,'\n')
            # print(i)
            return i;


def removedge(graph,firstnode,secondnode):
    firstidx=findidx(graph,firstnode)
    secondidx=findidx(graph,secondnode)
    for i in range(len(graph[firstidx])):
        if graph[firstidx][i]==secondnode:
            del graph[firstidx][i];
            break;
    for j in range(len(graph[secondidx])):
        if graph[secondidx][j]==firstnode:
            del graph[secondidx][j];
            break;



def removeself(graph,firstidx):
    i=len(graph[firstidx])-1
    while i>0:
        if graph[firstidx][i]==graph[firstidx][0]:
            del graph[firstidx][i];
        i=i-1

def run(graph):
    firstidx=random.randint(0, len(graph)-1);
    # print('First idx is',firstidx)
    # print('First node is',graph[firstidx])
    firstnode=graph[firstidx][0];
    findidx(graph,firstnode)
    secondidx=random.randint(1,len(graph[firstidx])-1)
    a1=len(graph[firstidx])
    # print('The second index is',secondidx,'\n')
    secondnode=graph[firstidx][secondidx]
    secondidx=findidx(graph,secondnode)

    b1=len(graph[secondidx])
    # print('Second idx is',secondidx)
    # print('Second node is',graph[secondidx],'\n')
    removedge(graph,firstnode,secondnode);
    # print('First node is',graph[firstidx],'\n')
    # print('Second node is',graph[secondidx],'\n')
    # a2=len(graph[firstidx])
    # b2=len(graph[secondidx])
    # for i in [1,2,3]:
    #     print(graph[findidx(graph,graph[secondidx][i])])

    for nodes in graph[secondidx]:
        if nodes!=secondnode:
            graph[firstidx].append(nodes);
            tempidx=findidx(graph,nodes);
            for i in range(len(graph[tempidx])):
                if graph[tempidx][i]==secondnode:
                    graph[tempidx][i]=firstnode;
    # for i in [1,2,3]:
    #     print(graph[findidx(graph,graph[secondidx][i])])


    # print('First node is',graph[firstidx],'\n')
    # print('Second node is',graph[secondidx],'\n')
    # a3=len(graph[firstidx])
    # b3=len(graph[secondidx])
    removeself(graph,firstidx);
    del graph[secondidx];
    # print(graph[firstidx])
    # print(a1,a2,a3,b1,b2,b3)

#
#
#     for nodes in graph[secondidx]:
#         if(nodes!=firstnode and nodes!=secondnode):
#             tempidx=findidx(graph,nodes)
#             if firstnode in graph[tempidx]:
#                 graph[tempidx].remove(secondnode);
#             elif firstnode not in graph[tempidx]:
#                 graph[tempidx].append(firstnode);
#                 graph[tempidx].remove(secondnode);
#             if nodes not in graph[firstidx]:
#                 graph[firstidx].append(nodes)
#     print('The first node after is',graph[firstidx])
#     print(a+b-k,len(graph[firstidx]),'\n\n\n')
#     del graph[secondidx]
#


final=list()
for i in range(100):
    xfile=open('kargerMinCut.txt')
    graph=list();
    for lines in xfile:
        t=lines.split();
        graph.append(t);
    for j in range(198):
        run(graph)
    final.append(len(graph[0])-1)

print(final)
print(min(final))

#
#
# for i in range(len(graph)):
#     print(graph[i])
