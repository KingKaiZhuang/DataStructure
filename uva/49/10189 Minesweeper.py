title=1
isFirst=0

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break

    if isFirst>0:
        print()
    print(f"Field #{title}:")
    title+=1

    rec=[]
    for _ in range(n):
        rec.append(list(input()))
    
    dirs=[(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]

    for i in range(n):
        ans=""
        for j in range(m):
            count=0
            if rec[i][j]=="*":
                ans+="*"
            else:
                for k in dirs:
                    n1,n2=k
                    r=n1+i
                    c=n2+j

                    if 0<=r<n and 0<=c<m:
                        if rec[r][c]=="*":
                            count+=1
                ans+=str(count)
        print(ans)