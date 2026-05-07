record=[0]*10005
maxN,minN=0,10005

while True:
    try:
        line=input().split()
        left,h,right=map(int,line)

        if left<minN:
            minN=left
        if right>maxN:
            maxN=right

        # record height
        for i in range(left,right):
            if h>record[i]:
                record[i]=h
    except EOFError:
        break

# max left->max right
curH=0
ans=[]
for j in range(minN,maxN+1):
    if record[j]!=curH:
        ans.append(j)
        ans.append(record[j])
        curH=record[j]
print(*ans)