while True:
    try:
        n,m,t,k=map(int,input().split())

        # position
        record=set()
        turtles={}
        for _ in range(t):
            turId,row,col=map(int,input().split())
            turtles[turId]=[row,col]
            record.add((row,col))

        # define dirs
        dirs={
            'N':(-1,0),
            'S':(1,0),
            'E':(0,1),
            'W':(0,-1),
            'NE':(-1,1),
            'NW':(-1,-1),
            'SE':(1,1),
            'SW':(1,-1)
        }

        # test case
        for _ in range(k):
            line=input().split()
            testId=int(line[0])
            dir=line[1]
            # update position
            curX,curY=turtles[testId]
            dx,dy=dirs[dir]
            newX,newY=dx+curX,dy+curY
            # refresh
            if 0<=newX<n and 0<=newY<m:
                if (newX,newY) not in record:
                    record.remove((curX,curY))
                    record.add((newX,newY))
                    turtles[testId]=[newX,newY]
        
        # draw
        for r in range(n):
            draw=""
            for c in range(m):
                if (r,c) in record:
                    draw+="*"
                else:
                    draw+=" "
            print(draw.rstrip())
        print()
        
    except EOFError:
        break