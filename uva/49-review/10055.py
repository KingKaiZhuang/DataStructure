while True:
    try:
        n1,n2=map(int,input().split())
        if n1>n2:
            n1,n2=n2,n1

        print(n2-n1)
    except EOFError:
        break