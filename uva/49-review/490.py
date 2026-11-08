rec=[]

while True:
    try:
        s=input()
        if s=="":
            break
        rec.append(s)
    except EOFError:
        break

maxLen=-1
for r in rec:
    if maxLen<len(r):
        maxLen=len(r)

for r in range(maxLen):
    for k in range(len(rec)-1,-1,-1):
        if len(rec[k])>r:
            print(rec[k][r],end="")
        else:
            print(" ",end="")
    print()