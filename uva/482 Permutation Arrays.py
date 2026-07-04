while True:
    try:
        t=int(input())

        for _ in range(t):
            emp=input()
            rec={}
            flagList=list(map(int,input().split()))
            numList=input().split()
            length=len(numList)

            for i in range(length):
                rec[flagList[i]]=numList[i]

            sortList=sorted(flagList)
            for j in sortList:
                print(rec[j])
    except EOFError:
        break