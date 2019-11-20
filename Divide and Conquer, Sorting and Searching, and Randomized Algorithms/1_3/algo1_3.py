xfile=open('QuickSort.txt','r')

seq=list()

for lines in xfile:
    seq.append(int(lines));

def med(seq):
    a=list();
    a.append(seq[0]);
    if len(seq)%2==1:
        m=int((len(seq)-1)/2)
        a.append(seq[m]);
    else:
        m=int(len(seq)/2)-1
        a.append(seq[m]);
    a.append(seq[len(seq)-1]);
    a.sort()
    if seq[0]==a[1]:
        return 0;
    elif seq[m]==a[1]:
        return m;
    else:
        return (len(seq)-1)


m=0

def quick3(seq,first,last):
    global m;
    if first<last:
        m=m+last-first;
        medindex=first+med(seq[first:last+1])
        temp=seq[first];
        seq[first]=seq[medindex];
        seq[medindex]=temp;
        pivot=first;
        i=first+1;
        j=first+1;
        while i<=last:
            if seq[i]<=seq[pivot]:
                temp=seq[j];
                seq[j]=seq[i];
                seq[i]=temp;
                j=j+1;
            i=i+1;
        temp=seq[j-1];
        seq[j-1]=seq[pivot];
        seq[pivot]=temp;
        quick3(seq,first,j-2);
        quick3(seq,j,last);

quick3(seq,0,len(seq)-1);
print(seq,m);





#
#
# print(m)
