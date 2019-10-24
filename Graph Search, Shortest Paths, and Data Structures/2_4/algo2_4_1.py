file=open('sum.txt','r')

a=list()

for lines in file:
    lines=int(lines)
    a.append(lines)
a.sort()
i=0
j=len(a)-1
d=dict()
while i<j:
    if a[i]+a[j]>10000:
        j=j-1
    elif a[i]+a[j]<-10000:
        i=i+1
    else:
        k=j
        while i<k:
            if a[i]+a[k]<=10000 and a[i]+a[k]>=-10000:
                d[a[i]+a[k]]=1
                k=k-1
            elif a[i]+a[k]<-10000:
                break
        i=i+1
print(len(d))


# for i in [-3,-1,1,2,9,11,7,6,2]:
#     a[i]=1
#
# c1=input('lower bound')
# c2=input('upper bound')
#
# c1=int(c1)
# c2=int(c2)
# c=0


# for j in range(c1,c2+1):
#     for i in a:
#         if a.get(j-i,0)!=0 and j!=2*i:
#             c=c+1
#             print(c)
#             break
