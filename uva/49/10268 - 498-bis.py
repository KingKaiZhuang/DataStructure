while True:
    try:
        n=int(input())
        line=list(map(int,input().split()))

        r=len(line)-1
        total=0
        current=1

        for i in range(r-1,-1,-1):
            total+=(r-i)*line[i]*current
            current*=n
        print(total)
    except EOFError:
        break