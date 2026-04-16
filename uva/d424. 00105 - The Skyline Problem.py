# input data
data=[]
while True:
    try:
        line=input()
        data.extend(line.split())
    except EOFError:
        break
# define
max_pos=10005
min_L=max_pos
max_R=0
house=[0]*max_pos
# outline
i=0
while i<len(data):
    L,H,R=int(data[i]),int(data[i+1]),int(data[i+2])
    i+=3
    
    if L<min_L:
        min_L=L
    if R>max_R:
        max_R=R

    for x in range(L,R):
        if house[x]<H:
            house[x]=H
# 判斷結果
cur=0
ans=[]
for i in range(min_L,max_R+1):
    if house[i]!=cur:
        ans.append(str(i))
        ans.append(str(house[i]))
        cur=house[i]

print(" ".join(ans))