xfile=open('IntegerArray.txt');
a=list()
for i in xfile:
    a.append(int(i));
# print(a)

count=0

def merge(seq1,seq2):
    i=0;j=0;sol=list();
    global count
    while ((i<len(seq1))or(j<len(seq2))):
        if seq1[i]>seq2[j]:
            sol.append(seq2[j]);
            j=j+1;
            count=count+len(seq1)-i;
            if j==len(seq2):
                sol.extend(seq1[i:])
                break;
        else:
            sol.append(seq1[i]);
            i=i+1;
            if i==len(seq1):
                sol.extend(seq2[j:])
                break;
    return(sol);


def part(seq):
    l=len(seq)
    if l==1:
        return seq;
    else:
        # print(l,l/2,round(l/2),seq[:round(l/2)],seq[round(l/2):])
        seq1=part(seq[:int(round(l/2))]);
        seq2=part(seq[int(round(l/2)):]);
        # print(seq1,seq2)
        sol=merge(seq1,seq2);
        return(sol);
c=part(a)

print(count)


#
#
# print(a[:int(round(21/2))])
# print(a[int(round(199900/2)):])


#
# # a.pop(1)
# # print(a)
#
# a.remove(1)
# print(a,len(a),range(3))
# for i in range(3):
#     print(i)
