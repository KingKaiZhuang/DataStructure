# input data
data=[]
while True:
    try:
        line=input()
        data.extend(map(int,line.split()))
    except EOFError:
        break
# define every height
house=[0]*10005
minN=10005
maxN=0
i=0
while i<len(data):
    L=data[i]
    H=data[i+1]
    R=data[i+2]
    i+=3

    if L<minN:
        minN=L
    if R>maxN:
        maxN=R

    for x in range(L,R):
        if H>house[x]:
            house[x]=H
# output
curH=0
record=[]
for i in range(minN,maxN+1):
    if house[i]!=curH:
        record.append(str(i))
        record.append(str(house[i]))
        curH=house[i]

ans=" ".join(record)
print(ans)