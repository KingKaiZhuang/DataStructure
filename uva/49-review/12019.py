weeks=[ "Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday"]
days=[31,28,31,30,31,30,31,31,30,31,30,31]

caseNum=int(input())
for _ in range(caseNum):
    m,d=map(int,input().split())
    total=0

    for i in range(m-1):
        total+=days[i]
    total+=d

    print(weeks[total%7])