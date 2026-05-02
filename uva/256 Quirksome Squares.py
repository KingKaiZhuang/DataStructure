# input
while True:
    try:
        n=int(input())
        # define
        maxN=int((10**n)**0.5)
        devision=(10**(n//2))
        # cal -> print result
        left,right=0,0
        for i in range(maxN):
            squareNum=i*i
            left=squareNum//devision
            right=squareNum%devision
            if left+right==i:
                ans=str(squareNum).zfill(n)
                print(ans)
    except EOFError:
        break