def permutation(a,k,m):
    if k==m:
        for i in range(len(a)):
            print(f"{a[i]}",end="")
        print()
    else:
        for j in range(k,m+1):
            a[k],a[j]=a[j],a[k]
            permutation(a,k+1,m)
            a[k],a[j]=a[j],a[k]

a=['a','b','c']
k,m=0,len(a)-1
permutation(a,k,m)