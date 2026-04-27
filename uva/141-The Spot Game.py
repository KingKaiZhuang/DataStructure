# input
while True:
    n=int(input())
    if n==0:
        break
    moves=[]
    for _ in range(n*2):
        line=input().split()
        r,c,act=int(line[0]),int(line[1]),line[2]
        moves.append((r,c,act))        
    # record history
    history=set()
    current=set()
    gameOver=False
    winner=0
    moveEnd=0
    
    for i in range(n*2):
        r,c,act=moves[i]

        if not gameOver:
            if act=='+':
                current.add((r,c))
            else:
                current.discard((r,c))
            # rotate cal
            state_0=frozenset((x,y) for x,y in current)
            state_90=frozenset((y,n-x+1) for x,y in current)
            state_180=frozenset((n-x+1,n-y+1) for x,y in current)
            state_270=frozenset((n-y+1,n-(n-y+1)+1) for x,y in current)

            if state_0 in history or state_90 in history or state_180 in history or state_270 in history:
                gameOver=True
                winner= 2 if i%2==0 else 1
                endMove=i+1
                break
            else:
                history.add(state_0)
    
    if gameOver:
        print(f"Player {winner} wins on move {endMove}")
    else:
        print("Draw")