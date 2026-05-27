while True:
    try:
        t=int(input())
        emp=input()

        for caseNum in range(t):
            r,c=map(int,input().split())
            rec=[]
            for _ in range(r):
                rec.append(input().lower())

            test=int(input())

            # define eight dirs
            dirs=[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

            for _ in range(test):
                line=input().lower()
                found=False
                # search first location

                for j in range(r):
                    if found:
                        break
                    for k in range(c):
                        if found:
                            break
                        if rec[j][k]==line[0]:
                            # check the road is ok
                            for dr,dc in dirs:
                                match=True
                                for l in range(len(line)):
                                    n1=j+dr*l
                                    n2=k+dc*l

                                    if n1<0 or n1>=r or n2<0 or n2>=c or rec[n1][n2]!=line[l]:
                                        match=False
                                        break
                                # if ok: print first location
                                if match:
                                    print(f"{j+1} {k+1}")
                                    found=True
                                    break
            if caseNum<t-1:
                emp=input()
    except EOFError:
        break
