while True:
    n1,n2=map(int,input().split())
    if n1==0 and n2==0:
        break
    ans=int(n2**0.5)-int((n1-1)**0.5)
    print(ans)