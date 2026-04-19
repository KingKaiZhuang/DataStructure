while True:
    try:
        line=input().strip()
        H,W=map(int,line.split())

        if H==0 and W==0:
            break
            
        if H==1:
            print("0 1")
            continue

        N,k=0,0
        for steps in range(1,40):
            n1=round(H**(1/steps))
            n=round(W**(1/steps))

            if n+1==n1 and n1**steps==H and n**steps==W:
                N=n
                k=steps
                break
        
        nonWork=0
        totalHeight=0
        curCat=1
        curHeight=H

        for i in range(k+1):
            if i<k:
                nonWork+=curCat
            totalHeight+=curCat*curHeight
            curCat*=N
            curHeight//=(N+1)
        
        print(f"{nonWork} {totalHeight}")
                
    except EOFError:
        break