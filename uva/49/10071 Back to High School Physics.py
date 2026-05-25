while True:
    try:
        n1,n2=map(int,input().split())
        print(n1*n2*2)
    except EOFError:
        break