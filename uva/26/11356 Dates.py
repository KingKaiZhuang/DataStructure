month=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
dayList1=[31,28,31,30,31,30,31,31,30,31,30,31]
dayList2=[31,29,31,30,31,30,31,31,30,31,30,31]

while True:
    try:
        testCase=int(input())

        for i in range(testCase):
            line=input().split("-")
            curYear,curMonth,curDay=int(line[0]),line[1],int(line[2])
            passDay=int(input())

            monIndex=month.index(curMonth)
            while passDay>0:
                if (curYear%400==0) or (curYear%4==0 and curYear%100!=0):
                    dayList=dayList2
                else:
                    dayList=dayList1

                curDay+=1

                if curDay>dayList[monIndex]:
                    curDay=1
                    monIndex+=1

                    if monIndex==12:
                        monIndex=0
                        curYear+=1
                
                passDay-=1
            print(f"Case {i+1}: {curYear}-{month[monIndex]}-{curDay:02d}")

    except EOFError:
        break