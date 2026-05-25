def sort_key(num):
    tmp=num%m
    if num<0 and tmp>0:
        tmp-=m

    if num%2!=0:
        isOdd=0
        last=-1*num
    else:
        isOdd=1
        last=num
    return (tmp,isOdd,last)

while True:
    n,m=map(int,input().split())
    print(n,m)
    if n==0 and m==0:
        break
    nList=[]
    for _ in range(n):
        nList.append(int(input()))
    
    nList.sort(key=sort_key)

    for i in nList:
        print(i)