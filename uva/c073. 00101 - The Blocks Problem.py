def search_position(blocks,n,target):
    for r in range(n):
        for c in range(len(blocks[r])):
            if blocks[r][c]==target:
                return r,c
    return -1,-1

def clear_above(blocks,r,c):
    while len(blocks[r])>c+1:
        val=blocks[r].pop()
        blocks[val].append(val)

while True:
    try:
        n=int(input())
        blocks=[]
        for i in range(n):
            blocks.append([i])

        while True:
            line=input().strip()
            if line=="quit":
                break

            command=line.split()

            action1,action2=command[0],command[2]
            a,b=int(command[1]),int(command[3])


            r1,c1=search_position(blocks,n,a)
            r2,c2=search_position(blocks,n,b)

            if a==b or r1==r2:
                continue

            if action1=="move":
                clear_above(blocks,r1,c1)
            if action2=="onto":
                clear_above(blocks,r2,c2)

            move_list=blocks[r1][c1:]
            blocks[r1]=blocks[r1][:c1]

            for val in move_list:
                blocks[r2].append(val)

        for i in range(n):
            out=str(i)+":"
            for val in blocks[i]:
                out+=" "+str(val)
            print(out)
    except EOFError:
        break