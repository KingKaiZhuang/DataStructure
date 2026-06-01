while True:
    try:
        line=input().split()
        if len(line)==0:
            continue
        s=int(line[0])
        n=line[1]
        if s==0 and n=="0":
            break
        # Define nine numbers
        digs={
            '0':[1,1,1,1,1,1,0],
            '1':[0,1,1,0,0,0,0],
            '2':[1,1,0,1,1,0,1],
            '3':[1,1,1,1,0,0,1],
            '4':[0,1,1,0,0,1,1],
            '5':[1,0,1,1,0,1,1],
            '6':[1,0,1,1,1,1,1],
            '7':[1,1,1,0,0,0,0],
            '8':[1,1,1,1,1,1,1],
            '9':[1,1,1,1,0,1,1]
        }
        # first row -> last row
        # Define Horizental
        def horizontal(segIndex):
            for k,i in enumerate(n):
                char='-' if digs[i][segIndex]==1 else ' '
                print(f" {char*s} ",end="")
                if k<len(n)-1:
                    print(" ",end="")
            print()

        # Define Verticle
        def vertical(left,right):
            for _ in range(s):
                for k,i in enumerate(n):
                    charL="|" if digs[i][left] else ' '
                    charR="|" if digs[i][right] else ' '
                    print(f"{charL}{s*' '}{charR}",end="")
                    if k<len(n)-1:
                        print(" ",end="")
                print()
            
        horizontal(0)
        vertical(5,1)
        horizontal(6)
        vertical(4,2)
        horizontal(3)
        print()
    except EOFError:
        break