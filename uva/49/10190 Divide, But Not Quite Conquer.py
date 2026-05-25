while True:
    try:
        n,m=map(int,input().split())
        if n==0 or m==0:
            print("Boring!")
            continue
        rec=[n]
        isBoring=False
        while n>1:
            if n%m!=0:
                isBoring=True
                break
            else:
                n//=m
                rec.append(n)
        
        if isBoring:
            print("Boring!")
        else:
            print(*rec)
    except EOFError:
        break