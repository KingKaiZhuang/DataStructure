# function analyze
def perfection(n):
    total=1
    lim=int(n**0.5)
    for j in range(2,lim+1):
        if n%j==0:
            total+=j
            if j!=n//j:
                total+=n//j
    return total
# input
isEnd=False
while True:
    if isEnd==True:
        break
    print("PERFECTION OUTPUT")
    line=input().split()
    for i in line:
        if i=="0":
            print("END OF OUTPUT")
            isEnd=True
            break
        num=int(i)
        ans=perfection(num)
        if ans==num:
            print(f"{i:>5}  PERFECT")
        elif ans>num:
            print(f"{i:>5}  ABUNDANT")
        else:
            print(f"{i:>5}  DEFICIENT")