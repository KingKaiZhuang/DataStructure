isFirst=True

while True:
    n=int(input())

    if n==0:
        break
    
    a=[1]

    if isFirst==False:
        print()
    isFirst=True

    for i in range(1,n+1):
        carry=0
        for j in range(len(a)):
            tmp=a[j]*i+carry
            a[j]=tmp%10
            carry=tmp//10

        while carry>0:
            a.append(carry%10)
            carry//=10

        ans="".join(str(j) for j in reversed(a))
        print(f"{i}!={ans}")