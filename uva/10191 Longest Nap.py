testCase=1

while True:
    try:
        n=int(input())
        rec=[]
        # Record the start time and end time
        for _ in range(n):
            line=input().split()
            startString,endString=line[0],line[1]
            h1,m1=startString.split(":")
            h2,m2=endString.split(":")
            startMin,endMin=int(h1)*60+int(m1),int(h2)*60+int(m2)
            # save into record
            rec.append((startMin,endMin))
        
        # calculate the max snap time section
        # start at 10:00 am -> 600min
        # last at 18:00 pm -> 1080
        lastTime=600
        maxSnap=0
        bestStart=600

        for start,end in rec:
            snapGap=start-lastTime
            if snapGap>maxSnap:
                maxSnap=snapGap
                bestStart=lastTime
            lastTime=end

        endSnap=1080-lastTime
        if endSnap>maxSnap:
            maxSnap=endSnap
            bestStart=lastTime

        # update the output display time
        hourResult=bestStart//60
        minutesResult=bestStart%60
        resultHour=maxSnap//60
        resultMin=maxSnap%60

        # Display
        if maxSnap>=60:
            print(f"Day #{testCase}: the longest nap starts at {hourResult}:{minutesResult:02d} and will last for {resultHour} hours and {resultMin} minutes.")
        else:
            print(f"Day #{testCase}: the longest nap starts at {hourResult}:{minutesResult:02d} and will last for {resultMin} minutes.")

        testCase+=1

    except EOFError:
        break