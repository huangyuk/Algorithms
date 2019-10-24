file=open('jobs.txt','r')

def sort_diff3(key):
    return key[3]
def sort_diff2(key):
    return key[2]
def sort_diff0(key):
    return key[0]

all_work=list()

# I first store all the jobs in a tuple, the first two argument are weight and length
# the third is their weight minus length, the fourthe is weight/length
for lines in file:
    b=lines.split()
    if len(b)==2:
        all_work.append((int(b[0]),int(b[1]),int(b[0])-int(b[1]),int(b[0])/int(b[1])))

#Question 1
# sort weight minus length in a decreasing order, but still need to break ties
all_work.sort(key=sort_diff2,reverse=True)

# use k=1 to record if the previus terms tie.
# use j to record the first term of consecutive tie terms.
i=0
k=0
#This while loop is used for break ties.
while i<=len(all_work)-2:
    if all_work[i][2]==all_work[i+1][2] and k==0:    #If first tied ,set k=1, store the first tie term as j
        k=1
        j=i
    elif (all_work[i][2]!=all_work[i+1][2] and k==1): #If tie is over, set k=0 and sort these tied terms by weight
        b=all_work[j:i+1]
        b.sort(key=sort_diff0,reverse=True)
        all_work[j:i+1]=b
        k=0
    elif all_work[i][2]==all_work[i+1][2] and k==1 and i==len(all_work)-2: #If the last two terms tie, sort them by weight
        b=all_work[j:i+2]
        b.sort(key=sort_diff0,reverse=True)
        all_work[j:i+2]=b
    i=i+1

time=0
score=0

#counting the weighted score based on the sorted jobs
for i in range(len(all_work)):
    time=time+all_work[i][1]
    score=score+all_work[i][0]*time
print(score)


#Question 2
# sort weight/length in a decreasing order,doesnt need to break ties
all_work.sort(key=sort_diff3,reverse=True)
time=0
score=0
for i in range(len(all_work)):
    time=time+all_work[i][1]
    score=score+all_work[i][0]*time
print(score)
