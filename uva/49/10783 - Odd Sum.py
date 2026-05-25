testNum=int(input())
caseNum=1

for _ in range(testNum):
    left=int(input())
    if left%2==0:
        left+=1
    right=int(input())
    total=0
    if left==0 and right==0:
        print(f"Case {caseNum}: {total}")
        caseNum+=1
        continue

    for i in range(left,right+1,2):
        total+=i
    print(f"Case {caseNum}: {total}")
    caseNum+=1
