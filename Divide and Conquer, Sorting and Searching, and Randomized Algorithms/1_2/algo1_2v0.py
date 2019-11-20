xfile=open('IntegerArray.txt','r')

a=list()
for line in xfile:
    a.append(int(line))

# while True:
#     b=input('')
#     if b=='done':
#         break
#     a.append(int(b))


def merge(seq):
    if len(seq)==1:
        return(seq)
    n2=round(len(seq)/2)
    subseq1=merge(seq[0:n2])
    subseq2=merge(seq[n2:])
    mergeseq=list()
    i=0
    j=0
    while True:
        if subseq1[i]<subseq2[j]:
            mergeseq.append(subseq1[i])
            i=i+1
            if i==len(subseq1):
                mergeseq.extend(subseq2[j:])
                break
        else:
            mergeseq.append(subseq2[j])
            j=j+1
            if j==len(subseq2):
                mergeseq.extend(subseq1[i:])
                break
    return(mergeseq)

def count(seq):
    if len(seq)==1:
        return(0)
    n1=round(len(seq)/2)
    first=count(seq[0:n1])
    second=count(seq[n1:])
    splitcount=[0]
    subseq1=merge(seq[0:n1])
    subseq2=merge(seq[n1:])
    i=0
    j=0
    while True:
        if subseq1[i]<subseq2[j]:
            i=i+1
            if i==len(subseq1):
                break
        else:
            splitcount[0]=splitcount[0]+len(subseq1)-i
            j=j+1
            if j==len(subseq2):
                break
    totalcount=first+second+splitcount[0]
    return totalcount

print(a,count(a))

# def f1(): #outer function
#     a = [1]
#     def f2(): #outer function
#         print(a)
#         a[0] = a[0] + 1
#         print (a) #prints 2
#     f2()
#     print (a) #prints 2
# f1()


# sort=merge(a)
# i=0
# while i<100000:
#     print(sort[i:i+20])
#     i=i+20
