record=[]
while True:
    try:
        line=input()
        record.append(line)
    except EOFError:
        break

maxL=0
for r in record:
    if len(r)>maxL:
        maxL=len(r)

for j in range(maxL):
    ans=""
    for i in range(len(record)-1,-1,-1):
        if len(record[i])>j:
            ans+=record[i][j]
        else:
            ans+=" "
    print(ans)