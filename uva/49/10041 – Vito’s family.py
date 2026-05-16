tCase=int(input())

for _ in range(tCase):
    line=list(map(int,input().split()))
    n=line[0]
    line=line[1:]
    line.sort()

    mid=len(line)//2
    midN=line[mid]
    ans=0

    for i in line:
        ans+=abs(midN-i)
    print(ans)