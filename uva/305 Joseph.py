# joseph function
def joseph(k,m):
    remains,pos=0,0
    for i in range(k):
        remains=2*k-i
        pos=(pos+m-1)%remains
        if pos<k:
            return False
    return True
# record
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
    ans=record[n]
    print(ans)