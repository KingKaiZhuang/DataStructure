while True:
    try:
        # input
        n=int(input())
        # define 
        maxN=int((10**n)**0.5)
        devision=int((10**(n//2)))
        # cal
        left,right=0,0
        for i in range(maxN):
            num=i*i
            left=num//devision
            right=num%devision
            if (left+right)==i:
                ans=str(num).zfill(n)
                print(ans)
    except EOFError:
        break