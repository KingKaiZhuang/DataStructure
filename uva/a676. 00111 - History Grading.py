while True:
    try:
        line=input().split()
        if len(line)==1:
            n=int(line[0])
            ansList=list(map(int,input().split()))
            ansSeq=[0]*n
            for i in range(n):
                ansSeq[ansList[i]-1]=i+1
            print(ansSeq)
        else:
            stuList=list(map(int,line))
            stuSeq=[0]*n
            for i in range(n):
                stuSeq[stuList[i]-1]=i+1
            print(stuSeq)
            # LCS
            arr=[[0]*(n+1) for _ in range(n+1)]
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if ansSeq[i-1]==stuSeq[j-1]:
                        arr[i][j]=arr[i-1][j-1]+1
                    else:
                        arr[i][j]=max(arr[i][j-1],arr[i-1][j])
            print(arr[n][n])
    except EOFError:
        break