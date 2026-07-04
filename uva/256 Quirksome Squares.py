while True:
    try:
        n=int(input())
        maxN=int((10**n)**0.5)
        separate=10**(n//2)

        left,right=0,0
        for i in range(maxN):
            num=i*i
            left=num//separate
            right=num%separate

            if left+right==i:
                ans=str(num).zfill(n)
                print(ans)

    except EOFError:
        break