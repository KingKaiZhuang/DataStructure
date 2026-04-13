def search_pos(blocks,n,a):
    for r in range(n):
        for c in range(len(blocks[r])):
            if blocks[r][c]==a:
                return r,c
    return -1,-1

def clear_top(blocks,r,c):
    while len(blocks[r])>c+1:
        val=blocks[r].pop()
        blocks[val].append(val)

while True:
    try:
        n=int(input())
        blocks=[]
        for i in range(n):
            blocks.append([i])
    except EOFError:
        break
    
    while True:
        line=input()
        if line=="quit":
            break

        command=line.split()
        act1,act2=command[0],command[2]
        a,b=int(command[1]),int(command[3])

        r1,c1=search_pos(blocks,n,a)
        r2,c2=search_pos(blocks,n,b)

        if act1=="move":
            clear_top(blocks,r1,c1)
        if act2=="onto":
            clear_top(blocks,r2,c2)

        move_list=blocks[r1][c1:]
        blocks[r1]=blocks[r1][:c1]

        for u in move_list:
            blocks[r2].append(u)

    for i in range(n):
        listNum=""
        for j in range(len(blocks[i])):
            listNum+=" "+str(blocks[i][j])
        print(f"{i}:"+listNum)