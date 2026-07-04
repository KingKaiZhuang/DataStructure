tCase=int(input())

for _ in range(tCase):
    line=input().split()
    n1,n2,n3=int(line[0]),float(line[1]),int(line[2])
    lose=1-n2
    
    ans=(n2*lose**(n3-1))/(1-lose**n1)
    print(f"{ans:.4f}")