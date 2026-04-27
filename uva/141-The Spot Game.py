while True:
    n=int(input())
    if n==0:
        break
    
    # input
    moves=[]
    for _ in range(2*n):
        line=input().split()
        r=int(line[0])
        c=int(line[1])
        act=line[2]
        moves.append((r,c,act))
    # rotating -> history
    history=set()
    gameOver=False
    current=set()
    winner=0
    moveEnd=0
    
    for i in range(2*n):
        r,c,act=moves[i]
        if act=="+":
            current.add((r,c))
        else:
            current.discard((r,c))
        if not gameOver:
            state_0=frozenset((x,y) for x,y in current)
            state_90=frozenset((y,n-x+1) for x,y in current)
            state_180=frozenset((n-x+1,n-(y)+1) for x,y in current)
            state_270=frozenset((n-(y)+1,n-(n-x+1)+1) for x,y in current)

            if state_0 in history or state_90 in history or state_180 in history or state_270 in history:
                gameOver=True
                winner=2 if i%2==0 else 1
                moveEnd=i+1
                break
            else:
                history.add(state_0)
    # output
    if gameOver:
        print(f"Player {winner} wins on move {moveEnd}")
    else:
        print("Draw")