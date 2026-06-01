caseNum=1

while True:
    t=int(input())
    if t==0:
        break
    line=list(map(int,input().split()))
    # average
    ave=sum(line)//t
    count=0
    # count = every high - average high
    for h in line:
        if h>ave:
            count+=h-ave
    # output answer
    print(f"Set #{caseNum}")
    caseNum+=1
    print(f"The minimum number of moves is {count}.")