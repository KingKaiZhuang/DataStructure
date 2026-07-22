r,c=map(int,input().split())
dirs=['N','E','S','W']
dir=[(0,1),(1,0),(0,-1),(-1,0)]
scents=set()

while True:
    try:
        line1=input().split()
        x,y,d=int(line1[0]),int(line1[1]),line1[2]
        line2=input().strip()
        index=dirs.index(d)
        lost=False
        # analyze
        for i in line2:
            if i=="L":
                index=(index-1)%4
                d=dirs[index]
            elif i=="R":
                index=(index+1)%4
                d=dirs[index]
            else:
                n1,n2=dir[index]
                nextX,nextY=n1+x,n2+y
                if 0<=nextX<=r and 0<=nextY<=c:
                    x,y=nextX,nextY
                else:
                    if (x,y) not in scents:
                        scents.add((x,y))
                        lost=True
                        break
                    else:
                        continue
        
        if lost:
            print(f"{x} {y} {d} LOST")
        else:
            print(f"{x} {y} {d}")
            
    except EOFError:
        break