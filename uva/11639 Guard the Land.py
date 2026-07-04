n=int(input())

for i in range(1,n+1):
    x1_round1,y1_round1,x2_round1,y2_round1=map(int,input().split())
    x1_round2,y1_round2,x2_round2,y2_round2=map(int,input().split())
    # strongly
    x1=max(x1_round1,x1_round2)
    x2=min(x2_round1,x2_round2)
    y1=max(y1_round1,y1_round2)
    y2=min(y2_round1,y2_round2)

    n1=max(0,x2-x1)
    n2=max(0,y2-y1)
    strongly=n1*n2
    # weakly
    rec1=(x2_round1-x1_round1)*(y2_round1-y1_round1)
    rec2=(x2_round2-x1_round2)*(y2_round2-y1_round2)
    weakly=rec1+rec2-strongly*2
    # unsecured
    unsecured=10000-strongly-weakly
    print(f"Night {i}: {strongly} {weakly} {unsecured}")