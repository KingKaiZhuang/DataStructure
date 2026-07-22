while True:
    n1,n2=map(int,input().split())
    if n1==0 and n2==0:
        break
    total=0
    add=0
    while n1>0 or n2>0:
        remain1=n1%10
        remain2=n2%10
        if remain1+remain2+add>=10:
            total+=1
            add=1
        else:
            add=0
        n1//=10
        n2//=10
    
    if total==0:
        print("No carry operation.")
    elif total==1:
        print(f"{total} carry operation.")
    else:
        print(f"{total} carry operations.")