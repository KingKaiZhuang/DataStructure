while True:
    try:
        nList=list(map(int,input().split()))
        caseNum=nList[0]
        nList=nList[1:]
        rec=[]

        for i in range(1,caseNum):
            rec.append(abs(nList[i-1]-nList[i]))

        isJolly=True
        for j in range(1,len(rec)+1):
            if j not in rec:
                isJolly=False
                break

        if isJolly:
            print("Jolly")
        else:
            print("Not jolly")

    except EOFError:
        break