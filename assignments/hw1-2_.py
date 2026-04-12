isFirst=0

while True:
    n=int(input())

    if n==0:
        break

    if isFirst>0:
        print()
    isFirst+=1

    a=[1]

    for i in range(1,n+1):
        carry=0
        for j in range(len(a)):
            cur=a[j]*i+carry
            a[j]=cur%10
            carry=cur//10

        while carry>0:
            a.append(carry%10)
            carry//=10

        ans="".join(str(num) for num in reversed(a))
        
        print(f"{i}!={ans}")