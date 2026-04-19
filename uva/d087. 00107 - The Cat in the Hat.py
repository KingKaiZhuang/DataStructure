while True:
    # input
    H,W=map(int,input().split())
    if H==0 and W==0:
        break
    if H==1 and W==0:
        print("0 1")
    # (N+1)^k=H, N^k=W
    N,K=0,0
    for i in range(1,40):
        n1=round(H**(1/i))
        n2=round(W**(1/i))

        if n2+1==n1 and n1**i==H and n2**i==W:
            N,K=n2,i
            break
    # ans
    nonWorker,totalHeight,curCat,curH=0,0,1,H
    for j in range(K+1):
        if j<K:
            nonWorker+=curCat
        totalHeight+=curH*curCat
        curCat*=N
        curH//=(N+1)

    print(f"{nonWorker} {totalHeight}")