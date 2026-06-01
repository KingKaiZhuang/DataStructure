while True:
    try:
        line=input().split()
        s=int(line[0])
        n=line[1]

        if s==0 and n=="0":
            break

        # Define Seven Json
        digs={
            "0":[1,1,1,1,1,1,0],
            "1":[0,1,1,0,0,0,0],
            "2":[1,1,0,1,1,0,1],
            "3":[1,1,1,1,0,0,1],
            "4":[0,1,1,0,0,1,1],
            "5":[1,0,1,1,0,1,1],
            "6":[1,0,1,1,1,1,1],
            "7":[1,1,1,0,0,0,0],
            "8":[1,1,1,1,1,1,1],
            "9":[1,1,1,1,0,1,1]
        }
        # Def horizantal
        def horizantal(num):
            for k,c in enumerate(n):
                if digs[c][num]==1:
                    print(f" {'-'*s} ",end="")
                else:
                    print(f" {' '*s} ",end="")
                if k<len(n)-1:
                    print(" ",end="")
            print()
        # Def verticle
        def verticle(left,right):
            for _ in range(s):
                for k,c in enumerate(n):
                    leftDisplay='|' if digs[c][left]==1 else " "
                    rightDisplay='|' if digs[c][right]==1 else " "
                    combine=leftDisplay+" "*s+rightDisplay
                    print(combine,end="")
                    if k<len(n)-1:
                        print(" ",end="")
                print()
                        
        # Call function
        horizantal(0)
        verticle(5,1)
        horizantal(6)
        verticle(4,2)
        horizantal(3)
        # gap
        print()

    except EOFError:
        break