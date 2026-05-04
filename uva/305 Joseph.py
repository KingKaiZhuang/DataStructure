# define func m
def joseph(k,m):
    curPos=0
    remains=0
    for i in range(k):
        remains=2*k-i
        curPos=(curPos+m-1)%remains
        if curPos<k:
            return False
    return True
# define record 14
record=[0]*14
for k in range(1,14):
    m=1
    while not joseph(k,m):
        m+=1
    record[k]=m
# input
while True:
    n=int(input())
    if n==0:
        break
    print(record[n])