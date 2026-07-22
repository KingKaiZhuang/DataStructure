testCase=int(input())

# a+b=n1
# a-b=n2
# 2a=n1+n2,a=n1/2
# 2b=n1-n2,b=(n1-n2)/2

for _ in range(testCase):
    n1,n2=map(int,input().split())

    if n1<n2 or (n1+n2)%2:
        print("impossible")
        continue
    else:
        a=(n1+n2)//2
        b=(n1-n2)//2
        print(f"{a} {b}")