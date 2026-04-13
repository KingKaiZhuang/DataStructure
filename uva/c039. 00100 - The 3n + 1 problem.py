while True:
    try:
        left,right=map(int,input().split())    
        maxN=0
        print(f"{left} {right}",end=" ")
        if left>right:
            left,right=right,left

        for n in range(left,right+1):
            count=1
            while n!=1:
                if n%2!=0:
                    n=3*n+1
                else:
                    n=n//2
                count+=1
            if count>maxN:
                maxN=count
        print(maxN)
    except EOFError:
        break