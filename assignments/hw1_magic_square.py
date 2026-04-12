def squareFun(n):
    arr=[[0]*n for _ in range(n)]

    m=n//2
    x,y=0,m
    arr[0][m]=1

    for i in range(2,n*n+1):
        next_x=(x-1)%n
        next_y=(y-1)%n

        if arr[next_x][next_y]==0:
            arr[next_x][next_y]=i
        else:
            next_x=(x+1)%n
            next_y=y
            arr[next_x][next_y]=i

        x,y=next_x,next_y
    
    for  row in arr:
        for col in row:
            print(f"{col}",end=" ")
        print()
    print()

for i in [1,3,5,7,9]:
    squareFun(i)