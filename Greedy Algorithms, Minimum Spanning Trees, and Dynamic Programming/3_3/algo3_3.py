#The purpose of this program is counting the expected length of a string coded by hoffman code.
#The character is provided with their frequency.
file=open('huffman.txt','r')
index=-1
all_data=[() for i in range(1000)]
all_data_copy=[() for i in range(1000)]

for lines in file:
    lines=int(lines)
    if lines!=1000:       # because the first line is the total number of data, 1000.
        index=index+1
        all_data[index]=([index],lines)
        all_data_copy[index]=([index],lines)   # The original list will be sorted by their frequency.
                                            #I'll need a copy of the original data.

# This functon is for sorting purpose.
def ind(a):
    return a[1]

# I'll need a array storing the length for each character
length=[0 for i in range(1000)]

# Sorting according to their frequency
all_data.sort(key=ind)

while len(all_data)>1:
    for i in all_data[0][0]:            # Add a digit to the least two frequent substring
        length[i]=length[i]+1
    for i in all_data[1][0]:
        length[i]=length[i]+1
    temp_node=all_data[0][0]            # Combining the substring with the least frequency
    temp_node.extend(all_data[1][0])
    temp_weight=all_data[0][1]+all_data[1][1]  # Combining the frequency of substrings with the least frequency
    new_node=(temp_node,temp_weight)    # create the combination of the least two strings
    all_data.pop(0)                     # take the least two substrings out
    all_data.pop(0)
    all_data.append(new_node)           # adding the new substring into the tree
    all_data.sort(key=ind)              # sorting by the frequence

length.sort()
print(length)
