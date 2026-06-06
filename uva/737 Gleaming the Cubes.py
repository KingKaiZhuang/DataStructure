while True:
    try:
        n=int(input().strip())
        if n==0:
            break

        # left side
        x1,y1,z1,width1=0,0,0,0
        # right side
        x2,y2,z2,width2=10000,10000,10000,10000

        for _ in range(n):
            x,y,z,width=map(int,input().split())

            x1=max(x1,x)
            y1=max(y1,y)
            z1=max(z1,z)

            x2=min(x2,x+width)
            y2=min(y2,y+width)
            z2=min(z2,z+width)

        n1=max(0,x2-x1)
        n2=max(0,y2-y1)
        n3=max(0,z2-z1)

        print(n1*n2*n3)

    except EOFError:
        break