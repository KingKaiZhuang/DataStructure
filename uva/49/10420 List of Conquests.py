testCase=int(input())
rec={}
names=[]

for _ in range(testCase):
    line=input().split()
    name=line[0]
    if name not in rec:
        rec[name]=1
        names.append(name)
    else:
        rec[name]+=1
    
names.sort()
for i in range(len(names)):
    print(f"{names[i]} {rec[names[i]]}")