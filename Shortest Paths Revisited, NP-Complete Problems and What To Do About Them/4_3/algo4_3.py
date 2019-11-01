# This homework asked us to use another algorithm solving the TSP problem.
# Because we have to find the next minimum distance among all unexplored cities,
# I includ numpy and using vectorized calculation which is faster.
# Also, use numpy.amin and numpy.argmin to achieve this goal.
import numpy as np
import math
file=open('nn.txt')
rawpoints=[]
for lines in file:
    lines=lines.split()
    if len(lines)==3:
        rawpoints.append((float(lines[1]),float(lines[2])))

rawpoints=np.array(rawpoints)
points=rawpoints
next_index=0     #index for the next city
total_length=0   #initialized the total traveling distance as zero
first_point=[points[0,:]]     #remember the coordinates of beginning city
total=33708      #There are 33708 points in total
while True:
    print(total)
    this_point=[points[next_index,:]]
    points=np.delete(points,next_index,0)       #remove the current city
    total=total-1
    this_point_vec=np.repeat(this_point,total,axis=0)  # create a matrix of current coordinates. The size is as large as the remaining cities
    diff_square=np.square(points-this_point_vec)
    length_square=np.amin(diff_square[:,0]+diff_square[:,1],0)  #find the shortest city from the current one
    next_index=np.argmin(diff_square[:,0]+diff_square[:,1],0)   #find the index for the shortest city
    total_length=total_length+math.sqrt(length_square)          #add the length to total length
    if total==1:
        break


print(total_length+math.sqrt(np.sum(np.square(points-first_point))))
