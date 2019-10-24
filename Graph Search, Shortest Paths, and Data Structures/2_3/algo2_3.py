# For this median maintainence problem, we need two heaps,
# One is min heap keep the smallest at the first position, and the other is max heap, which keeps the maximum at the first position.

class min_heap:
    data=[0]
    def __init__(self):
        print(self.data)
    def print(self):
        print(self.data)
    def swap(self,position1,position2):
        temp=self.data[position1]
        self.data[position1]=self.data[position2]
        self.data[position2]=temp
    def insert(self,new):
        self.data.append(new)
        self.bubble_up(len(self.data)-1)
    def bubble_up(self,node):
        if node>1:
            up_node=self.half(node)
            if self.data[node]<self.data[up_node]:
                self.swap(node,up_node)
                self.bubble_up(up_node)
    def half(self,n):
        if n%2==1:
            return int((n-1)/2)
        else:
            return int(n/2)

    def bubble_down(self,node):
        if 2*node+1<=len(self.data)-1:
            if self.data[2*node]<self.data[2*node+1] and self.data[node]>self.data[2*node]:
                self.swap(node,2*node)
                self.bubble_down(2*node)
            elif self.data[2*node]>self.data[2*node+1] and self.data[node]>self.data[2*node+1]:
                self.swap(node,2*node+1)
                self.bubble_down(2*node+1)
        elif 2*node>len(self.data)-1:
            return
        else:
            if self.data[node]>self.data[2*node]:
                self.swap(node,2*node)
                self.bubble_down(2*node)
    def delete(self,node):
        last_node=len(self.data)-1
        if node==last_node:
            self.data.pop(last_node)
            return
        else:
            self.swap(node,last_node)
            self.data.pop(last_node)
        if node==1:
            self.bubble_down(node)
        elif node>1:
            if self.data[node]<self.data[self.half(node)]:
                self.bubble_up(node)
            else:
                self.bubble_down(node)

class max_heap:
    data=[0]
    def __init__(self):
        print(self.data)
    def print(self):
        print(self.data)
    def swap(self,position1,position2):
        temp=self.data[position1]
        self.data[position1]=self.data[position2]
        self.data[position2]=temp
    def half(self,n):
        if n%2==1:
            return int((n-1)/2)
        else:
            return int(n/2)
    def insert(self,new):
        self.data.append(new)
        self.bubble_up(len(self.data)-1)
    def bubble_up(self,node):
        if node>1:
            up_node=self.half(node)
            if self.data[node]>self.data[up_node]:
                self.swap(node,up_node)
                self.bubble_up(up_node)
    def bubble_down(self,node):
        if 2*node+1<=len(self.data)-1:
            if self.data[2*node]>self.data[2*node+1] and self.data[node]<self.data[2*node]:
                self.swap(node,2*node)
                self.bubble_down(2*node)
            elif self.data[2*node]<self.data[2*node+1] and self.data[node]<self.data[2*node+1]:
                self.swap(node,2*node+1)
                self.bubble_down(2*node+1)
        elif 2*node>len(self.data)-1:
            return
        else:
            if self.data[node]<self.data[2*node]:
                self.swap(node,2*node)
                self.bubble_down(2*node)
    def delete(self,node):
        last_node=len(self.data)-1
        if node==last_node:
            self.data.pop(last_node)
            return
        else:
            self.swap(node,last_node)
            self.data.pop(last_node)
        if node==1:
            self.bubble_down(node)
        elif node>1:
            if self.data[node]>self.data[self.half(node)]:
                self.bubble_up(node)
            else:
                self.bubble_down(node)


file=open('Median.txt','r')

rawdata=list()
for lines in file:
    rawdata.append(int(lines))


max_heap=max_heap()
min_heap=min_heap()


#a is the max heap and b is the min heap
def balance(a,b):
    if len(a.data)>len(b.data)+1:
        temp=a.data[1]
        a.delete(1)
        b.insert(temp)
    elif len(a.data)<len(b.data):
        temp=b.data[1]
        b.delete(1)
        a.insert(temp)
    return a.data[1]         # Always return the first element in the max heap as the current median

#Initialize the first median
# The "sum" store the sum of medians for other purpose
median=[]
sum=[]
max_heap.data.append(rawdata[0])
median.append(rawdata[0])
sum.append(median[0])

for i in range(1,len(rawdata)):
    if rawdata[i]>max_heap.data[1]:
        min_heap.insert(rawdata[i])
    else:
        max_heap.insert(rawdata[i])
    median.append(balance(max_heap,min_heap))    # For each insertion, we check if the heaps need to be balanced, then return the meadian
    sum.append(sum[i-1]+median[i])

print(median[0:10])
print(sum[0:10])
