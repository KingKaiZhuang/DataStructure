house=[0]*10005
minN=9999
maxN=0
# input
while True:
    try:
        line=input()
        if not line:
            break
        data=list(map(int,line.split()))
        left,H,right=data[0],data[1],data[2]

        if left<minN:
            minN=left
        if right>maxN:
            maxN=right

        # height def
        for i in range(left,right):
            if house[i]<H:
                house[i]=H
    except EOFError:
        break

# output
curH=0
record=[]
for j in range(minN,maxN+1):
    if house[j]!=curH:
        record.append(str(j))
        record.append(str(house[j]))
        curH=house[j]

ans=" ".join(record)
print(ans)