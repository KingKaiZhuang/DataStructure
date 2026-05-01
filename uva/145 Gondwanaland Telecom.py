# input
while True:
    line=input()
    if line=="#":
        break
    detail=line.split()
    step,phone,h1,m1,h2,m2=detail[0],detail[1],int(detail[2]),int(detail[3]),int(detail[4]),int(detail[5])

    # minute duration
    n1=h1*60+m1
    n2=h2*60+m2

    if n1==n2:
        duration=1440
    elif n1<n2:
        duration=n2-n1
    else:
        duration=(1440-n1)+n2

    curTime=n1
    day,eve,night=0,0,0
    # cal day eve night
    for _ in range(duration):
        if 8*60<=curTime<18*60:
            day+=1
        elif 18*60<=curTime<22*60:
            eve+=1
        else:
            night+=1

        curTime=(curTime+1)%1440
    # define rate
    rate={
        'A':[0.10,0.06,0.02],
        'B':[0.25,0.15,0.05],
        'C':[0.53,0.33,0.13],
        'D':[0.87,0.47,0.17],
        'E':[1.44,0.80,0.30]
    }
    # cal charge
    total=0
    r1,r2,r3=rate[step]
    total=r1*day+r2*eve+r3*night
    # print result
    print(f"{phone:>10}{day:>6}{eve:>6}{night:>6}{step:>3}{total:>8.2f}")