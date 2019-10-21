#This program is for solving the ordinary knapsack problam using dynamic programming

file=open("knapsack1.txt",)
read=1
all_data=[0]

# I store all the weights and values in a list of tuple. index 0 is the value;index 1 is the weight
# using the order in list as the name of all the objects. beginning with 1; end with 100. The zero postion is 0;
for lines in file:
    if read>=2:
        lines=lines.split()
        all_data.append((int(lines[0]),int(lines[1])))
    read=read+1
print(all_data)

# Creat a 100X10000 two dimensional array for storing the maximum value.
# The first dimension is the objects we can use so far, the second dimension is the space we can use so far.
value_table=[[0 for j in range(10001)] for i in range(101)]

#fill out the maximum table and we can know the maximun possible value we can carry.
for i in range(1,101):
    for j in range(1,10001):
        if j-all_data[i][1]<0:      #if current space is even smaller than the ith object, we dont think about adding ith in.
            value_table[i][j]=value_table[i-1][j]
        else:                       #choose the maximum value between to add or not to add the ith item.
            value_table[i][j]=max(value_table[i-1][j], value_table[i-1][j-all_data[i][1]]+all_data[i][0])

print(value_table[100][9995:])
