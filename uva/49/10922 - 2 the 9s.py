def degCal(num,dep):
    if num=="9" and dep==0:
        return 1
    
    total=0
    for i in range(len(num)):
        total+=int(num[i])
    dep+=1
    if total==9:
        return dep
    elif total<9:
        return 0
    else:
        return degCal(str(total),dep)

while True:
    n=input()
    if n=="0":
        break
    
    depth=0
    ans=degCal(n,depth)

    if ans>0:
        print(f"{n} is a multiple of 9 and has 9-degree {ans}.")
    else:
        print(f"{n} is not a multiple of 9.")