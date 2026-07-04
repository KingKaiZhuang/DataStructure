while True:
    try:
        # input
        n=int(input())
        if n==0:
            break
        record=[]
        for _ in range(2*n):
            line=input().split()
            x,y,act=int(line[0]),int(line[1]),line[2]
            record.append((x,y,act))

        # calculate
        current=set()
        history=set()
        gameOver=False
        winner=-1
        step=0
        for i in range(2*n):
            r,c,a=record[i]
            if a=="+":
                current.add((r,c))
            else:
                current.discard((r,c))
            # (1,4)->(4,4)
            deg_0=frozenset((n1,n2) for n1,n2 in current)
            deg_90=frozenset((n2,n-n1+1) for n1,n2 in current)
            deg_180=frozenset((n-n1+1,n-n2+1) for n1,n2 in current)
            deg_270=frozenset((n-n2+1,n-(n-n1+1)+1) for n1,n2 in current)

            if deg_0 in history or deg_90 in history or deg_180 in history or deg_270 in history:
                gameOver=True
                winner=2 if i%2==0 else 1
                step=i+1
                break
            else:
                history.add(deg_0)
        
        if gameOver:
            print(f"Player {winner} wins on move {step}")
        else:
            print("Draw")

    except EOFError:
        break