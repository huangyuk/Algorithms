# The purpose of this homework is writing a hash table
# Since Python already include a hash table, dictionary, I just use it.

file=open('sum.txt','r')

a=dict()

for lines in file:
    lines=int(lines)
    if lines not in a:
        a[lines]=1
    else:
        a[lines]=a[lines]+1

c=0
#To find all the numbers j between -10000 and 10000 which is the sum of two distinct number in this hash table.
# First let i in the hash table, then find if j-i is also in the hash table, but exclude the possibility that j=2*i
for j in range(-10000,10001):
    print(j)
    for i in a:
        if a.get(j-i,0)!=0 and j!=2*i:  # exclude the situation that j=2*i
            c=c+1
            print(c)
            break
print(c)
