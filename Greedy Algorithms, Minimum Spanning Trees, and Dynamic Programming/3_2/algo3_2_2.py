# This problem is the same as 3_2, but instead of providing the required k,
# this one required the inter-cluster distance to be at least 3.
# and it asked for the number of cluster with minumun inter-cluster distance to be 3.
# a sample data "001101011001011100010.." with 24 digits
file=open("clustering_big.txt",'r')

# Due to the large number of data, it is impossible to find all the distances
# First of all, I set up a bloom filter to combine the repeat data, i.e. with a distance of 0.
# Also, I categorize all the data into 25 different group by the sum of their digits.
all_data=[[] for i in range(25)]
bloom=dict()
index=0

for lines in file:
    if bloom.get(lines,0)==0:
        bloom[lines]=1
        index=index+1
        lines=lines.split()
        temp=[]
        sum=0
        if len(lines)>3:
            for i in lines:
                i=int(i)
                sum=sum+i
                temp.append(i)
            temp2=[index]
            temp2.extend(temp)
            all_data[sum].append(temp2)

print(index)
cluster=list()
leader=list()
num_group=index

for i in range(index+1):
    cluster.append([i])
    leader.append(i)


# because there is no edge with length 0, we first merge the edges with length 1.
# Since it can only happend between neighbours, I will use a for loop between all neighbour groups.
# using this function to detect their distance
def hdist1(a,b):
    dist=0
    for i in range(1,len(a)):
        if a[i]!=b[i]:
            dist=dist+1
            if dist>=2:         # for two data, if the difference is above 1, we return false
                return False
    return True

# The edges with lenght of 2 can only happen within the same group or between groups with a difference of 2 in their "sum indices".
def hdist2(a,b):
    dist=0
    for i in range(1,len(a)):
        if a[i]!=b[i]:
            dist=dist+1
            if dist>=3:
                return False
    return True

# If the lengths satisfy the requirement, we merge this two data.
# Still using union find algoritm
def merge(a,b):
    global num_group
    leader1=leader[a]
    leader2=leader[b]
    if len(cluster[leader1])>=len(cluster[leader2]):
        for j in cluster[leader2]:
            leader[j]=leader1
        cluster[leader1].extend(cluster[leader2])
    elif len(cluster[leader1])<len(cluster[leader2]):
        for j in cluster[leader1]:
            leader[j]=leader2
        cluster[leader2].extend(cluster[leader1])
    num_group=num_group-1
    # print(num_group)

# scan the distribution of number of data among all groups indexed by the sum of digits.
for i in range(len(all_data)):
    print(len(all_data[i]))

def merge_1(group1,group2):
    for i in group1:
        for j in group2:
            if leader[i[0]]!=leader[j[0]]:
                if hdist1(i,j):
                    merge(i[0],j[0])

def merge_2(group1,group2):
    for i in group1:
        for j in group2:
            if leader[i[0]]!=leader[j[0]]:
                if hdist2(i,j):
                    merge(i[0],j[0])

# run this loop between neighbour groups to merge edges with length 1
for i in range(25):
    if i==24:
        break
    print(i)
    merge_1(all_data[i],all_data[i+1])

# run this loop within the same group and between groups with a difference of 2 in their "sum indices".
for i in range(25):
    print(i)
    merge_2(all_data[i],all_data[i])
    if i+2<=24:
        merge_2(all_data[i],all_data[i+2])

print(num_group)
