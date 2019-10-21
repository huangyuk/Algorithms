# the Organization of this program is the same as the previous one, just because there are 2000 possible items
# we modify our program to save the memory

file=open("knapsack_big.txt",)
read=1
all_data=[0]
for lines in file:
    if read>=2:
        lines=lines.split()
        all_data.append((int(lines[0]),int(lines[1])))
    read=read+1
# print(all_data)

#we just assign two rows and iterate on these two instead of memeorize everything
value_table=[[0 for j in range(2000001)] for i in range(2)]

for i in range(1,2001):
    for j in range(1,2000001):
        if j-all_data[i][1]<0:
            value_table[1][j]=value_table[0][j]
        else:
            value_table[1][j]=max(value_table[0][j], value_table[0][j-all_data[i][1]]+all_data[i][0])
    value_table[0]=value_table[1][:]   #when copying the latest news on the old row,
                                       #we have to use [:] to access the vector store in the list.
                                       #otherwise we just copy the pointers rather than all the values.
    print(i)

print(value_table[1][1999995:])
