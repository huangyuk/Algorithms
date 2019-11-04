def mult(x, y):
    if (len(x)==1)&(len(y)==1):
        single=int(x)*int(y)
        return single
    else:
        a=x[0:int(len(x)/2)]
        b=x[int(len(x)/2):len(x)]
        c=y[0:int(len(y)/2)]
        d=y[int(len(y)/2):len(y)]
        # ab=str(int(a)+int(b))
        # cd=str(int(c)+int(d))
        rec=10**len(x)*mult(a, c)+10**int(len(x)/2)*(int(a)*int(d)+int(b)*int(c))+mult(b, d)
        # rec=10**len(x)*mult(a, c)+10**int(len(x)/2)*(mult(a,d)+mult(b,c))+mult(b, d)
        return int(rec)


test1="3141592653589793238462643383279502884197169399375105820974944592"
test2="2718281828459045235360287471352662497757247093699959574966967627"


test3=test1
test4=test2

c=mult(test3,test4)

print(c,int(test3)*int(test4),c==int(test3)*int(test4))
