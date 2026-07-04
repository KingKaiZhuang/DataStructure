def get_position(blocks,target,n):
    for i in range(n):
        for j in range(len(blocks[i])):
            if blocks[i][j]==target:
                return i,j
    return -1,-1

def clear_top(blocks,r1,c1):
    while len(blocks[r1])-1>c1:
        tmp=blocks[r1].pop()
        blocks[tmp].append(tmp)

while True:
    try:
        # input
        n=int(input())
        blocks=[[i] for i in range(n)]
        # command
        while True:
            line=input()
            if line=="quit":
                break
            command=line.split()
            act1,n1,act2,n2=command[0],int(command[1]),command[2],int(command[3])
            # position
            r1,c1=get_position(blocks,n1,n)
            r2,c2=get_position(blocks,n2,n)
            if r1==r2 or n1==n2:
                continue
            # clear
            if act1=="move":
                clear_top(blocks,r1,c1)
            if act2=="onto":
                clear_top(blocks,r2,c2)
            # move
            moveList=blocks[r1][c1:]
            blocks[r2].extend(moveList)
            blocks[r1]=blocks[r1][:c1]
        
        for i in range(n):
            print(f"{i}:",*blocks[i])
    except EOFError:
        break