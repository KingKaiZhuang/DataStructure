def print_magic_square(n):
    print(f"{n} 階模方陣")

    grid=[[0]*n for _ in range(n)]

    i=0
    j=n//2
    grid[i][j]=1

    for k in range(2,n*n+1):
        next_i=(i-1)%n
        next_j=(j-1)%n

        if grid[next_i][next_j]!=0:
            next_i=(i+1)%n
            next_j=j

        i=next_i
        j=next_j
        grid[i][j]=k


    for r in grid:
        for num in r:
            print(f"{num:3d}", end=" ")
        print()
    print()

for n in [1,3,5,7,9]:
    print_magic_square(n)