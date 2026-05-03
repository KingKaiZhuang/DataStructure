while True:
    try:
        # input
        n=int(input())
        # in which line?
        tmp,level=1,1
        while tmp<n:
            level+=1
            tmp+=level
        
        # cal line - n
        duration=tmp-n
        
        n1,n2=0,0
        if level%2==1:
            n1=1+duration
            n2=level-duration
        else:
            n1=level-duration
            n2=1+duration
        
        print(f"TERM {n} IS {n1}/{n2}")

    except EOFError:
        break