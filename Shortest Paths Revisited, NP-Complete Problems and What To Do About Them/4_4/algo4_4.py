# This homework uses local search algorithm to solve 2SAT problem
import numpy as np
file=open('2sat3.txt')
raw_data=[0]

# Store each clause as a list of tuple
for lines in file:
    lines=lines.split()
    if len(lines)==1:
        num_node=int(lines[0])
    else:
        raw_data.append((int(lines[0]),int(lines[1])))

# Use an array to store the current correctness,
# later we will change the value of some variables among those in incorrect clauses
clauses_correctness=np.array([0]*(num_node+1))
assign_values=np.random.randint(2,size=(num_node+1))

j=0
# Due to the large number of variables, 100,000~1,000,000.
# Here we basically keep running until satisfied or manually stop the program when it get too long.
while j<=(num_node^2):
    j=j+1
    index=1
    while index<=num_node:
        i=raw_data[index][0]
        j=raw_data[index][1]
        if i>0 and j>0:
            if assign_values[i]==1 or assign_values[j]==1:
                clauses_correctness[index]=1
            else:
                clauses_correctness[index]=0
        elif i>0 and j<0:
            if assign_values[i]==1 or assign_values[-1*j]==0:
                clauses_correctness[index]=1
            else:
                clauses_correctness[index]=0
        elif i<0 and j>0:
            if assign_values[-1*i]==0 or assign_values[j]==1:
                clauses_correctness[index]=1
            else:
                clauses_correctness[index]=0
        elif i<0 and j<0:
            if assign_values[-1*i]==0 or assign_values[-1*j]==0:
                clauses_correctness[index]=1
            else:
                clauses_correctness[index]=0
                #print(index)
        index=index+1
    sum_correct=sum(clauses_correctness))
    print(sum_correct)
    if sum_correct==num_node:
        print('satisfied')
        find=True
        break
    unsatisfied=np.where(clauses_correctness==0)[0] #Find those incorrect clauses
    if len(unsatisfied)<3:
        updating_clause=np.random.choice(unsatisfied[1:])   #eliminate zero then choose one of the clause
        updating_var=np.absolute(np.random.choice(raw_data[updating_clause]))
        if assign_values[updating_var]==0:                  #randomly choose one of the variables then change its value
            assign_values[updating_var]=1
        elif assign_values[updating_var]==1:
            assign_values[updating_var]=0
    else:       #Due to large number of variables, choose a larger number of incorrect clauses speed up the program.
        updating_clause=np.random.choice(unsatisfied[1:],size=len(unsatisfied)-2,replace=False)
        for m in updating_clause:
            updating_var=np.absolute(np.random.choice(raw_data[m]))
            if assign_values[updating_var]==0:
                assign_values[updating_var]=1
            elif assign_values[updating_var]==1:
                assign_values[updating_var]=0


#The left are outcomes using local search; the right are by strongly connected components.
#1                    1
#0 (possible)         0
#0 (possible)         1
#0 (should be)        1
#                     0
#0 (should be)        0
