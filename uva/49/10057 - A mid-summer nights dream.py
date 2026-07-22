while True:
    try:
        n=int(input())
        rec=[]
        for _ in range(n):
            rec.append(int(input()))
        
        rec.sort()
        length=len(rec)

        if length%2!=0:
            mid1=rec[length//2]
            mid2=rec[length//2]
        else:
            mid1=rec[length//2-1]
            mid2=rec[length//2]

        ans2=0
        for i in rec:
            if mid1<=i<=mid2:
                ans2+=1

        ans3=mid2-mid1+1

        print(f"{mid1} {ans2} {ans3}")
    except EOFError:
        break