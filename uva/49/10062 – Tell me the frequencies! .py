def sort_key(n):
    return(numDic[n],-n)

isFirst=True
while True:
    try:
        rec=[]
        numDic={}
        line=input()
        
        if isFirst!=True:
            print()

        for i in line:
            asc=ord(i)
            if asc not in rec:
                rec.append(asc)
                numDic[asc]=1
            else:
                numDic[asc]+=1
        rec.sort(key=sort_key)
        for j in rec:
            print(f"{j} {numDic[j]}")
        
        isFirst=False
    except EOFError:
        break   