# def fun
def perfection(n):
    total=1
    if n==1:
        return 0
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            total+=j
            if j!=n//j:
                total+=n//j        
    return total


print("PERFECTION OUTPUT")
# input -> for -> func
while True:
    try:
        line=input().split()
        for i in line:
            if i=='0':
                print("END OF OUTPUT")
                break
            num=int(i)
            ans=perfection(num)

            if ans==num:
                print(f"{num:>5}  PERFECT")
            elif ans<num:
                print(f"{num:>5}  DEFICIENT")
            else:
                print(f"{num:>5}  ABUNDANT")
    except EOFError:
        break