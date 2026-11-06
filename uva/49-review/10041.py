testCase=int(input())

for _ in range(testCase):
    total=0
    numList=list(map(int,input().split()))
    numList=numList[1:]
    numList.sort()
    midNum=len(numList)//2

    for i in range(len(numList)):
        total+=abs(numList[i]-numList[midNum])
    print(total)
