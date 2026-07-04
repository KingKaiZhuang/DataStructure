def sort_key(unit):
    return (-numDic[unit],ord(unit))

n=int(input())
record=[]
numDic={}

for _ in range(n):
    line=input().upper()    
    for c in line:
        if not c.isalpha():
            continue
        if c not in record:
            record.append(c)
            numDic[c]=1
        else:
            numDic[c]+=1

record.sort(key=sort_key)

for i in record:
    print(f"{i} {numDic[i]}")