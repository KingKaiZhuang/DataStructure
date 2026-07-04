while True:
    try:
        n1,n2=map(int,input().split())
        a=max(n1,n2)
        b=min(n1,n2)
        print(a-b)
    except EOFError:
        break