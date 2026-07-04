while True:
    try:
        line=list(map(int,input().split()))
        n=line[0]
        line=line[1:]
        record=[]
        isJolly=True
        
        for i in range(n-1):
            gap=abs(line[i+1]-line[i])
            record.append(gap)
        
        record.sort()
        for j in range(len(record)-1):
            analyze=abs(record[j+1]-record[j])
            if analyze!=1:
                isJolly=False
                break
        
        if isJolly:
            print("Jolly")
        else:
            print("Not jolly")
    except EOFError:
        break