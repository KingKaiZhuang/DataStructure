def threen_fun(n):
    count=1
    while True:
        if n==1:
            break
        count+=1

        if n%2!=0:
            n=3*n+1
        else:
            n//=2
    return count

while True:
    try:
        start,end=map(int,input().split())
        print(f"{start} {end}",end=" ")
        if start>end:
            start,end=end,start
        maxN=-1
        for i in range(start,end+1):
            cal=threen_fun(i)
            if cal>maxN:
                maxN=cal
        print(f"{maxN}")
    except EOFError:
        break